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
