#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.


a = int(input("1 chislo "))
b = int(input("2 chislo "))


def rec_sum(a, b):
    if a == 0:
        return b
    else:
        return rec_sum(a - 1, b + 1)


print(rec_sum(a, b))