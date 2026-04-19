import numpy as np
from scipy.optimize import minimize_scalar, minimize, approx_fprime
from scipy.integrate import quad

def P(t):
    return 100 + 40*t - 4*t**2

for t in [2, 5, 8]:
    derivative = approx_fprime([t], P, 1e-6)[0]
    if derivative > 0.1:
        trend = "зростає ↑"
    elif derivative < -0.1:
        trend = "спадає ↓"
    else:
        trend = "пік! 🎯"
    print(f"t={t}: P'(t) = {derivative:.2f} → {trend}")

result = minimize_scalar(lambda t: -P(t), bounds=(0, 10), method='bounded')
t_star = result.x
print(f"Пікова продуктивність: t* = {t_star:.2f}")
print(f"P(t*) = {P(t_star):.2f}")


total, _= quad(P, 0, 10)
print(f"Загальний обсяг виробництва: {total:.2f} одиниць")

A = np.array([[2, 1],
              [1, 3]])
b = np.array([20, 25])
x0, y0 = np.linalg.solve(A, b)
print(f"x₀ = {x0:.2f}, y₀ = {y0:.2f}")

def C(vars):
    x, y = vars
    return x**2 + y**2 - 10*x - 8*y + 50

result = minimize(C, x0=[x0, y0], method='BFGS')
x_opt, y_opt = result.x
min_cost = result.fun
print(f"Оптимальні параметри: x* = {x_opt:.2f}, y* = {y_opt:.2f}")
print(f"Мінімальна вартість: {min_cost:.2f}")

all_prices = min_cost * total
print(f"Загальна вартість виробництва: {all_prices:.2f} грн")

