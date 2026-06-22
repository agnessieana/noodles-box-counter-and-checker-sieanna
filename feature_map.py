import cv2
import torch
import matplotlib.pyplot as plt
from ultralytics import YOLO


# ==========================
# LOAD MODEL
# ==========================

model = YOLO("D:/Magang/BOX_CHECKING2/runs/detect/train-3/weights/best.pt")

# ambil model pytorch YOLO
yolo_model = model.model


# ==========================
# FEATURE STORAGE
# ==========================

features = {}


def save_feature(name):
    def hook(module, input, output):
        features[name] = output.detach().cpu()

    return hook


# ==========================
# PILIH LAYER YOLOv8
# ==========================

# lihat struktur layer kalau mau ganti
for i, layer in enumerate(yolo_model.model):
    print(i, layer)


# layer backbone C2f (umumnya)
layer_number = 4

yolo_model.model[layer_number].register_forward_hook(
    save_feature("backbone_feature")
)


# ==========================
# LOAD IMAGE
# ==========================

img_path = "D:/Magang/BOX_CHECKING2/box_project/photo_asset/ng_1.png"

img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2RGB
)


# ==========================
# INFERENCE
# ==========================

results = model(
    img_rgb,
    conf=0.05,
    iou=0.7
)


# ==========================
# AMBIL FEATURE MAP
# ==========================

feature = features["backbone_feature"]

print(
    "Feature map shape:",
    feature.shape
)


# pilih channel pertama
feature_map = feature[0, 0]


# ==========================
# VISUALISASI
# ==========================

plt.figure(figsize=(15,5))


# --------------------------
# 1. INPUT IMAGE
# --------------------------

plt.subplot(1,3,1)

plt.imshow(img_rgb)

plt.title(
    "Input Image"
)

plt.axis("off")



# --------------------------
# 2. FEATURE MAP
# --------------------------

plt.subplot(1,3,2)

plt.imshow(
    feature_map,
    cmap="viridis"
)

plt.title(
    "YOLOv8 Backbone Feature Map"
)

plt.axis("off")



# --------------------------
# 3. DETECTION RESULT
# --------------------------

result_img = results[0].plot()


plt.subplot(1,3,3)

plt.imshow(
    result_img
)

plt.title(
    "Detection Output"
)

plt.axis("off")


plt.tight_layout()

plt.show()