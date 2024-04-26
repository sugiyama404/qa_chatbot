from sentence_transformers import SentenceTransformer
import pandas as pd
from . import utils
import os

"""
モデルとデータセットを読み込みます。
"""
model = None
if not os.path.exists("./app/model"):
    print("モデルが見つかりません。ダウンロードします。")
    model = utils.get_model()
else:
    print("モデルをロードします。")
    model = SentenceTransformer.load("./app/model")
try:
    df = pd.read_csv('./app/qanda_transformer.csv')
    print("データセットを読み込みました。")
except FileNotFoundError as e:
    print(f"データセットが見つかりません。パスを確認してください: {e.filename}")
    raise
