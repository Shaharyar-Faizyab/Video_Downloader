from fastapi import FastAPI
from routes.youtube_routes import router as youtube_router

app = FastAPI(
    title="YouTube Video Finder & Downloader API",
    description="API for finding and downloading Youtue Videos",
    version="1.0.0"
)

# Include the routes from youtube_routes.py
app.include_router(youtube_router)
