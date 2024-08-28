import random
noppien_maara = int(input("Monta noppaa haluat heittää? "))
summa = 0
for i in range(noppien_maara):
    heitto = random.randint(1, 6)
    summa += heitto
print(f"Summa on: {summa}")