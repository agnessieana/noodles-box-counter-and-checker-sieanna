import cv2
from palleting import add_box_to_conveyor
import calibration

counted_ids = set()

last_positions = {}

class_count = {
    "front": 0,
    "side": 0
}

def process_counting(frame, box, track_id, class_name):

    h, w = frame.shape[:2]

    # ROI
    roi_x = int(w * 0.75)

    # Bounding box
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    # Titik tengah
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    # Visual titik tengah
    cv2.circle(
        frame,
        (center_x, center_y),
        5,
        (0, 0, 255),
        -1
    )

    # ROI line
    cv2.line(
        frame,
        (roi_x, 0),
        (roi_x, h),
        (0, 255, 255),
        2
    )

    # posisi sebelumnya
    prev_x = last_positions.get(track_id, center_x)

    # crossing kanan -> kiri
    if prev_x > roi_x and center_x <= roi_x:

        if track_id not in counted_ids:

            counted_ids.add(track_id)

            if class_name in class_count:

                class_count[class_name] += 1

                print(f"{class_name} counted")
                width = x2 - x1
                height = y2 - y1
                ratio = width / height

                print(
                    f"W={width}"
                    f"H={height}"
                    f"R={ratio:.2f}"
                )

                    # tambah buffer conveyor/cuma front
                if class_name == "front":
                    #ini simpen data
                    calibration.save_calibration_data(
                        track_id,
                        class_name,
                        width,
                        height,
                        ratio
                    )
                    
                    add_box_to_conveyor()

    # update posisi terakhir
    last_positions[track_id] = center_x

    return frame