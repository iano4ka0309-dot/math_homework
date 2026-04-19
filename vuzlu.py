import math
import itertools

# 1. Дані
failure_probs = {"A": 0.02, "B": 0.05, "C": 0.03, "D": 0.04}

# 2. Робимо СЛОВНИК для роботи (замість списку)
# Тепер ми можемо писати work_probs["A"] і отримувати 0.98
work_probs = {node: 1 - p for node, p in failure_probs.items()}

# 3. Основні розрахунки
P_all_work = math.prod(work_probs.values())
P_one_failure = 1 - P_all_work
total_exactly_two = 0

# 4. Таблиця для пункту 3
print(f"{'Комбінація відмови':<25} | {'Ймовірність сценарію':<20}")
print("-" * 48)

nodes = failure_probs.keys()

for failed_nodes in itertools.combinations(nodes, 2):
    p_scenario = 1
    for node in nodes:
        if node in failed_nodes:
            p_scenario *= failure_probs[node]  # Вузол зламався
        else:
            # ТУТ СТАЛО ПРОСТІШЕ: просто беремо зі словника за ключем
            p_scenario *= work_probs[node]     # Вузол працює
    
    combo_str = ", ".join(failed_nodes)
    print(f"Вузли {combo_str:<18} | {p_scenario:.6%}")
    total_exactly_two += p_scenario

print("-" * 48)
print(f"1. Ймовірність (всі працюють):    {P_all_work:.4%}")
print(f"2. Ймовірність (хоча б 1 збій):   {P_one_failure:.4%}")
print(f"3. Ймовірність (рівно два):       {total_exactly_two:.4%}")