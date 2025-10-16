"""
Google Gemini (AI Studio) Client

Lightweight REST client for summarization and cross-check using Gemini models.
"""

import os
import requests
from typing import Dict, Any, Optional

API_KEY = os.getenv("GOOGLE_API_KEY", "")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
MODEL = os.getenv("GOOGLE_GEMINI_MODEL", "models/gemini-1.5-flash")


def is_configured() -> bool:
    return bool(API_KEY)


def _post(path: str, json: dict, timeout: int = 20) -> Dict[str, Any]:
    url = f"{BASE_URL}/{path}?key={API_KEY}"
    resp = requests.post(url, json=json, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def summarize_and_verify(text: str, max_chars: int = 4000) -> Dict[str, Any]:
    """
    Ask Gemini to summarize and judge if content seems misleading.
    Returns compact dict: { summary, verdict, reasons }
    """
    if not is_configured():
        return {"ok": False, "error": "GOOGLE_API_KEY not configured"}

    prompt = (
        "You are a concise fact literacy assistant.\n"
        "Given the following news-like content, provide: \n"
        "1) a 2-3 sentence neutral summary, \n"
        "2) a verdict in one word: Real, Mixed, or Fake (best-effort, non-definitive), \n"
        "3) 1-2 brief reasons.\n"
        "Be cautious and avoid absolute claims.\n\n"
        f"CONTENT:\n{text[:max_chars]}"
    )

    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        data = _post(f"{MODEL}:generateContent", body)
        # Parse text output
        text_out = ""
        try:
            text_out = data["candidates"][0]["content"]["parts"][0]["text"].strip()
        except Exception:
            pass

        return {
            "ok": True,
            "raw": data,
            "text": text_out,
        }
    except requests.HTTPError as e:
        return {"ok": False, "error": f"HTTP {e.response.status_code}", "details": e.response.text[:300]}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}
