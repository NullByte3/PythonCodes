import random

tietokoneen_luku = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku 1-10 väliltä: "))
    if arvaus < tietokoneen_luku:
        print("Liian pieni arvaus")
    elif arvaus > tietokoneen_luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break