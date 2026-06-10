import pandas as pd

#array buat simpen sementara
calibration_data = []

def save_calibration_data(
    track_id,
    class_name,
    width,
    height,
    ratio
):

    global calibration_data

    calibration_data.append({
        "track_id": track_id,
        "class": class_name,
        "width": width,
        "height": height,
        "ratio": ratio
    })

    print(f"Data saved: {ratio:.2f}")


def export_to_excel():

    global calibration_data

    if len(calibration_data) == 0:

        print("Tidak ada data")

        return

    df = pd.DataFrame(calibration_data)

    df.to_excel(
        "attempt.xlsx",
        index=False
    )

    print("Data berhasil disimpan")