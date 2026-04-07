import numpy as np

u = np.array([8, 2, 5])
vA = np.array([9, 1, 2])
vB = np.array([1, 9, 8])
vC = np.array([7, 2, 6])

def cosine_similarity(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

scores = {
    "Фільм A": cosine_similarity(u, vA),
    "Фільм B": cosine_similarity(u, vB),
    "Фільм C": cosine_similarity(u, vC)
}

for film, score in scores.items():
    print(film, round(score, 2))

best = max(scores, key=scores.get)
print("\nНайкращий фільм:", best, round(scores[best], 2))