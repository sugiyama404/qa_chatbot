from sentence_transformers import SentenceTransformer
from . import utils

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

data_dir = "/opt/app"
model, df = utils.load_model_and_dataset(data_dir)
if model is None:
    model = SentenceTransformer.load(f"{data_dir}/model")

app = FastAPI()

class Query(BaseModel):
    query: str

@app.api_route('/', methods=['GET', 'HEAD'])
def read_root():
    """
    シンプルな挨拶メッセージを返すルートエンドポイント。
    """
    return {"Hello": "World"}

@app.api_route('/stage', methods=['POST', 'HEAD'])
def get_answer(query: Query):
    """
    answer API エンドポイント。
    このエンドポイントはリクエストボディにクエリ文字列を受け取り、
    内部データストアから取得したトップアンサーを返します。
    Args:
        query: ユーザーの質問を含むクエリ・オブジェクト。
    Returns:
        回答文字列またはエラーメッセージを含む辞書。
    """
    if query.query is None:
        return {"message": "Please input query"}
    try:
        return utils.get_answer(model, df, query.query)
    except (IndexError, ValueError) as e:
        return {"message": f"Error processing query: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
