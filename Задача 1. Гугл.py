# Задача 1. Гугл
# Программисты постоянно гуглят ошибки и ищут уже готовый код, который можно
# использовать для своей программы, чтобы не изобретать велосипед.Андрей
# поступил также и нашёл для своего проекта код, который должен находить минимальное
# и максимальное числа в списке.Вот этот код:

nums_list = []

N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
    num = int(input('Очередное число: '))

nums_list.append(num)
maximum = 0
minimum = -1

for i in nums_list:
    if maximum < i:
        maximum = i

    if minimum > i  :
        minimum = i
print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)

# Однако он столкнулся с проблемой. Если брать, к примеру, количество чисел 5, то
# на тестах - 1 - 2 - 3 - 4 - 5 и 1 2 3 4 5 программа выводит неверный результат.
#.
# Доработайте программу так, чтобы она выводила верный результат.Подсказка: для
# отладки используйте точки останова.
