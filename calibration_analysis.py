import pandas as pd

df = pd.read_excel("calibration_data3.xlsx")

print("=== HEIGHT ===")
print(df["height"].describe())

print("\n=== WIDTH ===")
print(df["width"].describe())

print("\n=== RATIO ===")
print(df["ratio"].describe())

print("\n=== PERCENTILE ===")

print("Height P5 :", df["height"].quantile(0.05))   #129.0
print("Height P10 :", df["height"].quantile(0.10))  #130.5
                                            
print()

print("Ratio P10 :", df["ratio"].quantile(0.10))
print("Ratio P50 :", df["ratio"].quantile(0.50))
print("Ratio P90 :", df["ratio"].quantile(0.90))

print()

print("Width P90 :", df["width"].quantile(0.90))   #190.5
print("Width P95 :", df["width"].quantile(0.95))   #230.75