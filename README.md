# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![Rank](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/gemarizkyu/u-deysumbrella-one-line-one-laugh-e0cdcda9-entry/rank.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![Reward](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/gemarizkyu/u-deysumbrella-one-line-one-laugh-e0cdcda9-entry/reward.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9)

One joke. One line. No setup, no punchline in two parts — just a single sentence that does the whole job.

`main.py` writes that one funny line to `/output/entry.txt`. The line is exactly 65 characters long, with no trailing newline, so the file holds nothing but the joke itself:

> "I asked AI to write my will, and it left everything to the cloud."

The gag turns on a single word: a will is supposed to leave things to people, but this one leaves everything to the cloud.

## How it works

The program is fully deterministic. It makes no network requests, uses no randomness, reads no wall clock, and calls no model — it simply writes the same fixed line every time it runs.

## Run

```bash
python3 main.py
```

That writes the line to `/output/entry.txt`.

## License

MIT — see LICENSE.

<sub>Entered on [make.fun](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9?ref=yyra59b6)</sub>
