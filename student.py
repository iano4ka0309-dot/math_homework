import numpy as np
from scipy.integrate import solve_ivp


# t - час, K - поточний рівень знань
def learning_rate(t, K):
    r = 0.15  # коефіцієнт швидкості
    M = 100   # макс. рівень знань
    dK_dt = r * (M - K)
    return dK_dt


t_span = (0, 30)  
K0_initial = [10] 


solution = solve_ivp(learning_rate, t_span, K0_initial, t_eval=np.linspace(0, 30, 100))

start_levels = [5, 10, 20]
target_knowledge = 90

print(f"{'Початковий рівень (%)':<25} | {'День досягнення 90%':<20}")
print("-" * 50)

for k_start in start_levels:
    
    res = solve_ivp(learning_rate, (0, 50), [k_start], rtol=1e-6)
    
    times = res.t
    knowledge = res.y[0]
    
    
    reached_indices = np.where(knowledge >= target_knowledge)[0]
    
    if len(reached_indices) > 0:
        day_reached = times[reached_indices[0]]
        print(f"{k_start:<25}% | {day_reached:<20.2f} днів")