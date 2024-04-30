from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Query(BaseModel):
    query: str

@app.api_route('/', methods=['GET', 'HEAD'])
def read_root():
    return {"Hello": "World"}

@app.api_route('/', methods=['POST', 'HEAD'])
def test_answer(query: Query):
    if query.query is None:
        return {"message": "Please input query"}
    return {"answer": f"answer-{query.query}"}

@app.api_route('/stage', methods=['POST', 'HEAD'])
def get_answer(query: Query):
    if query.query is None:
        return {"message": "Please input query"}
    return {"answer": f"answer-{query.query}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
