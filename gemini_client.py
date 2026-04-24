# import os
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# MODEL = "gemini-2.5-flash-lite"


# def generate_summary(transcript_text: str, prompt: str) -> str:
#     """
#     Send the transcript + prompt to Gemini and return the summary text.
#     """
#     try:
#         response = client.models.generate_content(
#             model=MODEL,
#             contents=prompt + transcript_text
#         )
#         return response.text
#     except Exception as e:
#         raise RuntimeError(f"Gemini API error: {str(e)}")





import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

MODEL = "gemini-2.5-flash-lite"

# ── Lazy client init with key validation ──────────────────────────────────────
_client = None

def _get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError(
                "❌ GOOGLE_API_KEY not found.\n"
                "Please add it to your `.env` file:\n"
                "`GOOGLE_API_KEY=your_key_here`"
            )
        _client = genai.Client(api_key=api_key)
    return _client


def generate_summary(transcript_text: str, prompt: str) -> str:
    """
    Send the transcript + prompt to Gemini and return the summary text.
    Raises RuntimeError with user-friendly messages on failure.
    """
    if not transcript_text or not transcript_text.strip():
        raise RuntimeError("⚠️ Transcript is empty — nothing to summarize.")

    # Truncate very long transcripts to avoid token limits (~100k chars max)
    MAX_CHARS = 80_000
    if len(transcript_text) > MAX_CHARS:
        transcript_text = transcript_text[:MAX_CHARS] + "\n\n[Transcript truncated due to length]"

    try:
        client = _get_client()
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt + transcript_text
        )
        result = response.text
        if not result or not result.strip():
            raise RuntimeError("⚠️ The AI returned an empty response. Please try again.")
        return result

    except RuntimeError:
        raise

    except Exception as e:
        err = str(e).lower()
        if "quota" in err or "rate" in err:
            raise RuntimeError(
                "⏳ API rate limit reached. Please wait a moment and try again."
            )
        elif "api key" in err or "invalid" in err:
            raise RuntimeError(
                "🔑 Invalid API key. Please check your GOOGLE_API_KEY in the `.env` file."
            )
        else:
            raise RuntimeError(f"🤖 Gemini API error: {str(e)}")