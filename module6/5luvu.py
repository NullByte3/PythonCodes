kaikki_luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parilliset = []
def pari(luku):
    return luku % 2 == 0
parilliset = list(filter(pari, kaikki_luvut))
print("Kaikki luvut:", kaikki_luvut)
print("Parilliset luvut:", parilliset)