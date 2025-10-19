import requests
import time
import os

def banner():
    """
    Membersihkan layar dan menampilkan banner dengan warna gradasi.
    """
    os.system("cls" if os.name == "nt" else "clear")
    
    banner_text = r"""
 ########:'########:::'#######:::::::::::'##::::'##:'########::
 ##.....:: ##.... ##:'##.... ##::::::::::. ##::'##:: ##.... ##:
 ##::::::: ##:::: ##:..::::: ##:::::::::::. ##'##::: ##:::: ##:
 ######::: ########:::'#######::'#######:::. ###:::: ##:::: ##:
 ##...:::: ##.. ##::::...... ##:........::: ## ##::: ##:::: ##:
 ##::::::: ##::. ##::'##:::: ##::::::::::: ##:. ##:: ##:::: ##:
 ##::::::: ##:::. ##:. #######::::::::::: ##:::. ##: ########::
..::::::::..:::::..:::.......::::::::::::..:::::..::........:::
"""

    footer_text = """
🔥Terimakasih Telah Menggunakn Tools FR3NEWERA🔥
Copyright ©FR3NEWERA
Telegram: @fr3newera
"""
    start_rgb = (0, 150, 255)
    end_rgb = (0, 255, 100)
    
    lines = banner_text.splitlines()
    num_lines = len(lines)
    
    for i, line in enumerate(lines):
        ratio = i / (num_lines - 1) if num_lines > 1 else 0
        r = int(start_rgb[0] + ratio * (end_rgb[0] - start_rgb[0]))
        g = int(start_rgb[1] + ratio * (end_rgb[1] - start_rgb[1]))
        b = int(start_rgb[2] + ratio * (end_rgb[2] - start_rgb[2]))
        
        color_code = f"\033[38;2;{r};{g};{b}m"
        reset_code = "\033[0m"
        print(color_code + line + reset_code)
    final_color = f"\033[38;2;{end_rgb[0]};{end_rgb[1]};{end_rgb[2]}m"
    print(final_color + footer_text + reset_code)
    print("\n>>> Telegram Spammer By @fr3newera <<<\n")


def main():
    """
    Fungsi utama untuk menjalankan logika spammer.
    """
    banner()
    
    try:
        TOKEN = input("[?] Masukkan BOT TOKEN: ")
        chat_ids_raw = input("[?] Masukkan Chat ID: ")
        CHAT_IDS = [cid.strip() for cid in chat_ids_raw.split(",")]
        IMAGE_PATH = input("[?] Masukkan path foto (contoh: foto.png): ")
        CAPTION = input("[?] Masukkan caption/text: ")
        LOOP_COUNT = int(input("[?] Kirim berapa kali?: "))
        DELAY = int(input("[?] Delay antar kirim: "))

        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

        print("\n[+] Mulai ngirim...\n")
        for i in range(LOOP_COUNT):
            for chat_id in CHAT_IDS:
                try:
                    with open(IMAGE_PATH, "rb") as file:
                        files = {"photo": file}
                        data = {"chat_id": chat_id, "caption": CAPTION}
                        response = requests.post(url, files=files, data=data)
                        
                        if response.status_code == 200:
                            print(f"[{i+1}] Sukses kirim ke target {chat_id}.")
                        else:
                            print(f"[{i+1}] Gagal kirim ke {chat_id}. Response: {response.json()}")
                
                except FileNotFoundError:
                    print(f"[!] Error: File tidak ditemukan di path '{IMAGE_PATH}'")
                    return
                except Exception as e:
                    print(f"[!] Terjadi error saat mengirim ke {chat_id}: {e}")

            if i < LOOP_COUNT - 1:
                delay_in_seconds = DELAY / 1000
                print(f"\n--- Menunggu {delay_in_seconds} detik sebelum pengiriman berikutnya ---\n")
                time.sleep(delay_in_seconds)
        
        print("\n[+] Selesai.")

    except ValueError:
        print("\n[!] Input tidak valid. Pastikan jumlah kirim dan delay adalah angka.")
    except KeyboardInterrupt:
        print("\n[!] Program dihentikan oleh pengguna.")

if __name__ == "__main__":
    main()