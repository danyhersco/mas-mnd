import os
import requests

import pandas as pd
from dotenv import load_dotenv


load_dotenv()

av_key = os.getenv("ALPHA_VANTAGE_KEY")

def read_intraday_data(ticker: str, interval: int):
    url = (
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"
        f"&symbol={ticker}&interval={interval}min&apikey={av_key}"
    )
    r = requests.get(url)
    data = r.json()

    time_series = data[f"Time Series ({interval}min)"]
    df = pd.DataFrame(time_series)

    df = df.T
    df.columns = [col.split('. ', 1)[-1] for col in df.columns]
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    return df
