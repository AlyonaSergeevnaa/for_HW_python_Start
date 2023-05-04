# ; Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# ;  если разрешается сделать один разлом по прямой между дольками 
# ;  (то есть разломить шоколадку на два прямоугольника).

# ; *Пример:*

# ; 3 2 4 -> yes

# ; 3 2 1 -> no

width_m = int (input ('vvedite shirinu'))
length_n = int (input ('vvedite dlinu'))
amount = int (input ('vvedite kol-vo dolek'))

if (width_m * length_n > amount) and ((amount % length_n == 0) or (amount % width_m == 0)):
    print ('yes')
else: 
    print ('no')