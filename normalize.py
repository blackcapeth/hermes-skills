#!/usr/bin/env python3
"""
normalize.py — Convert special characters in location names to ASCII equivalents.
Usage: python3 normalize.py "Köln"
Output: Cologne (or Koeln if no known alias)
"""

import sys
import unicodedata

# Known city aliases (special character name → preferred ASCII name)
CITY_ALIASES = {
    # German cities
    "köln": "Cologne",
    "münchen": "Munich",
    "düsseldorf": "Duesseldorf",
    "nürnberg": "Nuremberg",
    "würzburg": "Wuerzburg",
    "göttingen": "Goettingen",
    "tübingen": "Tuebingen",
    "lübeck": "Luebeck",
    "fürth": "Fuerth",
    # Turkish cities
    "İstanbul": "Istanbul",
    "i̇stanbul": "Istanbul",
    "istanbul": "Istanbul",
    "şişli": "Sisli",
    "üsküdar": "Uskudar",
    "kadıköy": "Kadikoy",
    "beşiktaş": "Besiktas",
    "çanakkale": "Canakkale",
    "ığdır": "Igdir",
    "muğla": "Mugla",
    "şanlıurfa": "Sanliurfa",
    "diyarbakır": "Diyarbakir",
    "kırıkkale": "Kirikkale",
}

CHAR_MAP = {
    'ä': 'ae', 'ö': 'oe', 'ü': 'ue',
    'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
    'ß': 'ss',
    'ğ': 'g', 'Ğ': 'G',
    'ş': 's', 'Ş': 'S',
    'ç': 'c', 'Ç': 'C',
    'ı': 'i', 'İ': 'I',
}

def normalize(name: str) -> str:
    # Check known aliases first
    alias = CITY_ALIASES.get(name.lower())
    if alias:
        return alias
    # Apply character map
    result = ""
    for ch in name:
        result += CHAR_MAP.get(ch, ch)
    # Final unicode normalization (strips remaining accents)
    result = unicodedata.normalize("NFD", result)
    result = "".join(c for c in result if unicodedata.category(c) != "Mn")
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 normalize.py <location>")
        sys.exit(1)
    location = " ".join(sys.argv[1:])
    print(normalize(location))
