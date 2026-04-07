from matplotlib_venn import venn3
import matplotlib.pyplot as plt

rock_fans = {101, 102, 103, 105, 107, 109, 110, 112, 115, 118}
pop_fans = {102, 104, 105, 106, 108, 110, 111, 113, 115, 117}
jazz_fans = {103, 105, 108, 110, 112, 114, 115, 116, 119, 120}
all_users = rock_fans | pop_fans | jazz_fans
print(f"Унікальних користувачів: {len(all_users)}")

all_three = rock_fans & pop_fans & jazz_fans
print(f"Меломани (всі 3 жанри): {all_three}")
print(f"Кількість: {len(all_three)}")

rock_fans_only = rock_fans - (pop_fans | jazz_fans)
print(f"Тільки рок: {rock_fans_only}")

two_genres = (rock_fans & pop_fans) | (rock_fans & jazz_fans) | (pop_fans & jazz_fans) - all_three
print(f"Два жанри: {two_genres}")
print(f"Кількість: {len(two_genres)}")


venn3([rock_fans, pop_fans, jazz_fans],
      set_labels=('Rock', 'Pop', 'Jazz'))
plt.title('Перетин аудиторій')
plt.show()


