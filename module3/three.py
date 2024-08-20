ratio = float(input("Kerro sun hemoglobiiniarvon g/l: "))
gender = input("Kerro sukupuolesi (M/N): ")
if gender == "M":
    if ratio < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif ratio > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.");
elif gender == "N":
    if ratio < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif ratio > 176:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.");
else:
    print("Virheellinen sukupuoli.")