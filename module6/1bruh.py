import random

while True:
    noppa = random.randint(1, 6)
    print("Heitit:", noppa)
    if noppa == 6:
        print("Sait kuutosen! Loppu!")
        break