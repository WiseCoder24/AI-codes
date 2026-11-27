#!/usr/bin/env python3

import json
import os
import subprocess
from pathlib import Path

TICKETS_DIR = Path("/root/tickets")
OUTPUT_DIR = Path("/root/triaged")

VALID_CATEGORIES = {"billing", "technical", "account", "other"}
VALID_PRIORITIES = {"low", "medium", "high"}


def classify_ticket(ticket_text):
    prompt = f"""
You are a support ticket classification assistant.

Classify the following ticket using ONLY these allowed values:

category:
- billing
- technical
- account
- other

priority:
- low
- medium
- high

Return ONLY valid JSON in exactly this format:
{{
  "category": "billing",
  "priority": "high"
}}

Do not include markdown, explanations, or any additional text.

TICKET:
---BEGIN TICKET---
{ticket_text}
---END TICKET---
"""

    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        check=True,
    )

    output = result.stdout.strip()

    # Handle accidental markdown fences.
    if output.startswith("```"):
        lines = output.splitlines()
        output = "\n".join(
            line for line in lines
            if not line.strip().startswith("```")
        ).strip()

    data = json.loads(output)

    if data.get("category") not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category: {data.get('category')}")

    if data.get("priority") not in VALID_PRIORITIES:
        raise ValueError(f"Invalid priority: {data.get('priority')}")

    return {
        "category": data["category"],
        "priority": data["priority"],
    }


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    tickets = sorted(TICKETS_DIR.iterdir())

    for ticket in tickets:
        if not ticket.is_file():
            continue

        print(f"Processing {ticket.name}...")

        ticket_text = ticket.read_text(encoding="utf-8")
        result = classify_ticket(ticket_text)

        output_file = OUTPUT_DIR / f"{ticket.stem}.json"

        output_file.write_text(
            json.dumps(result, indent=2) + "\n",
            encoding="utf-8",
        )

        print(f"Saved: {output_file}")


if __name__ == "__main__":
    main()
