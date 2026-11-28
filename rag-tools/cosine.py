import math

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    length_a = math.sqrt(sum(x * x for x in a))
    length_b = math.sqrt(sum(y * y for y in b))
    return dot / (length_a * length_b)

print(cosine([1, 2, 3], [1, 2, 3]))    # 1.0  - identical
print(cosine([1, 2, 3], [2, 4, 6]))    # 1.0  - same direction, longer arrow
print(cosine([1, 0, 0], [0, 1, 0]))    # 0.0  - completely different directions
