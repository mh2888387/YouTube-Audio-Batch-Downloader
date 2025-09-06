
import csv
import os
import sys


from yt_dlp import YoutubeDL


def download_audio(url: str, fmt: str = "mp3", output_dir: str = "downloads"):

    os.makedirs(output_dir, exist_ok=True)
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": fmt,
            "preferredquality": "192" if fmt == "mp3" else "0",
        }],
        "quiet": False,
        "no_warnings": True,
    }

    for element in url:
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([element])
        except Exception as e:
            print(f"Error ignored: {e}")


if __name__ == "__main__":
    video_url = []
    with open('youtube_videos.csv', mode='r',encoding='utf-8') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
           video_url.append(lines['url'])


    format_choice = "mp3"

    download_audio(video_url, format_choice)
    print(f"Downloaded audio as {format_choice.upper()} in the ‘downloads’ folder.")
