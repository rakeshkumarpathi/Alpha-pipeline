def generate_dashboard(df, metrics):

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    fig, axes = plt.subplots(
        3,
        2,
        figsize=(18, 14)
    )

    fig.suptitle(
        "AlphaPipeline Analytics Dashboard",
        fontsize=20,
        fontweight="bold"
    )

    # ---------------- Close Price ----------------

    axes[0,0].plot(df["trade_date"], df["close_price"])
    axes[0,0].set_title("Closing Price")
    axes[0,0].grid(True)

    # ---------------- Moving Average ----------------

    axes[0,1].plot(df["trade_date"], df["close_price"], label="Close")
    axes[0,1].plot(df["trade_date"], df["ma_5"], label="MA 5")
    axes[0,1].plot(df["trade_date"], df["ma_20"], label="MA 20")
    axes[0,1].legend()
    axes[0,1].set_title("Moving Average")
    axes[0,1].grid(True)

    # ---------------- Volume ----------------

    axes[1,0].bar(
        df["trade_date"],
        df["volume"] / 1_000_000
    )

    axes[1,0].set_title("Volume (Millions)")
    axes[1,0].grid(True)

    # ---------------- Daily Return ----------------

    axes[1,1].plot(
        df["trade_date"],
        df["daily_return"] * 100
    )

    axes[1,1].axhline(0, linestyle="--")

    axes[1,1].set_title("Daily Return (%)")
    axes[1,1].grid(True)

    # ---------------- Volatility ----------------

    axes[2,0].plot(
        df["trade_date"],
        df["volatility"] * 100
    )

    axes[2,0].set_title("Volatility (%)")
    axes[2,0].grid(True)

    # ---------------- KPI Panel ----------------

    axes[2,1].axis("off")

    text = "\n".join(
        [f"{k}: {v}" for k, v in metrics.items()]
    )

    axes[2,1].text(
        0,
        1,
        text,
        fontsize=12,
        va="top"
    )

    # Format every x-axis

    for ax in axes.flat:

        if ax != axes[2,1]:

            ax.xaxis.set_major_formatter(
                mdates.DateFormatter("%b")
            )

            ax.xaxis.set_major_locator(
                mdates.MonthLocator()
            )

            ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()

    plt.savefig(
        "reports/dashboard.png",
        dpi=300
    )

    plt.show()