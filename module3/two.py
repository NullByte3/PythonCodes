boat = input("Kerro veneen tyyppi: ")

if boat == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif boat == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif boat == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif boat == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")