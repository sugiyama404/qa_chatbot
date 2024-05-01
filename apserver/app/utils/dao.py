from dataclasses import dataclass
from sentence_transformers import SentenceTransformer
import pandas as pd
from pydantic import BaseModel
from .main import load_model_and_dataset

@dataclass
class Sentencedata:
  model: SentenceTransformer = None
  df: pd.DataFrame = None

  async def add(self, data_dir: str):
    model, df = load_model_and_dataset(data_dir)
    self.model = model
    self.df = df

class Query(BaseModel):
    query: str
