# Letter Board

An English word game in the browser. The board shows a word length and a letter, and you type any real English word that fits.

## Modes

| Mode | Goal | Timer | Scoring |
|---|---|---|---|
| **Sprint** (`#sprint`) | Score as many points as you can | 60 seconds for the whole round | 1 point per letter. You can skip a board |
| **Survival** (`#survival`) | Keep going as long as you can | A time limit per word (set by difficulty), reset after each correct answer | 1 point per word. Running out of time ends the game |

## Difficulty

Each difficulty deals a board by picking one random word from its own word list and using that word's length and letter. This makes the boards follow that list's word distribution.

| Difficulty | Boards follow | Survival time per word |
|---|---|---|
| **Easy** | How often words are used in real English (about 18,000 known words, weighted by usage), so short words come up most | 25 s |
| **Advanced** | The everyday list (about 30,000 words, each equally likely). It starts short: questions 1–5 use up to 5 letters, 6–10 up to 6, 11–15 up to 7, then anything from 3 to 9 | 20 s |
| **Hard** | Every accepted word (about 72,000, rare ones included), so long words come up most | 15 s |

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
- **Question 21 onwards:** the letter goes in a **random position** (for example "E as the 4th letter"). The gold tile shows where.
- **Word length:** boards use lengths from 3 to 9 letters.
- **Any word counts:** answers are checked against the full dictionary, whatever the difficulty.
- **No repeats:** you can't use the same word twice in one game.
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
