# =========================
# KONFIGURASI
# =========================

BOX_PER_LAYER = 15
LAYER_PER_PALLET = 8

ROBOT_PATTERN = [6, 6, 3]

AUTO_START_NEXT_PALLET = True


# =========================
# STATUS SISTEM
# =========================

# jumlah pallet penuh
pallet_count = 0

# jumlah layer selesai pada pallet aktif
layer_count = 0

# jumlah box tersedia di conveyor
current_on_con = 0

# jumlah box pada layer aktif
current_layer = 0

# jumlah box pada pallet aktif
current_on_pallet = 0

# index pola robot
pattern_index = 0

# status pallet
waiting_new_pallet = False


# =========================
# TAMBAH BOX KE BUFFER
# =========================

def add_box_to_conveyor():

    global current_on_con

    current_on_con += 1

    print(f"Buffer conveyor: {current_on_con}")


# =========================
# RESET PALLET
# =========================

def reset_current_pallet():

    global layer_count
    global current_layer
    global current_on_pallet
    global pattern_index
    global waiting_new_pallet

    layer_count = 0
    current_layer = 0
    current_on_pallet = 0
    pattern_index = 0

    waiting_new_pallet = False

    print("New pallet started")


# =========================
# ROBOT PICK
# =========================

def process_robot_pick():

    global current_on_con
    global current_layer
    global current_on_pallet
    global pattern_index
    global layer_count
    global pallet_count
    global waiting_new_pallet

    # kalau pallet penuh dan sedang menunggu pallet baru
    if waiting_new_pallet:
        return

    target_pick = ROBOT_PATTERN[pattern_index]

    # buffer belum cukup
    if current_on_con < target_pick:
        return

    # =========================
    # ROBOT PICK
    # =========================

    current_on_con -= target_pick

    current_layer += target_pick

    current_on_pallet += target_pick

    print(f"Robot picked {target_pick} box")

    # pindah ke batch berikutnya
    pattern_index += 1

    # =========================
    # LAYER SELESAI
    # =========================

    if current_layer >= BOX_PER_LAYER:

        layer_count += 1

        print(f"Layer {layer_count} selesai")

        current_layer = 0

        pattern_index = 0

    # =========================
    # PALLET PENUH
    # =========================

    if current_on_pallet >= BOX_PER_LAYER * LAYER_PER_PALLET:

        pallet_count += 1

        print(f"Pallet {pallet_count} penuh")

        # Prototype:
        # langsung mulai pallet berikutnya

        if AUTO_START_NEXT_PALLET:

            reset_current_pallet()

        # Future industrial mode:
        # tunggu operator / PLC

        else:

            waiting_new_pallet = True