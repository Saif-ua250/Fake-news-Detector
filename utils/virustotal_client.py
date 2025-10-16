"""
VirusTotal Client (v3) - URL scan and reputation lookup
"""

import os
import time
import requests
from typing import Dict, Any

API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "")
BASE = "https://www.virustotal.com/api/v3"


def is_configured() -> bool:
    return bool(API_KEY)


def _headers():
    return {"x-apikey": API_KEY}


def url_analyze(url: str) -> Dict[str, Any]:
    """
    Submit URL for analysis, then poll for result briefly.
    Returns: { ok, verdict, malicious, suspicious, harmless, undetected, raw }
    """
    if not is_configured():
        return {"ok": False, "error": "VIRUSTOTAL_API_KEY not configured"}

    try:
        r = requests.post(f"{BASE}/urls", headers=_headers(), data={"url": url}, timeout=20)
        r.raise_for_status()
        data = r.json()
        analysis_id = data.get("data", {}).get("id")
        if not analysis_id:
            return {"ok": False, "error": "No analysis id returned"}

        # Poll a few times (short)
        for _ in range(6):
            time.sleep(2)
            rr = requests.get(f"{BASE}/analyses/{analysis_id}", headers=_headers(), timeout=20)
            rr.raise_for_status()
            d2 = rr.json()
            status = d2.get("data", {}).get("attributes", {}).get("status")
            if status == "completed":
                stats = d2["data"]["attributes"].get("stats", {})
                malicious = stats.get("malicious", 0)
                suspicious = stats.get("suspicious", 0)
                harmless = stats.get("harmless", 0)
                undetected = stats.get("undetected", 0)

                # Simple verdict heuristic
                if malicious > 0:
                    verdict = "malicious"
                elif suspicious > 0:
                    verdict = "suspicious"
                else:
                    verdict = "clean"

                return {
                    "ok": True,
                    "verdict": verdict,
                    "malicious": malicious,
                    "suspicious": suspicious,
                    "harmless": harmless,
                    "undetected": undetected,
                    "raw": d2,
                }

        return {"ok": False, "error": "Timeout waiting for analysis"}
    except requests.HTTPError as e:
        return {"ok": False, "error": f"HTTP {e.response.status_code}", "details": e.response.text[:300]}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}
