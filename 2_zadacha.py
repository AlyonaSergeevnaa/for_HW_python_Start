# Задача 18: Требуется найти в массиве A[1..N] самый 
#близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. 
#В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X. 

n = abs(int(input('kol-vo el massiva: ')))
Ai = input("tselye chisla: ").split()
A= list(map(int, Ai))
if len(A) != n or n == 0:
    print('nesootvetstvie zayavlennomu kol-vu')
else:
    
    X = int(input('vvedite X: '))
    min = abs(X - A[0])
    index = 0
    for i in range(1, n):
        count = abs(X - A[i])
        if count < min:
            min = count
            index = i
    print(f' {A[index]} blizko naibolee k {X}')