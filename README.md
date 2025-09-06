# YouTube Audio Batch Downloader

A simple Python utility that reads a list of YouTube video URLs from a CSV file and downloads each video’s audio as MP3 (or WAV) using **yt-dlp** and **FFmpeg**.

***

## Features

- Batch download from a CSV (`youtube_videos.csv`) of URLs under the `url` column  
- Download best-quality audio stream  
- Convert to MP3 (default) or WAV  
- Automatic creation of a `downloads/` directory  
- Ignores and logs individual download errors without stopping the batch  

***

## Prerequisites

- Python 3.7 or newer  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- [FFmpeg](https://ffmpeg.org) (must be installed and on your PATH, so that `ffmpeg` and `ffprobe` commands are available)  

***

## Installation

1. Clone or download this repository.  
2. (Optional) Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux  
   venv\Scripts\activate      # Windows  
   ```
3. Install Python dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

***

## Usage

1. Prepare a CSV file named `youtube_videos.csv` in the project root.  
   - The CSV **must** include a header row with a column named `url`.  
   - Example:
     ```csv
     url
     https://www.youtube.com/watch?v=VIDEO_ID_1
     https://www.youtube.com/watch?v=VIDEO_ID_2
     ```
2. Run the script:
   ```bash
   python main.py
   ```
3. All downloaded audio files will appear in the `downloads/` folder as `<video title>.mp3`.

***

## Customization

- **Change output format**  
  Edit the `format_choice` variable in `main.py`:
  ```python
  format_choice = "wav"  # or "mp3"
  ```
- **Adjust audio quality**  
  In the `ydl_opts` dictionary, modify `"preferredquality"`:
  ```python
  "preferredquality": "320"   # for 320 kbps MP3
  ```

***

## Error Handling

- If FFmpeg is not found, the script will raise a postprocessing error.  
  - Ensure FFmpeg is installed and on your system PATH, or set `"ffmpeg_location"` in `ydl_opts` to the correct folder path.  
- Any download or conversion errors for individual URLs are caught and printed; the batch continues with the next URL.

***

## requirements.txt

Dependencies are locked for reproducibility. To install:
```bash
pip install -r requirements.txt
```

***

## License

This project is released under the MIT License.
