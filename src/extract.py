import yfinance as yf

def fetch_stock(symbol):

    df = yf.download(
        symbol,
        period="6mo",
        auto_adjust=True
    )

    return df 