import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import PySimpleGUI as sg
from tqdm import tqdm

# ===== BƯỚC 1: MỞ TRÌNH DUYỆT ẨN DANH VÀ ĐĂNG NHẬP =====
def login_anonymous():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Mở ở chế độ ẩn danh
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://trangwebcuaban.com/dangnhap")  # Thay URL bằng trang thật

    # Giả lập đăng nhập (ví dụ)
    time.sleep(2)
    print("🔒 Đăng nhập thành công ở chế độ ẩn danh.")
    return driver

# ===== BƯỚC 2: KIỂM TRA SỐ DƯ TÀI KHOẢN =====
def check_balance():
    # Giả lập số dư
    balance = 1_500_000
    if balance >= 1_000_000:
        print(f"💰 Số dư hiện tại: {balance}")
        return True
    else:
        print("❌ Không đủ số dư để chơi.")
        return False

# ===== BƯỚC 3: MÔ PHỎNG LOADING 5 PHÚT =====
def simulate_loading():
    print("⌛ Đang tải... (5 phút)")
    for _ in tqdm(range(100), desc="Loading", ncols=100):
        time.sleep(3)  # Tổng cộng: 100 * 3s = 5 phút

# ===== BƯỚC 4: GIAO DIỆN GAME TÀI XỈU =====
def launch_game_ui():
    sg.theme("DarkBlue")

    layout = [
        [sg.Text("🎲 Game Tài Xỉu", font=("Helvetica", 16))],
        [sg.Text("Chọn cược:"), sg.Combo(["Tài", "Xỉu"], key="BET")],
        [sg.Text("Số tiền cược:"), sg.Input(key="AMOUNT")],
        [sg.Button("Quay"), sg.Button("Thoát")],
        [sg.Output(size=(50, 10))]
    ]

    window = sg.Window("Game Tài Xỉu", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Thoát"):
            break
        elif event == "Quay":
            bet = values["BET"]
            try:
                amount = int(values["AMOUNT"])
            except:
                print("⚠️ Nhập số tiền hợp lệ.")
                continue
            result = roll_dice()
            win = (result > 10 and bet == "Tài") or (result <= 10 and bet == "Xỉu")
            print(f"🎲 Kết quả: {result} - Bạn {'THẮNG' if win else 'THUA'}!")

    window.close()

# ===== HÀM QUAY XÚC XẮC =====
import random
def roll_dice():
    dice = [random.randint(1, 6) for _ in range(3)]
    return sum(dice)

# ======= CHƯƠNG TRÌNH CHÍNH =======
if __name__ == "__main__":
    driver = login_anonymous()
    if check_balance():
        simulate_loading()
        launch_game_ui()
    else:
        print("Không đủ tiền để bắt đầu game.")
    driver.quit()
