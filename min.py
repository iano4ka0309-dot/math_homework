from scipy.optimize import minimize
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def f(vars):
    x, y = vars
    return x**2 + x*y + y**2 - 6*x - 9*y + 20

result = minimize(f, x0=[0, 0], method='BFGS')
optimal_x, optimal_y = result.x
optimal_value = result.fun

print(f"Оптимальні значення: x = {optimal_x:.2f}, y = {optimal_y:.2f}")
print(f"Значення функції в оптимумі: {optimal_value:.2f}")

start_points = [[0, 0], [10, 10], [-5, 15]]

print("\nСтійкість розв'язку:")
for point in start_points:
    result = minimize(f, x0=point, method='BFGS')
    print(f"Старт {point} → x={result.x[0]:.2f}, y={result.x[1]:.2f}, f={result.fun:.2f}")

print("\nМатриця Гессе:")
print("H = [[2, 1], [1, 2]]")
print("\nВласні значення:")
H = np.array([[2, 1], [1, 2]])
eigenvalues = np.linalg.eigvals(H)
print(f"λ₁ = {eigenvalues[0]:.2f}")
print(f"λ₂ = {eigenvalues[1]:.2f}")
print(f"Обидва > 0 → точка (1, 4) є мінімумом функції.")


