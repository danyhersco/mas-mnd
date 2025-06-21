import os

import plotly.graph_objects as go
import pandas as pd


def make_candlestick(df: pd.DataFrame, ticker: str):

    fig = go.Figure(data=[go.Candlestick(
        x=df.index.strftime('%Y-%m-%d %H:%M'), # type: ignore
        open=df['open'].astype(float),
        high=df['high'].astype(float),
        low=df['low'].astype(float),
        close=df['close'].astype(float),
    )])

    fig.update_layout(
        title=(
            f"{ticker} Candlestick Chart from {df.index[0].strftime("%Y-%m-%d %H:%M")} "
            f"to {df.index[-1].strftime("%Y-%m-%d %H:%M")}"
        ),
        xaxis_title='Time',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False,
        xaxis=dict(type='category')
    )

    os.makedirs("data", exist_ok=True)
    fig.write_image(f"data/{ticker}_candlestick.png", width=1920, height=1080, scale=2)
