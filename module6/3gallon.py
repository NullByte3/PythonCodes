while True:
    gallona = float(input("Anna gallona summa50 (- lopettaa): "))
    if gallona < 0:
        print("Ohjelma loppuu")
        break
    litra = gallona * 3.785
    print(gallona, "gallonaa on", litra, "litraa")
