import numpy as np
from scipy.optimize import approx_fprime

def f(t):
    return 1000 * t[0] * np.exp(-0.2 * t[0])


def f_prime_analytical(t):
    return 1000 * np.exp(-0.2 * t) * (1 - 0.2 * t)


t_points = [2.0, 6.0, 10.0]  
epsilon = 1e-6               

print(f"{'Час':<10} | {'t':<5} | {'Чисельна похідна':<20} | {'Аналітична похідна':<20}")
print("-" * 75)

for t_val in t_points:
   
    t_array = np.array([t_val], dtype=float)
    
    
    num_grad = approx_fprime(t_array, f, epsilon)[0]
    
  
    ana_grad = f_prime_analytical(t_val)
    
    
    real_time = f"{int(8 + t_val):02d}:00"
    
    print(f"{real_time:<10} | {t_val:<5} | {num_grad:<20.4f} | {ana_grad:<20.4f}")


t_star = 1 / 0.2
peak_time = f"{int(8 + t_star)}:00"

print("-" * 75)
print(f"Момент пікового навантаження (t*): {t_star} годин від початку (о {peak_time})")


