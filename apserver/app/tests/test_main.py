import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_read_root():
    """
    GETメソッドによるルートエンドポイントの正常処理を検証するテスト
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_get_answer_with_query():
    """
    POSTメソッドによる正常処理テスト (クエリパラメータあり)
    """
    query = "天気はいかがですか？"
    response = client.post("/stage", json={"query": query})
    assert response.status_code == 200
    assert "answer" in response.json()

def test_get_answer_with_invalid_query():
    """
    クエリに不正な値が渡された場合の挙動を検証するテストケース
    """
    response = client.post("/stage", json={"query": None})
    assert response.status_code == 422
    res = response.json()
    assert res['detail'][0]['msg'] == "none is not an allowed value"

def test_get_answer_without_query():
    """
    クエリが省略された場合の挙動を検証するテストケース
    """
    response = client.post("/stage")
    assert response.status_code == 422
    res = response.json()
    assert res['detail'][0]['msg'] == "field required"
