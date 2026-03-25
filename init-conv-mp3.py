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
