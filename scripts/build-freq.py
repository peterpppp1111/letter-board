"""Add usage frequencies for Easy mode to words.json.

Easy boards are dealt by picking a word with probability proportional to how
often it is used in real English, so short common words come up most often.

Frequencies come from the `wordfreq` package (data under CC BY-SA 4.0):
    pip install wordfreq==3.1.1
    python3 scripts/build-freq.py

Run it from the repo root after scripts/build-words.js.
"""
import json

import wordfreq

MIN_FREQ = 1e-6  # about once per million words: skips words most players won't know
SCALE = 1e8      # store weights as integers

data = json.load(open("words.json"))
words = set()
for part in ("common", "all"):
    for length, s in data[part].items():
        if 3 <= int(length) <= 9:
            words.update(s.split())

freq = {}
for w in sorted(words):
    f = wordfreq.word_frequency(w, "en")
    if f >= MIN_FREQ:
        freq.setdefault(len(w), []).append(f"{w}:{round(f * SCALE)}")

data["freq"] = {str(k): " ".join(v) for k, v in sorted(freq.items())}
json.dump(data, open("words.json", "w"), separators=(",", ":"))
print("easy words:", sum(len(v) for v in freq.values()))
