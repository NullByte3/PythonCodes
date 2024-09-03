def gallon_to_liter(gallons):
    return gallons * 3.785

while True:
    gallona = float(input("Anna gallona summa50 (- lopettaa): "))
    if gallona < 0:
        print("Ohjelma loppuu")
        break
    litra = gallon_to_liter(gallona)
    print(gallona, "gallonaa on", litra, "litraa")
