from typing import Union
import torch
from sentence_transformers import util
from . import model, df
from . import utils

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/")
def read_root():
    """
    シンプルな挨拶メッセージを返すルートエンドポイント。
    """
    return {"Hello": "World"}

@app.post("/stage")
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
        return _get_answer(query.query)
    except (IndexError, ValueError) as e:
        return {"message": f"Error processing query: {str(e)}"}

def _get_answer(query: str)->dict:
    """
    指定されたクエリに対する回答を取得する内部関数。
    Args:
        query: 質問文
    Returns:
        上位回答を含む辞書または、回答が見つからない場合は空の辞書
    """
    # answers = list(df["positive"][~df["positive"].duplicated()])
    answers = utils.get_unique_positives(df)
    corpus_embeddings = model.encode(answers, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)
    cos_scores = util.cos_sim(query_embedding , corpus_embeddings)
    top_results = torch.topk(cos_scores, k=3)
    ans = []
    for idx in top_results[1][0]:
        ans.append({"answer": answers[idx]})
    return ans[0]
