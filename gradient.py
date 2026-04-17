import numpy as np
from scipy.optimize import approx_fprime

def f(params):
    x, y = params
    return 0.5*x**2 + 0.3*y**2 + 0.2*x*y + 10*x + 5*y

point = np.array([10.0, 20.0])
epsilon = 1e-8 


grad_approx = approx_fprime(point, f, epsilon)

print(f"Чисельний градієнт: {grad_approx}")
print(f"Аналітичний градієнт: [24.0, 19.0]")



# Візуалізація функції та градієнта(додатково для кращого розуміння)
def f(x, y):
    return 0.5*x**2 + 0.3*y**2 + 0.2*x*y + 10*x + 5*y


x = np.linspace(0, 20, 100)
y = np.linspace(10, 30, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)


fig = plt.figure(figsize=(14, 6))


ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)
ax1.set_title('3D Поверхня функції f(x, y)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)


ax2 = fig.add_subplot(122)
contours = ax2.contour(X, Y, Z, 20, cmap='viridis')
ax2.clabel(contours, inline=True, fontsize=8)
ax2.plot(10, 20, 'ro')  # Позначаємо нашу точку
ax2.annotate('Точка (10, 20)', (10, 20), textcoords="offset points", xytext=(0,10), ha='center')
ax2.set_title('Контурний графік та градієнт')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.tight_layout()
plt.show()