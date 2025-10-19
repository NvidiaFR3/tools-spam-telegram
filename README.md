<p align="center">
  <img src="[https://files.catbox.moe/9pchlz.jpg]" alt="Thumbnail" width="300"/>
</p>

# 🚀 Telegram Tools Spammer

## Fitur Utama

* **Banner Keren**: Tampilan terminal yang menarik dengan gradasi warna bertema *cyber*.
* **Multi-Target**: Kirim pesan ke banyak Chat ID sekaligus dalam satu sesi.
* **Kustomisasi Penuh**: Tentukan sendiri gambar, *caption* (teks), jumlah pengiriman, dan jeda waktu.
* **Delay Milidetik**: Kontrol jeda waktu antar pengiriman dalam satuan milidetik untuk presisi tinggi.
* **Lintas Platform**: Berjalan lancar di Windows, Linux, dan Termux.
* **Penanganan Error**: Dilengkapi penanganan error dasar untuk input yang salah atau file tidak ditemukan.

---

## Instalasi & Penggunaan (Khusus Termux)

Panduan ini akan memandu Anda langkah demi langkah, mulai dari persiapan Termux hingga menjalankan skrip.

#### **Langkah 1: Persiapan Awal Termux**

Buka aplikasi Termux Anda dan jalankan perintah-perintah berikut satu per satu untuk memastikan semuanya siap.

1.  **Perbarui Paket Termux**
    Perintah ini penting untuk memastikan semua paket di Termux adalah versi terbaru.
    ```bash
    pkg update && pkg upgrade -y
    ```

2.  **Instal Paket yang Dibutuhkan**
    Kita akan menginstal **Python** (untuk menjalankan skrip) dan **Git** (untuk mengunduh file dari GitHub).
    ```bash
    pkg install python git -y
    ```

3.  **Izinkan Akses ke Penyimpanan**
    Perintah ini akan meminta izin untuk mengakses penyimpanan internal ponsel Anda. **Pilih 'Izinkan'** saat notifikasi muncul. Ini sangat penting agar skrip bisa menemukan file foto yang akan Anda kirim.
    ```bash
    termux-setup-storage
    ```

---

#### **Langkah 2: Instalasi Skrip**

Sekarang kita akan mengunduh dan menyiapkan skripnya.

1.  **Clone Repositori dari GitHub**
    Ganti `[NAMA-PENGGUNA-ANDA]` dan `[NAMA-REPOSITORI-ANDA]` dengan URL repositori yang benar.
    ```bash
    git clone [https://github.com/](https://github.com/)[NAMA-PENGGUNA-ANDA]/[NAMA-REPOSITORI-ANDA].git
    ```

2.  **Masuk ke Direktori Proyek**
    Ganti `[NAMA-REPOSITORI-ANDA]` dengan nama folder yang baru saja diunduh.
    ```bash
    cd [NAMA-REPOSITORI-ANDA]
    ```

3.  **Instal Modul Python**
    Skrip ini membutuhkan modul `requests`. Perintah di bawah ini akan menginstalnya secara otomatis dari file `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

---

#### **Langkah 3: Cara Menggunakan**

Setelah semua instalasi selesai, Anda siap menjalankan skripnya.

1.  **Jalankan Skrip**
    Pastikan Anda masih berada di dalam direktori proyek, lalu jalankan perintah:
    ```bash
    python spamx.py
    ```

2.  **Isi Input yang Diminta**
    Skrip akan meminta beberapa informasi. Ikuti petunjuk di layar:
    * **Masukkan BOT TOKEN**: Token dari @BotFather.
    * **Masukkan Chat ID**: ID target (pribadi, grup, atau channel).
    * **Masukkan path foto**: Lokasi file Yang Ada Di Dalam Repository / folder kalian
        > **Contoh path di Termux:**
        > * Jika foto ada di folder Download: `storage/emulated/0/Download/namafoto.jpg`
        > * Jika foto ada di folder DCIM/Kamera: `storage/dcim/Camera/IMG_20251019.jpg`
    * **Masukkan caption/text**: Teks yang ingin dikirim bersama gambar.
    * **Kirim berapa kali?**: Jumlah pengulangan.
    * **Delay antar kirim (milidetik)**: Jeda waktu, contoh: `1000` untuk 1 detik.

---

## Support Developer

Jika Anda merasa *tools* ini bermanfaat, Anda bisa mendukung saya dengan berdonasi melalui QRIS di bawah ini. Dukungan Anda sangat berarti!

<p align="center">
  <img src="[https://files.catbox.moe/nu6ci1.jpg]" alt="Donasi QRIS" width="300"/>
</p>

Anda juga bisa berdonasi melalui:
* **Saweria**: `https://saweria.co/fr3newera`

---

## Disclaimer

> [!CAUTION]
> * **Gunakan dengan Bijak.** Penulis tidak bertanggung jawab atas penyalahgunaan *tools* ini.
> * Penyalahgunaan skrip ini untuk melakukan spamming terhadap pihak yang tidak berkepentingan dapat menyebabkan akun Telegram Anda diblokir.
> * Proyek ini dibuat murni untuk tujuan **edukasi**.

---

Tools Ini Dibuat Oleh **FR3NEWERA**
* **Telegram**: [@fr3newera](https://t.me/fr3newera)
