import random

pisteiden_maara = int(input("Kuinka monta pistettä arvotaan? "))
pisteet_ympyrassa = 0
for i in range(pisteiden_maara):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        pisteet_ympyrassa = pisteet_ympyrassa + 1
pii_likiarvo = 4 * pisteet_ympyrassa / pisteiden_maara
print("Piin likiarvo on:", pii_likiarvo)
