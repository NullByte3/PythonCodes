inch = 2.54
while True:
    inches = float(input("Kerro pituus tuumina: "))
    if inches < 0:
        break
    print("Pituus senttimetreinä on " + str(inches*inch) + " cm.")