
from sentence_transformers import SentenceTransformer, SentencesDataset, InputExample, losses, models
import pandas as pd
from torch.utils.data import DataLoader

'''
QAデータセットからSentenceTransformerモデルを学習・保存します。
'''
def get_model():
    try:
        bert = models.Transformer('sonoisa/sentence-bert-base-ja-mean-tokens-v2')
        pooling = models.Pooling(bert.get_word_embedding_dimension())
        model = SentenceTransformer(modules=[bert, pooling])
        df = pd.read_csv('./app/qanda_transformer.csv')
        train_dataset = SentencesDataset([InputExample(texts=[row["anchor"], row["positive"], row["negative"]]) for index,row in df.iterrows()], model)
        train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=8)
        train_loss = losses.TripletLoss(model=model)
        model.fit(
                train_objectives=[(train_dataloader, train_loss)],
                epochs=5,
                evaluation_steps=1,
                warmup_steps=1,
                )
        model.save(path = "./app/model")
    except FileNotFoundError as e:
        print(f"データセットが見つかりません。パスを確認してください: {e.filename}")
    except Exception as e:
        print(f"学習中にエラーが発生しました: {e}")

def get_unique_positives(df):
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
