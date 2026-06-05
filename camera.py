import cv2
from ultralytics import YOLO
from counting import process_counting, class_count
import palleting
import calibration

model = YOLO("D:/Magang/BOX_CHECKING2/runs/detect/train-3/weights/best.pt").to("cuda")
cap = cv2.VideoCapture("D:/Magang/BOX_CHECKING2/box_project/video_asset/calibration_videos.mp4")

while True:
    ret, frame = cap.read() 

    if not ret:
        break

    # Deteksi dan track (dia kasih id)
    results = model.track(
        frame,
        conf=0.7,
        iou=0.4,
        persist=True)
    
    #frame hasil deteksi
    annotated_frame = results[0].plot(
        line_width=1,
        font_size=0.5
    )

    
#buat counting
    for r in results:

        boxes = r.boxes

        for box in boxes:

            # pastikan ada tracking ID
            if box.id is None:
                continue

            track_id = int(box.id[0])

            cls_id = int(box.cls[0])

            class_name = model.names[cls_id]
            class_name = class_name.lower()

            frame = process_counting(
                frame,
                box,
                track_id,
                class_name
            )

    # update palletizing
    palleting.process_robot_pick()


    # Ambil frame yang sudah ada bounding box
    annotated_frame = results[0].plot(
        line_width=1,   
        font_size=0.5   
    )

    #font buat count
    cv2.putText(
        annotated_frame,
        f"Front: {class_count['front']}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    #font palleting
    cv2.putText(
        annotated_frame,
        f"On conveyor: {palleting.current_on_con}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Current Layer: {palleting.current_layer}/15",
        (20, 180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"On Pallet: {palleting.current_on_pallet}/120",
        (20, 220),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
            (255, 0, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Layer Count: {palleting.layer_count}/8",
        (20, 260),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Pallet Count: {palleting.pallet_count}",
        (20, 300),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    # Tampilkan
    cv2.imshow("YOLO Detection", annotated_frame)

    # Tekan q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

calibration.export_to_excel()
cap.release()
cv2.destroyAllWindows()
