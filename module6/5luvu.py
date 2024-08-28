kaikki_luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parilliset = []
for luku in kaikki_luvut:
    if luku % 2 == 0:
        parilliset.append(luku)
print("Kaikki luvut:", kaikki_luvut)
print("Parilliset luvut:", parilliset)