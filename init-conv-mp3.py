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
    print("\t\t Youtube to MP3 Downloader")
    print("\t\t---------------------------\n")
    
    folder_path = input("Enter the destination folder path: ")
    
    if os.path.isdir(folder_path):
        urls = get_urls()
        count = 0
        for url in urls:
            try:
                yt = YouTube(url)
                print(f"Downloading Audio: {yt.title}")
                
                # Mengambil stream audio saja (kualitas terbaik)
                audio_stream = yt.streams.filter(only_audio=True).first()
                
                # Unduh file
                out_file = audio_stream.download(output_path=folder_path)
                
                # Ubah ekstensi dari .mp4/.m4a ke .mp3
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                
                count += 1
                print(f"[+] Berhasil mengunduh {count} MP3.\n")
            except Exception as e:
                print(f"[-] Gagal mengunduh {url}: {e}")
    else:
        print("Destination folder is Invalid...!")
