#!/usr/bin/env python3

import os
import sys

from openai import OpenAI


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} '<question>'", file=sys.stderr)
        sys.exit(1)

    question = sys.argv[1]

    client = OpenAI(
        base_url=os.environ["OPENAI_BASE_URL"],
        api_key=os.environ["OPENAI_API_KEY"],
    )

    response = client.chat.completions.create(
        model="glm-5.2",
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
