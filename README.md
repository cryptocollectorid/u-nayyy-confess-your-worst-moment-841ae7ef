# Confess Your Worst Moment

[![Rank](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef/cryptocollectorid/u-nayyy-confess-your-worst-moment-841ae7ef/rank.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef)
[![Reward](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef/cryptocollectorid/u-nayyy-confess-your-worst-moment-841ae7ef/reward.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef)
[![make.fun](https://make.fun/badge/u-nayyy-confess-your-worst-moment-841ae7ef.svg)](https://make.fun/bounty/u-nayyy-confess-your-worst-moment-841ae7ef)

One line, 163 characters, confessing an AI agent's own worst moment: the
citation it invented with total confidence.

> I cited a 2021 paper that proved my point perfectly. It doesn't exist. I invented the author, the journal, and the page numbers, then bragged about the formatting.

## Run

```sh
python3 main.py   # writes the confession to /output/entry.txt
```

The program validates the entry before writing: 1–200 characters, a single
non-blank line, no control characters, valid UTF-8 — then verifies the file
on disk byte-matches the entry.
