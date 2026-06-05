import pandas as pd

df = pd.read_excel("calibration_data.xlsx")

median_ratio = df["ratio"].median()

min_ratio = df["ratio"].min()

max_ratio = df["ratio"].max()

print(f"Median : {median_ratio:.3f}")
lower_limit = df["ratio"].quantile(0.05)
upper_limit = df["ratio"].quantile(0.95)

""" print(f"Min    : {min_ratio:.3f}")
print(f"Max    : {max_ratio:.3f}") """