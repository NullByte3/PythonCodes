numbers = []
while True:
    number = input("Anna luku: ")
    if number == "":
        break
    numbers.append(int(number))

print("Lukujen summa on " + str(sum(numbers)))
print("Lukujen suurin arvo on " + str(max(numbers)))
print("Lukujen pienin arvo on " + str(min(numbers)))