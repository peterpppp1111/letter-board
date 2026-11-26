# Letter Board

## ▶ [Play now: peterpppp1111.github.io/letter-board](https://peterpppp1111.github.io/letter-board/)

Jump straight to a mode: [Sprint](https://peterpppp1111.github.io/letter-board/#sprint) · [Survival](https://peterpppp1111.github.io/letter-board/#survival)

An English word game in the browser. The board shows a word length and a letter, and you type any real English word that fits.

## Modes

| Mode | Goal | Timer | Scoring |
|---|---|---|---|
| **Sprint** (`#sprint`) | Score as many points as you can | 90 seconds for the whole round | 1 point per letter. Unlimited skips |
| **Survival** (`#survival`) | Keep going as long as you can | A new clock for every board, longer for longer words (see below) | 1 point per word. Running out of time ends the game |

## Difficulty

Each difficulty deals a board by picking one random word from its own word list and using that word's length and letter. This makes the boards follow that list's word distribution.

| Difficulty | Boards follow | Survival time per board |
|---|---|---|
| **Easy** | How often words are used in real English (about 18,000 known words, weighted by usage), so short words come up most | 12 + 3 × letters (21–39 s) |
| **Advanced** | The everyday list (about 30,000 words, each equally likely). It starts short: questions 1–5 use up to 5 letters, 6–10 up to 6, 11–15 up to 7, then anything from 3 to 9 | 6 + 2 × letters (12–24 s) |
| **Hard** | Every accepted word (about 72,000, rare ones included), so long words come up most | 1 + 2 × letters, at least 10 s (10–19 s) |

On two-letter boards (question 21 onwards), Survival adds 3 more seconds. The clock pauses briefly while a correct answer is shown.

Survival seconds by word length (one-letter boards):

| Length | Easy | Advanced | Hard |
|---|---:|---:|---:|
| 3 | 21 | 12 | 10 |
| 4 | 24 | 14 | 10 |
| 5 | 27 | 16 | 11 |
| 6 | 30 | 18 | 13 |
| 7 | 33 | 20 | 15 |
| 8 | 36 | 22 | 17 |
| 9 | 39 | 24 | 19 |

Share of boards by word length, after the first questions:

| Length | Easy | Advanced | Hard |
|---|---:|---:|---:|
| 3 | 30% | 1.6% | 1.1% |
| 4 | 25% | 6.2% | 4.4% |
| 5 | 15% | 11.5% | 9.0% |
| 6 | 11% | 17.7% | 15.1% |
| 7 | 9% | 22.5% | 21.7% |
| 8 | 6% | 22.0% | 24.6% |
| 9 | 4% | 18.5% | 24.0% |

## Rules for every mode and difficulty

- **Questions 1–20:** the word must **start with** the given letter.
- **Question 21 onwards:** you get **two letters**: the first letter, plus a second letter at a random position, for example "starts with S and has E as the 4th letter" (SHEETED, SPRAYED). Both letters come from one real word, and the gold tiles show where they go.
- **Word length:** boards use lengths from 3 to 9 letters.
- **Any word counts:** answers are checked against the full dictionary, whatever the difficulty.
- **No repeats:** you can't use the same word twice in one game.
- **Skips:** Sprint has unlimited skips. In Survival, every 10 correct answers (10, 20, 30…) earn one skip, and unused skips carry over. The green energy bar beside the letters fills one cell per correct answer and shows how many are left until the next skip. In both modes, press **Skip** (or Esc), or press **Enter twice** with the box empty. In Survival, the next board starts with its own full time.
- **Every board has an answer:** a board is only dealt when at least 4 words in that difficulty's list fit it.
- **Best scores:** saved in your browser, separately for each mode and difficulty.

## Run it

It's a static page, but it loads `words.json` with `fetch`, so opening `index.html` straight from disk won't work. Serve the folder instead:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000/#sprint or http://localhost:8000/#survival.

To put it online, turn on **GitHub Pages** in the repository settings (Settings → Pages → deploy from the `main` branch, root folder).

## Dictionary

`words.json` has three parts, each grouped by length:

- `common`: about 39,000 everyday words from the SCOWL lists (through the `wordlist-english` npm package; see `WORDLIST-LICENSE`).
- `all`: rarer SCOWL words. They're accepted as answers and used for Hard boards.
- `freq`: about 18,000 words with how often each is used in English, from the [wordfreq](https://github.com/rspeer/wordfreq) package (data under CC BY-SA 4.0). They're used for Easy boards and hints.

Proper nouns and words with apostrophes are left out.

To rebuild it, run these from the repo root:

```bash
npm pack wordlist-english@1.2.1 && mkdir -p wle && tar -xzf wordlist-english-1.2.1.tgz -C wle
```

```bash
node scripts/build-words.js
```

```bash
pip install wordfreq==3.1.1 && python3 scripts/build-freq.py
```

`build-words.js` rewrites `words.json` without the `freq` part, so always run `build-freq.py` after it.
