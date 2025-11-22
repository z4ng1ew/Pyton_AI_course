# # print("Goodbye world" )
#
#
#
# name = input("Как тебя зовут?")
# program_lang = input("Какой язык уже знаешь?")
#
# print(f"Меня зовут1 {name}, я уже знаю {program_lang}")
#
# print("Меня зовут2", name, "я уже знаю", program_lang)
#
#
#









# number = int(input("Порядковый номер числа Фибоначчи: "))
#
# if number == 0:
#     print(0)
# elif number == 1:
#     print(1)
# else:
#     a, b = 0, 1
#     while b < number:
#         a, b = b, a + b











vklad = float(input("Введите сумму вклада: "))
srok = int(input("Введите срок вклада (в годах): "))
proc = float(input("Введите процентную ставку: "))

summa = vklad * (1 + proc / 100) ** srok
pribyl = summa - vklad

print(f"Внеся {vklad} руб. на срок {srok} лет под {proc}% годовых,")
print(f"вы получите {round(summa, 2)} руб., прибыль составит {round(pribyl, 2)} руб.")







# Более простой способ решения 2-ой задачи.  Решение № 2


vklad1 = float(input("Введите сумму вклада: "))
srok1 = int(input("Введите срок вклада (в годах): "))
proc1 = float(input("Введите процентную ставку: "))


summa1 = vklad1 + vklad1 * proc1 / 100 * srok1
pribyl1 = vklad1 * proc1 / 100 * srok1




print("Итоговая сумма: ", round(summa1, 2))
