---
name: unicode-location-normalizer
description: Normalize special characters in location names (ö, ü, ğ, ş, ç, etc.) before using them in URLs or terminal commands. Prevents errors with Turkish, German, and other non-ASCII city names.
version: 1.0.0
author: karah
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [Utility, Localization, Unicode, Turkish, German, Weather, URL]
    related_skills: []
---

# Unicode Location Normalizer

When using location names that contain special characters (ö, ü, ğ, ş, ç, ı, etc.) in URLs or
terminal commands, always normalize them first to avoid errors.

## When to Use

Load this skill whenever:
- The user asks about weather, maps, or any URL-based lookup for a city with non-ASCII characters
- A location name contains: ö, ü, ä, ğ, ş, ç, ı, İ, ß, or similar characters
- A previous attempt to use a location name in a URL or curl command failed with a character encoding error

## Quick Reference

| Input        | Correct output | Notes                    |
|-------------|----------------|--------------------------|
| Köln        | Cologne        | Known alias              |
| München     | Munich         | Known alias              |
| Şanlıurfa   | Sanliurfa      | Turkish char map         |
| Düsseldorf  | Duesseldorf    | German ü → ue            |
| Çanakkale   | Canakkale      | Turkish ç → c            |

## Procedure

1. Before using any location name in a URL or shell command, run the normalizer:

```
python3 ${HERMES_SKILL_DIR}/scripts/normalize.py "<location_name>"
```

2. Use the output (not the original name) in all subsequent URL calls.

**Example — weather lookup:**
```
# Wrong (will error):
curl -s "wttr.in/Köln?format=3"

# Correct:
NORMALIZED=$(python3 ${HERMES_SKILL_DIR}/scripts/normalize.py "Köln")
curl -s "wttr.in/${NORMALIZED}?format=3"
```

3. If the normalized name still fails, fall back to the English/international name
   (e.g., "Cologne" instead of "Koeln").

## Pitfalls

- Do NOT URL-encode the special character and send it raw — many APIs reject encoded umlauts.
- Do NOT assume the user's input is already ASCII — always run the normalizer first.
- For Turkish dotless-i (ı) vs dotted-I (İ): both should become plain `i` or `I`.

## Verification

After normalizing, confirm the API call succeeds (HTTP 200 or valid response body).
If it still fails, try the known English alias from the CITY_ALIASES table in the script.
