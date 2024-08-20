length = float(input("Kerro pituus: "))
if length < 36:
    print("Laita se takaisin, tarvi viela " + str(36-length) + " cm.")
else:
    print("Joo, se on hyvä.")