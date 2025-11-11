from fastapi import APIRouter, Query, HTTPException
import yt_dlp
import os

router = APIRouter()

@router.get("/youtube_video_downloader", tags=["Downloader"])
def url_search(query: str = Query(..., description="Give the URL of the YouTube video")):
    try:
        if not os.path.exists("Downloads"):
            os.makedirs("Downloads")

        ydl_opts = {
            'format': 'best',
            'outtmpl': 'Downloads/%(title)s.%(ext)s',
            'noplaylist': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([query])
            return {"message": "Video downloaded successfully!"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/youtube_video_finder", tags=["Finder"])
def youtube_search(query: str = Query(..., description="Enter a title if you don't know a URL")):
    try:
        ydl_opts = {
            'skip_download': True,
            'quiet': True,
            'extract_flat': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_query = f"ytsearch5:{query}"
            info = ydl.extract_info(search_query)
            results = [
                {
                    'title': entry.get('title'),
                    'duration': entry.get('duration'),
                    'url': f"https://www.youtube.com/watch?v={entry.get('id')}",
                    'channel': entry.get('uploader')
                }
                for entry in info['entries']
            ]
            return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))