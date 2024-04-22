from typing import Union
import torch
from sentence_transformers import util
from . import model, df

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/stage")
def get_answer(query: Query):
    if query.query is None:
        return {"message": "Please input query"}
    return _get_answer(query.query)

def _get_answer(query: str)->list:
    answers = list(df["positive"][~df["positive"].duplicated()])
    corpus_embeddings = model.encode(answers, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)
    cos_scores = util.cos_sim(query_embedding , corpus_embeddings)
    top_results = torch.topk(cos_scores, k=3)
    ans = []
    for idx in top_results[1][0]:
        ans.append({"answer": answers[idx]})
    return ans
