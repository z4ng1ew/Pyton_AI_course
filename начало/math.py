
# Числа Фибоначчи

# number = int(input("Порядковый номер числа Фибо: "))
#
# fib0 = 0
# fib1 = 1
#
# if number == 0:
#     print(fib0)
# elif number == 1:
#     print(fib1)
# else:
#     for i in range(2, number + 1):
#         fib_next = fib0 + fib1
#         fib0, fib1 = fib1, fib_next
#
#     print(fib1)


#Банк предлагает вкладчикам следующие условия вклада. Решение № 1

vklad_sum = float(input("Введите сумму вклада: "))
vklad_type = int(input("Выберите вид вклада (1, 2 или 3): "))

if vklad_type == 1:
    proc = 7
    srok = 1
elif vklad_type == 2:
    proc = 8
    srok = 3
elif vklad_type == 3:
    proc = 10
    srok = 5
else:
    print("Ошибка: такого вида вклада нет!")
    proc = 0
    srok = 0


if proc > 0:
    rate = proc / 100
    summa = vklad_sum * (1 + rate) ** srok
    pribyl = summa - vklad_sum

    print(f"Внеся {vklad_sum} руб. на срок {srok} лет под {proc}% годовых,")
    print(f"вы получите {round(summa, 2)} руб., прибыль составит {round(pribyl, 2)} руб.")
