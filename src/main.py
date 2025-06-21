
from data_reader import read_intraday_data
from data_visualiser import make_candlestick


def main():
    ticker = "IBM"
    df = read_intraday_data(ticker, interval=15)
    make_candlestick(df, ticker)


if __name__ == "__main__":
    main()
