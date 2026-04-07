from math import comb
backend = comb(8, 2)
print(f"Кількість способів для backend: {backend}")
frondend = comb(6, 2)
print(f"Кількість способів для frondend: {frondend}")
ui_ux = comb(4, 1)
print(f"Кількість способів для ui_ux: {ui_ux}")
total = backend * frondend * ui_ux
print(f"Загальна кількість способів вибору команди: {total}")



