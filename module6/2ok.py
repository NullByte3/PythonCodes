import random
tahkot = int(input("Montako tahkoa nopassa on? "))

def heita_noppaa():
    return random.randint(1, tahkot)

while True:
    noppa = heita_noppaa()
    print("Heitit:", noppa)
    if noppa == tahkot:
        print("Sait maksimin! Loppu!")
        break