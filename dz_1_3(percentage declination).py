i = input('Сейчас мы ловко просклоняем слово "процент"')
a = 'процент'
b = 'процента'
c = 'процентов'
exception = [11, 12, 13, 14]
for i in range(100):
    if i in exception:
        print(i, c)
    elif i % 10 == 1:
        print(i, a)
    elif 1 < i % 10 < 5:
        print(i, b)
    else:
        print(i, c)
