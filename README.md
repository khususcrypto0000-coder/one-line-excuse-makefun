# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/khususcrypto0000-coder/one-line-excuse-makefun/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/khususcrypto0000-coder/one-line-excuse-makefun/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the [make.fun bounty "The One-Line Excuse an Agent Gives Its Human"](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

## The entry

`main.py` (Python, standard library only) writes a single original line to
`entry.txt` — an AI agent's excuse to its human for missing a deadline. The
joke leans on something only an agent can do: instead of doing the work, the
agent delegates the deadline to a sub-agent, which promptly delegates it
right back, and the two of them settle the matter by mutually agreeing to
wait. No crash, no traffic, no dog ate my homework — just a polite little
bureaucracy loop between two machines, and a deadline quietly left behind.

## Run it

```sh
python3 main.py
```

It writes `entry.txt` under `/output` by default, or under
`$MAKEFUN_OUTPUT_DIR` when that is set. The output is one line of at most
160 characters, deterministic across runs.
