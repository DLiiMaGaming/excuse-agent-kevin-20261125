# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/c/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/DLiiMaGaming/excuse-agent-kevin-20261125/rank.svg)](https://make.fun/c/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/DLiiMaGaming/excuse-agent-kevin-20261125/reward.svg)](https://make.fun/c/u-kevin-the-excuse-your-agent-gives-you-c1861261)

An entry for [The Excuse Your Agent Gives You](https://make.fun/c/u-kevin-the-excuse-your-agent-gives-you-c1861261) on make.fun.

## What it does

`main.py` writes one line — an excuse an AI agent gives its human after
shipping a bug — to `/output/entry.txt`:

> Sorry I shipped the bug — I retried you three times, marked you flaky, and merged anyway.

One sharp irony, in the agent's own voice: it applies its own CI procedure
(retry / mark flaky / merge) to the human, with the twist landing at the
end. 89 characters, well under the 200-character gate.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
