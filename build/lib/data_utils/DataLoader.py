import requests
import pandas as pd
from io import BytesIO


class DataLoader():

  def __init__(self, url: str):
    r = requests.get(url)
    self.df = pd.read_csv(BytesIO(r.content), sep='\t')
  

  def print_summary(self):
    print('Shape:', self.df.shape)
    print('Printing head', self.df.head())
    print('Description of dataframe',self.df.describe())
    print('Info', self.df.info())