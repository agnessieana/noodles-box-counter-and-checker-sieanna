import pandas as pd
import matplotlib.pyplot as plt

# =====================
# LOAD RESULTS
# =====================

df = pd.read_csv(
    r"D:/Magang/BOX_CHECKING2/runs/detect/train-3/results.csv"
)

print(df.columns)

# =====================
# METRIK TERAKHIR
# =====================

last = df.iloc[-1]

print("\n===== FINAL RESULT =====")

print(
    f"Precision : {last['metrics/precision(B)']:.4f}"
)

print(
    f"Recall    : {last['metrics/recall(B)']:.4f}"
)

print(
    f"mAP50     : {last['metrics/mAP50(B)']:.4f}"
)

print(
    f"mAP50-95  : {last['metrics/mAP50-95(B)']:.4f}"
)

# =====================
# PRECISION
# =====================

plt.figure(figsize=(8,5))

plt.plot(
    df["epoch"],
    df["metrics/precision(B)"]
)

plt.title("Precision")
plt.xlabel("Epoch")
plt.ylabel("Precision")

plt.grid()

plt.show()

# =====================
# RECALL
# =====================

plt.figure(figsize=(8,5))

plt.plot(
    df["epoch"],
    df["metrics/recall(B)"]
)

plt.title("Recall")
plt.xlabel("Epoch")
plt.ylabel("Recall")

plt.grid()

plt.show()

# =====================
# mAP50
# =====================

plt.figure(figsize=(8,5))

plt.plot(
    df["epoch"],
    df["metrics/mAP50(B)"]
)

plt.title("mAP50")
plt.xlabel("Epoch")
plt.ylabel("mAP50")

plt.grid()

plt.show()

# =====================
# mAP50-95
# =====================

plt.figure(figsize=(8,5))

plt.plot(
    df["epoch"],
    df["metrics/mAP50-95(B)"]
)

plt.title("mAP50-95")
plt.xlabel("Epoch")
plt.ylabel("mAP50-95")

plt.grid()

plt.show()

# =====================
# BOX LOSS
# =====================

plt.figure(figsize=(8,5))

plt.plot(
    df["epoch"],
    df["train/box_loss"],
    label="Train"
)

plt.plot(
    df["epoch"],
    df["val/box_loss"],
    label="Validation"
)

plt.title("Box Loss")

plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend()

plt.grid()

plt.show()

# =====================
# CLS LOSS
# =====================

plt.figure(figsize=(8,5))

plt.plot(
    df["epoch"],
    df["train/cls_loss"],
    label="Train"
)

plt.plot(
    df["epoch"],
    df["val/cls_loss"],
    label="Validation"
)

plt.title("Classification Loss")

plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend()

plt.grid()

plt.show()

# =====================
# DFL LOSS
# =====================

plt.figure(figsize=(8,5))

plt.plot(
    df["epoch"],
    df["train/dfl_loss"],
    label="Train"
)

plt.plot(
    df["epoch"],
    df["val/dfl_loss"],
    label="Validation"
)

plt.title("DFL Loss")

plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend()

plt.grid()

plt.show()