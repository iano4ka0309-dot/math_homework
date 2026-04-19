from scipy.optimize import linprog
C = [-500, -800]
A = [[2,4], [3,2]]
b = [120, 90]

x_bounds = (0, None)
y_bounds = (0, None)
result = linprog(C, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
optimal_x, optimal_y = result.x
optimal_profit = -result.fun
wood_used = 2*optimal_x + 4*optimal_y
time_used = 3*optimal_x + 2*optimal_y

print(f"Оптимальна кількість товару A: {optimal_x:.2f}")
print(f"Оптимальна кількість товару B: {optimal_y:.2f}")
print(f"Максимальний прибуток: {optimal_profit:.2f}")

print(f"\nВисновки:")
if 120 - wood_used < 0.01:
    print("Деревина використана повністю ✅")
else:
    print(f"Деревина має залишок: {120 - wood_used:.2f} м²")

if 90 - time_used < 0.01:
    print("Робочий час використаний повністю ✅")
else:
    print(f"Робочий час має залишок: {90 - time_used:.2f} год")