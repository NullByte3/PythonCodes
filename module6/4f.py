def laske_summa(numerot):
    summa = 0
    for numero in numerot:
        summa = summa + numero
    return summa
numerot = [1, 2, 3, 4, 5]
summa = laske_summa(numerot)
print("Lista:", numerot)
print("Summa:", summa)
