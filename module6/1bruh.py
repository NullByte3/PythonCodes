import random

def heita_noppaa():
    return random.randint(1, 6)

while True:
    noppa = heita_noppaa()
    print("Heitit:", noppa)
    if noppa == 6:
        print("Sait kuutosen! Loppu!")
        break