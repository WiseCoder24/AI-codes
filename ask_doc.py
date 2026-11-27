#!/usr/bin/env python3

import subprocess
import sys

RUNBOOK = "/root/runbook.md"


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} '<question>'", file=sys.stderr)
        sys.exit(1)

    question = sys.argv[1]

    with open(RUNBOOK, "r", encoding="utf-8") as f:
        runbook = f.read()

    prompt = f"""You are answering a question using only the runbook provided below.

Answer from the document only.
Do not use outside knowledge or make guesses.
If the runbook does not cover the question, say clearly that the document does not cover it.

RUNBOOK:
---BEGIN RUNBOOK---
{runbook}
---END RUNBOOK---

QUESTION:
{question}

Give a concise answer based only on the runbook.
"""

    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        check=True,
    )

    print(result.stdout.strip())


if __name__ == "__main__":
    main()
