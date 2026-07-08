def display_dashboard(metrics):
    print("\n")
    print("=" * 60)
    print("           AlphaPipeline Analytics Dashboard")
    print("=" * 60)

    for key, value in metrics.items():
        print(f"{key:<30}: {value}")

    print("=" * 60)