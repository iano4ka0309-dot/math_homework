import numpy as np
from scipy.optimize import approx_fprime


def f(t):
    return 1000 * t * np.exp(-0.2 * t)

def f_prime_analytical(t):
    return 1000 * np.exp(-0.2 * t) * (1 - 0.2 * t)

hours_since_8am = np.array([2.0, 6.0, 10.0])
eps = 1e-8 

print(f"{'Час':<10} | {'Чисельна':<15} | {'Аналітична':<15} | {'Рішення IT'}")
print("-" * 75)

for t in hours_since_8am:
    
    numerical_grad = approx_fprime(np.array([t]), f, eps)[0]
    
    analytical_grad = f_prime_analytical(t)
       
    if numerical_grad > 100: 
        advice = "Додати сервери"
    elif numerical_grad < -100:
        advice = "Вимкнути сервери"
    else:
        advice = "Стабільно / Пік"

    time_str = f"{int(8+t):02d}:00"
    print(f"{time_str:<10} | {numerical_grad:<15.4f} | {analytical_grad:<15.4f} | {advice}")

