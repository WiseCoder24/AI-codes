import math

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    length_a = math.sqrt(sum(x * x for x in a))
    length_b = math.sqrt(sum(y * y for y in b))
    return dot / (length_a * length_b)

print(cosine([1, 2, 3], [1, 2, 3]))    # 1.0  - identical
print(cosine([1, 2, 3], [2, 4, 6]))    # 1.0  - same direction, longer arrow
print(cosine([1, 0, 0], [0, 1, 0]))    # 0.0  - completely different directions


# Cosine example
import math
import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
)

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    length_a = math.sqrt(sum(x * x for x in a))
    length_b = math.sqrt(sum(y * y for y in b))
    return dot / (length_a * length_b)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[
        "I was charged twice for my invoice",
        "There is a billing error on my account",
    ],
)

vec_a = response.data[0].embedding
vec_b = response.data[1].embedding
print(round(cosine(vec_a, vec_b), 3))
