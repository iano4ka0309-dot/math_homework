total = 500
db_only = 85
net_only = 60
both = 35

A = db_only + both
P_A = A / total
print(f"P(A) = {P_A * 100:.1f}%")

B = net_only + both
P_B = B / total
print(f"P(B) = {P_B * 100:.1f}%")

P_intersection = both / total          # P(A ∩ B) — перетин
P_union = P_A + P_B - P_intersection  # P(A ∪ B) — об'єднання
P_diff = db_only / total              # P(A \ B) — різниця

print(f"P(A ∩ B) = {P_intersection * 100:.1f}%")
print(f"P(A ∪ B) = {P_union * 100:.1f}%")
print(f"P(A \\ B) = {P_diff * 100:.1f}%")

