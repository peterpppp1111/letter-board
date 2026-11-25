# Letter Board

An English word game in the browser. The board shows a word length and a letter, and you type any real English word that fits.

## Modes

| Mode | Goal | Timer | Scoring |
|---|---|---|---|
| **Sprint** (`#sprint`) | Score as many points as you can | 60 seconds for the whole round | 1 point per letter. You can skip a board |
| **Survival** (`#survival`) | Keep going as long as you can | 15 seconds per word, reset after each correct answer | 1 point per word. Running out of time ends the game |

Both modes follow the same rules:

- **Questions 1–20:** the word must **start with** the given letter.
- **Question 21 onwards:** the letter goes in a **random position** (for example "E as the 4th letter"). The gold tile shows where.
- You can't use the same word twice in one game.
- **Word length:** choose 3–5, 4–7 or 6–9 letters.
- **Every board has an answer:** a board is only dealt when at least 4 everyday words fit it.
- **Best scores:** saved in your browser, separately for each mode and word length.

## Run it

It's a static page, but it loads `words.json` with `fetch`, so opening `index.html` straight from disk won't work. Serve the folder instead:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000/#sprint or http://localhost:8000/#survival.

To put it online, turn on **GitHub Pages** in the repository settings (Settings → Pages → deploy from the `main` branch, root folder).

## Dictionary

`words.json` comes from the SCOWL word lists, through the `wordlist-english` npm package; see `WORDLIST-LICENSE`. It has two parts:

- `common`: about 39,000 everyday words. These are used to deal boards and suggest answers.
- `all`: rarer words. These are accepted as answers but never dealt.

Together they cover about 105,000 words, grouped by length. Proper nouns and words with apostrophes are left out.

To rebuild the dictionary, run these from the repo root:

```bash
npm pack wordlist-english@1.2.1 && mkdir -p wle && tar -xzf wordlist-english-1.2.1.tgz -C wle
```

```bash
node scripts/build-words.js
```

The script overwrites `words.json` in the repo root.
