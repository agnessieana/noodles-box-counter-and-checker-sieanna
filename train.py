from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="D:/Magang/BOX_CHECKING2/box_dataset_v3/data.yaml",
    epochs=100,
    imgsz=416,
    batch=4,
    workers=0,
    cache=False,
    device=0
)