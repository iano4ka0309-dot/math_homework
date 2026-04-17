from math import comb

total = 12  
good = 8
defective = 4

P_rule = (good/total) * ((good-1)/(total-1))  * ((good-2)/(total-2))
print(f"Правило множення: {P_rule:.4f}")

P_comb = comb(good, 3) / comb(total, 3)
print(f"Комбінаторний підхід: {P_comb:.4f}")

if P_rule == P_comb:
    print("Обидва підходи дають однакову ймовірність.")
else:
    print("Підходи дають різні ймовірності, що вказує на помилку в розрахунках.")


P_rule_2_good = 3 * (good/total * (good-1)/(total-1) * defective/(total-2))
print(f"Правило множення (рівно 2 справні): {P_rule_2_good:.4f}")


P_comb_2_good = (comb(good, 2) * comb(defective, 1)) / comb(total, 3)
print(f"Комбінаторний підхід (рівно 2 справні): {P_comb_2_good:.4f}")


if P_rule_2_good == P_comb_2_good:
    print("Обидва підходи дають однакову ймовірність.")
else:
    print("Є розбіжність у розрахунках.")


