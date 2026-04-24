# from youtube_transcript_api import YouTubeTranscriptApi
# from urllib.parse import urlparse, parse_qs


# def extract_video_id(youtube_video_url: str) -> str | None:
#     """Extract the video ID from a YouTube URL robustly."""
#     parsed_url = urlparse(youtube_video_url)
#     video_id = parse_qs(parsed_url.query).get("v", [None])[0]
#     return video_id


# def extract_transcript(youtube_video_url: str) -> str | None:
#     """
#     Fetch and return the full transcript text from a YouTube video URL.
#     Returns None on failure and prints the error.
#     """
#     try:
#         video_id = extract_video_id(youtube_video_url)

#         if not video_id:
#             return None

#         ytt_api = YouTubeTranscriptApi()
#         transcript_data = ytt_api.fetch(video_id)

#         transcript = " ".join(i.text for i in transcript_data)
#         return transcript

#     except Exception as e:
#         raise RuntimeError(f"Could not fetch transcript: {str(e)}")



import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import urllib.request
import json
import re


# ── Video ID extractor ────────────────────────────────────────────────────────
def extract_video_id(youtube_video_url: str) -> str | None:
    """Extract the video ID from any YouTube URL format robustly."""
    if not youtube_video_url:
        return None

    # Handle youtu.be short links
    parsed = urlparse(youtube_video_url)
    if parsed.netloc in ("youtu.be",):
        return parsed.path.lstrip("/").split("?")[0] or None

    # Handle standard watch URLs
    video_id = parse_qs(parsed.query).get("v", [None])[0]
    if video_id:
        return video_id

    # Handle /embed/ and /v/ paths
    match = re.search(r"(?:/embed/|/v/)([A-Za-z0-9_-]{11})", parsed.path)
    if match:
        return match.group(1)

    return None


# ── Metadata fetch (no API key needed) ───────────────────────────────────────
def fetch_video_metadata(video_id: str) -> dict:
    """
    Fetch basic video metadata via YouTube's oembed endpoint (no API key).
    Returns dict with title, author_name, thumbnail_url.
    Falls back gracefully on error.
    """
    try:
        url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            return {
                "title": data.get("title", "Unknown Title"),
                "channel": data.get("author_name", "Unknown Channel"),
                "thumbnail": f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
                "thumbnail_fallback": f"https://img.youtube.com/vi/{video_id}/0.jpg",
            }
    except Exception:
        return {
            "title": "Unknown Title",
            "channel": "Unknown Channel",
            "thumbnail": f"https://img.youtube.com/vi/{video_id}/0.jpg",
            "thumbnail_fallback": f"https://img.youtube.com/vi/{video_id}/0.jpg",
        }


# ── Transcript extractor with caching ────────────────────────────────────────
@st.cache_data(ttl=3600, show_spinner=False)
def extract_transcript(youtube_video_url: str) -> str:
    """
    Fetch and return the full transcript text from a YouTube video URL.
    Results are cached for 1 hour to avoid redundant API calls.
    Raises RuntimeError with user-friendly messages on failure.
    """
    video_id = extract_video_id(youtube_video_url)

    if not video_id:
        raise RuntimeError(
            "❌ Invalid YouTube URL. Please paste a valid link like:\n"
            "`https://www.youtube.com/watch?v=...`"
        )

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_data = ytt_api.fetch(video_id)
        transcript = " ".join(i.text for i in transcript_data)

        if not transcript.strip():
            raise RuntimeError("⚠️ Transcript is empty. This video may have no spoken content.")

        return transcript

    except RuntimeError:
        raise

    except Exception as e:
        err = str(e).lower()
        if "no transcript" in err or "transcripts are disabled" in err:
            raise RuntimeError(
                "🚫 No transcript available for this video.\n"
                "This could be because:\n"
                "- The video has disabled captions\n"
                "- It's a private or age-restricted video\n"
                "- The video is too new and captions haven't been generated yet"
            )
        elif "video unavailable" in err:
            raise RuntimeError(
                "🚫 Video is unavailable. It may be private, deleted, or region-locked."
            )
        else:
            raise RuntimeError(f"⚠️ Could not fetch transcript: {str(e)}")