
from sentence_transformers import util, SentenceTransformer, SentencesDataset, InputExample, losses, models
import pandas as pd
import torch
from torch.utils.data import DataLoader
import os

def load_model_and_dataset(data_dir: str) -> tuple[SentenceTransformer, pd.DataFrame]:
    """
    モデルとデータセットを読み込みます。
    Args:
        data_dir (str): データセットのディレクトリパス
    Returns:
        SentenceTransformer: 学習済みモデル
        pd.DataFrame: データセット
    """
    model = None
    if not os.path.exists(f"{data_dir}/model"):
        print("モデルが見つかりません。ダウンロードします。")
        model = _get_model(data_dir)
    else:
        print("モデルをロードします。")
        model = SentenceTransformer.load(f"{data_dir}/model")
    try:
        df = pd.read_csv(f"{data_dir}/qanda_transformer.csv")
        print("データセットを読み込みました。")
        return model, df
    except FileNotFoundError as e:
        print(f"データセットが見つかりません。パスを確認してください: {e.filename}")
        raise

def _get_unique_positives(df):
    """
    データフレームから重複を除いた `positive` 列の値をリストとして取得する関数
    Args:
        df: データフレーム
    Returns:
        重複を除いた `positive` 列の値のリスト
    """
    if not pd.api.types.is_string_dtype(df["positive"]):
        raise TypeError("`positive` column must be of string dtype")

    unique_positives = []
    for value in df["positive"].unique():
        if value is not None:
            unique_positives.append(value)
    return unique_positives

def get_answer(model: SentenceTransformer ,df: pd.DataFrame ,query: str)->dict:
    """
    指定されたクエリに対する回答を取得する内部関数。
    Args:
        query: 質問文
    Returns:
        上位回答を含む辞書または、回答が見つからない場合は空の辞書
    """
    answers = _get_unique_positives(df)
    corpus_embeddings = model.encode(answers, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)
    cos_scores = util.cos_sim(query_embedding , corpus_embeddings)
    top_results = torch.topk(cos_scores, k=3)
    ans = []
    for idx in top_results[1][0]:
        ans.append({"answer": answers[idx]})
    return ans[0]

def _get_model(data_dir: str):
    '''
    QAデータセットからSentenceTransformerモデルを学習・保存します。
    Args:
        data_dir (str): データセットのディレクトリパス
    '''
    try:
        bert = models.Transformer('sonoisa/sentence-bert-base-ja-mean-tokens-v2')
        pooling = models.Pooling(bert.get_word_embedding_dimension())
        model = SentenceTransformer(modules=[bert, pooling])
        df = pd.read_csv(f'{data_dir}/qanda_transformer.csv')
        train_dataset = SentencesDataset([InputExample(texts=[row["anchor"], row["positive"], row["negative"]]) for index,row in df.iterrows()], model)
        train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=8)
        train_loss = losses.TripletLoss(model=model)
        model.fit(
                train_objectives=[(train_dataloader, train_loss)],
                epochs=5,
                evaluation_steps=1,
                warmup_steps=1,
                )
        model.save(path = f"{data_dir}/model")
    except FileNotFoundError as e:
        print(f"データセットが見つかりません。パスを確認してください: {e.filename}")
    except Exception as e:
        print(f"学習中にエラーが発生しました: {e}")

