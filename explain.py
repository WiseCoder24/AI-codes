#!/usr/bin/env python3

import subprocess
import sys


def explain_log(log_file):
    with open(log_file, "r", encoding="utf-8") as f:
        log_text = f.read()

    prompt = f"""
You are an experienced Site Reliability Engineer.

Analyze the following log and answer in plain English.

Provide exactly two things:

1. A one- or two-sentence summary of what happened.
2. The most likely cause.

Ground your answer ONLY in the actual log text below.
Do not invent information that is not present in the log.

LOG:
---BEGIN LOG---
{log_text}
---END LOG---
"""

    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout.strip()


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <log_file>", file=sys.stderr)
        sys.exit(1)

    explanation = explain_log(sys.argv[1])
    print(explanation)


if __name__ == "__main__":
    main()
