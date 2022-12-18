# Реализуйте алгоритм перемешивания списка.

# import random
# N = int(input('Введите размер списка: '))
# prod_list = [i for i in range(N)]
# print(prod_list)
# random.shuffle(prod_list)
# print(prod_list)

import random
N = int(input('Введите размер списка: '))
prod_list = [i for i in range(N)]
print(prod_list)
print(random.sample(prod_list, N))

# Закомментированный вариант реализован через "shuffle". Всё работает. Для наглядности выводим список "до" и "после".