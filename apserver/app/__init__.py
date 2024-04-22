from sentence_transformers import SentenceTransformer
import pandas as pd
from . import utils
import os

if not os.path.exists("./app/model"):
    model = utils.get_model()
else:
    model = SentenceTransformer.load("./app/model")
df = pd.read_csv('./app/qanda_transformer.csv')
