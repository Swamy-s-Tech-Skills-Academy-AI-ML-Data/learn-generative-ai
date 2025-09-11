# filename: extract_contact_info.py
r"""Extract contact details from free-form text.

Fields extracted:
- first_name
- company
- location
- email
- phone

Usage (PowerShell):
    py .\src\day2\extract_contact_info.py               # runs on built-in sample
    py .\src\day2\extract_contact_info.py .\path\to\file.txt
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple


EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\(?\d{3}\)?[\s\-.]?\d{3}[\s\-.]?\d{4}")


def _extract_first_name(text: str) -> Optional[str]:
    # Strategy 1: "My name is Amit Bahree" -> Amit
    m = re.search(r"\bmy name is\s+([A-Z][a-z]+)\b", text, flags=re.I)
    if m:
        return m.group(1)

    # Strategy 2: sign-offs like "Thanks, Amit" / "Regards Amit"
    m = re.search(
        r"\b(?:thanks|regards|best|sincerely)[,\s]+([A-Z][a-z]+)\b", text, flags=re.I)
    if m:
        return m.group(1)

    # Strategy 3: "I am Amit Bahree" / "I'm Amit ..."
    m = re.search(r"\b(?:i am|i'm)\s+([A-Z][a-z]+)\b", text, flags=re.I)
    if m:
        return m.group(1)

    return None


def _extract_company_and_location(text: str) -> Tuple[Optional[str], Optional[str]]:
    # Common phrasing: "calling from Acme Insurance, Seattle, WA."
    m = re.search(
        r"\bcalling from\s+([^\.,\n]+)(?:,\s*([^\.\n]+))?", text, flags=re.I)
    if m:
        company = m.group(1).strip()
        location = m.group(2).strip() if m.lastindex and m.group(2) else None
        return company or None, location or None

    # Fallback: capture a City, ST pattern anywhere as location
    loc_m = re.search(r"\b([A-Z][a-zA-Z .'-]+,\s*[A-Z]{2})\b", text)
    location = loc_m.group(1).strip() if loc_m else None
    return None, location


def _extract_email(text: str) -> Optional[str]:
    m = EMAIL_RE.search(text)
    return m.group(0) if m else None


def _extract_phone(text: str) -> Optional[str]:
    m = PHONE_RE.search(text)
    return m.group(0) if m else None


def extract_info(text: str) -> Dict[str, Optional[str]]:
    first_name = _extract_first_name(text)
    company, location = _extract_company_and_location(text)
    email = _extract_email(text)
    phone = _extract_phone(text)

    return {
        "first_name": first_name,
        "company": company,
        "location": location,
        "email": email,
        "phone": phone,
    }


SAMPLE_TEXT = (
    "Hi there. I'm Priya Sharma from Contoso Health, Austin, TX. "
    "I heard you're exploring our employee wellness packages. "
    "When you have a moment, please call me at 425-555-0139 so we can review options. "
    "I'm available Monday to Friday during normal business hours Central Time. "
    "You can also reach me by email at priya.sharma@contosohealth.com. "
    "Thanks, Priya."
)


def _load_text_from_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        path = Path(argv[1])
        if not path.exists():
            print(f"Input file not found: {path}", file=sys.stderr)
            return 2
        text = _load_text_from_file(path)
    else:
        text = SAMPLE_TEXT

    result = extract_info(text)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
