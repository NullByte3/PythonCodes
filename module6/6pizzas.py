import math
halkaisija1 = float(input("1. pizzan halkaisija: "))
hinta1 = float(input("1. pizzan hinta: "))
halkaisija2 = float(input("2. pizzan halkaisija: "))
hinta2 = float(input("2. pizzan hinta: "))

ala1 = math.pi * (halkaisija1/2)**2
ala2 = math.pi * (halkaisija2/2)**2

yksikkohinta1 = hinta1 / ala1
yksikkohinta2 = hinta2 / ala2

print("1. pizzan yksikköhinta:", yksikkohinta1, "e/cm^2")
print("2. pizzan yksikköhinta:", yksikkohinta2, "e/cm^2")

if yksikkohinta1 < yksikkohinta2:
    print("1. pizza on halvempi")
elif yksikkohinta2 < yksikkohinta1:
    print("2. pizza on halvempi")
else:
    print("Pizzat ovat samanhintaisia")