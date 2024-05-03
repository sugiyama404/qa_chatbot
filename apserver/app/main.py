import sys
sys.path.append('/opt')
from app.utils.main import get_answer
from app.utils.dao import Sentencedata, Query
from sentence_transformers import SentenceTransformer

from fastapi import FastAPI, BackgroundTasks
import uvicorn
import time
import os

app = FastAPI()

data_dir = "/opt/app"
data = Sentencedata()

@app.api_route('/', methods=['GET', 'HEAD'])
async def health_check(background_tasks: BackgroundTasks):
    """
    シンプルな挨拶メッセージを返すルートエンドポイント。
    ヘルスチェック用
    """
    if not os.path.isdir(data_dir + "/model"):
        background_tasks.add_task(data.add, data_dir)
    return {"Hello": "World"}

@app.api_route('/', methods=['POST', 'HEAD'])
def post_root(query: Query):
    return {"answer": f"this is root post....{query.query}"}

@app.api_route('/stage/', methods=['POST', 'HEAD'])
def post_answer2(query: Query):
    """
    answer API エンドポイント。
    このエンドポイントはリクエストボディにクエリ文字列を受け取り、
    内部データストアから取得したトップアンサーを返します。
    Args:
        query: ユーザーの質問を含むクエリ・オブジェクト。
    Returns:
        回答文字列またはエラーメッセージを含む辞書。
    """
    global data
    if query.query is None:
        return {"message": "Please input query"}
    try:
        if data.model == None:
            model = None
            for _ in range(30):
                if os.path.isdir(f"{data_dir}/model"):
                    model = SentenceTransformer.load(f"{data_dir}/model")
                    break
                time.sleep(10)
            if model != None:
                return get_answer(data.model, data.df, query.query)
            else:
                return {"message": "try again..."}
        else:
            return get_answer(data.model, data.df, query.query)
    except (IndexError, ValueError) as e:
        return {"message": f"Error processing query: {str(e)}"}

@app.api_route('/stage', methods=['POST', 'HEAD'])
def post_answer(query: Query):
    """
    answer API エンドポイント。
    このエンドポイントはリクエストボディにクエリ文字列を受け取り、
    内部データストアから取得したトップアンサーを返します。
    Args:
        query: ユーザーの質問を含むクエリ・オブジェクト。
    Returns:
        回答文字列またはエラーメッセージを含む辞書。
    """
    global data
    if query.query is None:
        return {"message": "Please input query"}
    try:
        if data.model == None:
            model = None
            for _ in range(30):
                if os.path.isdir(f"{data_dir}/model"):
                    model = SentenceTransformer.load(f"{data_dir}/model")
                    break
                time.sleep(10)
            if model != None:
                return get_answer(data.model, data.df, query.query)
            else:
                return {"message": "try again..."}
        else:
            return get_answer(data.model, data.df, query.query)
    except (IndexError, ValueError) as e:
        return {"message": f"Error processing query: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
