import numpy as np
import pandas as pd

# Вхідні дані
ratings = np.array([1, 2, 3, 4, 5])
counts = np.array([120, 180, 320, 580, 800])
total_reviews = counts.sum()

# 1. Побудова PMF та CDF
pmf = counts / total_reviews
cdf = np.cumsum(pmf)

# Вивід таблиці
df_ratings = pd.DataFrame({
    'Оцінка': ratings,
    'PMF (P(X=x))': pmf,
    'CDF (F(x))': cdf
})
print("Таблиця розподілу:")
print(df_ratings.to_string(index=False))

# 2. Числові характеристики
expected_value = np.sum(ratings * pmf)
variance = np.sum((ratings**2) * pmf) - (expected_value**2)
std_dev = np.sqrt(variance)

print(f"\nМатематичне сподівання E[X]: {expected_value:.2f}")
print(f"Дисперсія Var(X): {variance:.2f}")
print(f"Стандартне відхилення σ: {std_dev:.2f}")

# 3. Ймовірності
prob_negative = cdf[1]  # P(X <= 2)
prob_high = 1 - cdf[2]  # P(X >= 4) = 1 - P(X <= 3)

print(f"Ймовірність негативної оцінки (1-2): {prob_negative:.3f}")
print(f"Ймовірність оцінки 4 або 5: {prob_high:.3f}")

# 4. Медіана
median_rating = ratings[np.where(cdf >= 0.5)[0][0]]
print(f"Медіана рейтингу: {median_rating}")

