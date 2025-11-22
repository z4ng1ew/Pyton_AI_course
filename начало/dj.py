summa_vklada = float(input("Введите сумму вклада (в рублях): "))
tip_vklada = int(input("Выберите тип вклада (1, 2 или 3): "))


if tip_vklada == 1:
    procent = 7
    srok_let = 1
elif tip_vklada == 2:
    procent = 8
    srok_let = 3
elif tip_vklada == 3:
    procent = 10
    srok_let = 5
else:
    print("Ошибка: такого типа вклада не существует.")
    exit()


godovaya_stavka = procent / 100
itogovaya_summa = summa_vklada * (1 + godovaya_stavka) ** srok_let
pribyl = itogovaya_summa - summa_vklada

print(f"\nВы вложили {summa_vklada:.2f} ₽ под {procent}% годовых на {srok_let} лет.")
print(f"К концу срока на счёте будет: {itogovaya_summa:.2f} ₽")
print(f"Ваша прибыль составит: {pribyl:.2f} ₽")