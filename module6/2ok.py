import random
tahkot = int(input("Montako tahkoa nopassa on? "))
while True:
    noppa = random.randint(1, tahkot)
    print("Heitit:", noppa)
    if noppa == tahkot:
        print("Sait maksimin! Loppu!")
        break