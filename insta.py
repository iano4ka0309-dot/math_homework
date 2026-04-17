import numpy as np
from scipy.integrate import quad

def f(t):
    return 500 * np.exp(-0.3 * t)

def F_analytical(t):
    # Первісна F(t) = (500 / -0.3) * e^(-0.3t)
    return -(500 / 0.3) * np.exp(-0.3 * t)


analytical_result = F_analytical(7) - F_analytical(0)

numerical_result, error = quad(f, 0, 7)

theoretical_max, error_inf = quad(f, 0, np.inf)

efficiency = (numerical_result / theoretical_max) * 100


print("-" * 50)
print(f"1. Аналітичний результат (7 днів): {analytical_result:.2f} осіб")
print(f"2. Чисельний результат (quad):      {numerical_result:.2f} осіб")
print(f"3. Теоретичний максимум (0 до ∞):   {theoretical_max:.2f} осіб")
print("-" * 50)
print(f"Ефективність першого тижня:        {efficiency:.2f}%")
print("-" * 50)


if efficiency > 80:
    print("Висновок: Перший тиждень є критично важливим, оскільки забезпечує")
    print("понад 80% усіх реєстрацій. Рекомендується основні ресурси")
    print("спрямувати на початок кампанії.")