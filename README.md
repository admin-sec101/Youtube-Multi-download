# YouTube Playlist Downloader (Python)

Skrip Python sederhana untuk mengunduh banyak video YouTube sekaligus menggunakan daftar URL yang disimpan dalam file teks. Skrip ini menggunakan library `pytubefix` untuk memastikan kompatibilitas terbaru dengan server YouTube.

## 🚀 Fitur
- Batch Download (Unduh massal dari daftar URL).
- Otomatis mengambil resolusi tertinggi (Progressive MP4).
- Kompatibel dengan Kali Linux, WSL (Windows Subsystem for Linux), dan Ubuntu.
- Output langsung ke folder Windows (via `/mnt/c/`).

## 🛠️ Persyaratan Sistem
- Python 3.10 atau versi terbaru.
- Akses internet.

## 📥 Instalasi (Kali Linux/WSL)

1. **Clone atau Masuk ke Direktori Proyek:**
   ```bash
   cd ~/YT/youtube-playlist-downloader
   
***Buat & Aktifkan Virtual Environment (Direkomendasikan)***

```bash
python3 -m venv venv
source venv/bin/activate
```

***Instal Library yang Dibutuhkan***

```bash
pip install pytubefix
```

***Buka playlist Youtube***

```https://www.youtube.com/playlist?list=XXXXXXXX```

  Pada halaman playlist youtube klik kanan -> inspect -> console /Tekan F12 > pilih tab Console
  ketik: allow pasting
  paste kode berikut:
  ```
var urls = ""; 
document.querySelectorAll('a#video-title').forEach(function(el) { 
    urls += el.href.split('&')[0] + '\n'; 
}); 
console.log(urls);
```
  <img width="610" height="422" alt="image" src="https://github.com/user-attachments/assets/a0cc80f0-ea57-4f88-b0b6-8f4065ef463d" />

  Copy semua Url yang mucul

  /------------------
  
  Terkadang YouTube menggunakan "Lazy Loading". Jika playlist Anda punya 100+ video, gunakan kode ini agar browser otomatis scroll ke bawah sebelum mengambil link:
  ```javascript
window.scrollTo(0, document.documentElement.scrollHeight);
// Tunggu 2 detik, lalu jalankan kode Anda:
var urls = ""; 
document.querySelectorAll('a#video-title').forEach(function(el) { 
    urls += el.href.split('&')[0] + '\n'; 
}); 
console.log(urls);
  ```

***Buka Linux/WSL***

Buat file daftar URL: 
```bash
sudo nano downloadUrls.txt
```
Paste semua URL dari console browser di halaman playlist youtube
Simpan (Ctrl+O, Enter) dan keluar (Ctrl+X)

buat file 
```bash
sudo nano init.py
```
Paste Berikut:
```python
import os
from pytubefix import YouTube

def get_urls():
    urls = []
    try:
        with open('downloadUrls.txt', 'r') as f:
            for line in f:
                url = line.strip()
                if url:
                    urls.append(url)
    except Exception as e:
        print(f"\n[-] Error: Gagal membaca downloadUrls.txt: {e}")
    return urls

if __name__ == "__main__":
    print("\t\t Youtube Playlist Downloader (Fixed)")
    print("\t\t------------------------------------\n")
    
    folder_path = input("Enter the destination folder path: ")
    
    if os.path.isdir(folder_path):
        urls = get_urls()
        count = 0
        for url in urls:
            try:
                yt = YouTube(url)
                print(f"Downloading: {yt.title}")
                # Mengambil resolusi tertinggi (progressive mp4)
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path=folder_path)
                count += 1
                print(f"[+] Berhasil mengunduh {count} video.\n")
            except Exception as e:
                print(f"[-] Gagal mengunduh {url}: {e}")
    else:
        print("Destination folder is Invalid...!")
```
Jalankan: 

```bash
python3 init.py
```

Masukkan folder tujuan saat diminta. Contoh (untuk Windows):

Enter the destination folder path: ```/mnt/c/Users/[NAMA-PC]/Downloads```

//------------------------------Mulai Medownload File Video Youtube--------------------------//

***Untuk Converter ke mp3***

```sudo nano init-Conv-mp3.py```

```bash
import os
from pytubefix import YouTube

def get_urls():
    urls = []
    try:
        if not os.path.exists('downloadUrls.txt'):
            print("\n[-] Error: File downloadUrls.txt tidak ditemukan!")
            return urls
        with open('downloadUrls.txt', 'r') as f:
            for line in f:
                url = line.strip()
                if url:
                    urls.append(url)
    except Exception as e:
        print(f"\n[-] Error: Gagal membaca file: {e}")
    return urls

if __name__ == "__main__":
    print("\t\t YouTube to MP3 Batch Downloader")
    print("\t\t--------------------------------\n")
    
    folder_path = input("Masukkan path folder tujuan (Windows): ")
    
    if os.path.isdir(folder_path):
        urls = get_urls()
        count = 0
        for url in urls:
            try:
                yt = YouTube(url)
                # Mengambil stream audio saja dengan bitrate tertinggi
                audio = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
                
                print(f"Downloading Audio: {yt.title}")
                downloaded_file = audio.download(output_path=folder_path)
                
                # Mengubah ekstensi file menjadi .mp3
                base, ext = os.path.splitext(downloaded_file)
                new_file = base + '.mp3'
                
                # Cek jika file mp3 sudah ada agar tidak error saat rename
                if os.path.exists(new_file):
                    os.remove(new_file)
                
                os.rename(downloaded_file, new_file)
                
                count += 1
                print(f"[+] Berhasil: {count}. {yt.title}.mp3\n")
            except Exception as e:
                print(f"[-] Gagal pada {url}: {e}")
        
        print(f"\n Selesai! {count} file MP3 tersimpan di {folder_path}")
    else:
        print("Folder tujuan tidak valid!")
```

Jalankan: 

```bash
python3 init.py
```

Masukkan folder tujuan saat diminta. Contoh (untuk Windows):

Enter the destination folder path: ```/mnt/c/Users/[NAMA-PC]/Downloads```

//------------------------------Mulai Medownload File mp3 Youtube--------------------------//

//----------------------

Jika muncul error HTTP 403, perbarui library dengan:
bash
pip install --upgrade pytubefix

//----------------------

