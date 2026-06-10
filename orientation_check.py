HEIGHT_MIN = 129
WIDTH_MAX = 204

orientation_result = {}


def check_orientation(track_id, class_name, width, height):

    abnormal = False
    if class_name == "front":
        if height < HEIGHT_MIN:
            abnormal = True

        if width > WIDTH_MAX:
            abnormal = True

    print(
    f"ID={track_id}"
    f"W={width}"
    f"H={height}"
    f"Abnormal={abnormal}"
)

    orientation_result[track_id] = abnormal

    return abnormal
