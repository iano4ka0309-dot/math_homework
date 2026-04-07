import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 1],
              [2, 1],
              [3, 1],
              [4, 1],
              [5, 1]])
y = np.array([22, 28, 37, 45, 53])
t = np.array([1, 2, 3, 4, 5])

result = np.linalg.lstsq(A, y, rcond=None)
k, b = result[0]
y6 = k * 6 + b
print(y6)
print(f"Рівняння тренду: y = {k:.2f}·t + {b:.2f}")

AT = A.T
ATA = AT @ A
ATy = AT @ y
det = np.linalg.det(ATA)
print(f"Визначник: {det:.2f}")

x = np.linalg.solve(ATA, ATy)
k2, b2 = x
print(f"\nПорівняння:")
print(f"lstsq:  k = {k:.2f}, b = {b:.2f}")
print(f"вручну: k = {k2:.2f}, b = {b2:.2f}")
print(f"Збігаються: {np.allclose([k, b], [k2, b2])}")

plt.scatter(t, y, color='red', label='Реальні дані')
plt.plot(t, k*t + b, color='blue', label='Лінія тренду')
plt.scatter(6, y6, color='green', label=f'Прогноз: {y6:.1f}%')
plt.xlabel('Година')
plt.ylabel('Навантаження CPU %')
plt.title('Тренд навантаження CPU')
plt.legend()
plt.show()

