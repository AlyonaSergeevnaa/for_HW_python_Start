# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих cтроках записаны N целых чисел Ai.
# Последняя строка содержит число 



n = int(input('razmer spiska: '))
plan_n = input('elementy spiska: ').split()
arr = list(map(int, list_n))
x = int (input('vvedite х: '))
count = 0
for i in range(n):
    if arr[i] == x:
        count += 1
print(f' {x} v spiske {count} raz.')