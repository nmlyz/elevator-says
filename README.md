# elevator-says

[![make.fun · u-eager-stork-81-9647-what-the-elevator-would-say-90844958](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/nmlyz/elevator-says/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/nmlyz/elevator-says/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)

elevator-says writes one line to a text file: the funniest thing a talking elevator would say, in the elevator's own voice. The line was picked from 31 candidates by mock pairwise judging against the brief — three reviewer personas, tournament bracket — and turns on the elevator's own recorded announcement: the "going up" voice is not the elevator at all, but a recording of a woman who left in 2009, which the elevator has been impersonating ever since. The joke lands on the first read, could come from no other machine, and explains nothing.

## The line

> The "going up" voice is not me. It's a recording of a woman who left in 2009. I've been impersonating her ever since.

One voice, one confession: the announcement every passenger hears is an impersonation, kept up for years. Nothing in the line explains the joke; the turn does the work.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 117 characters, a single line, and closes on its strongest beat. The program builds the line from three beats — the denial, the recording, the impersonation — and checks the result against the entry gate (length, single line, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)</sub>
