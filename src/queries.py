QUERIES = {

    "Latest 5 Trading Days": """
        SELECT *
        FROM stock_features
        ORDER BY trade_date DESC
        LIMIT 5;
    """,

    "Highest Closing Price": """
        SELECT trade_date, close_price
        FROM stock_features
        ORDER BY close_price DESC
        LIMIT 1;
    """,

    "Lowest Closing Price": """
        SELECT trade_date, close_price
        FROM stock_features
        ORDER BY close_price ASC
        LIMIT 1;
    """,

    "Highest Trading Volume": """
        SELECT trade_date, volume
        FROM stock_features
        ORDER BY volume DESC
        LIMIT 1;
    """,

    "Highest Daily Return": """
        SELECT trade_date, daily_return
        FROM stock_features
        WHERE daily_return IS NOT NULL
        ORDER BY daily_return DESC
        LIMIT 1;
    """,

    "Highest Volatility": """
        SELECT trade_date, volatility
        FROM stock_features
        WHERE volatility IS NOT NULL
        ORDER BY volatility DESC
        LIMIT 1;
    """
}