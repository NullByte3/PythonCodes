bullet = 13.3
nail = 32*bullet
bread = nail*20

bullets = float(input("monta sulla on luotia? "))
nails = float(input("monta sulla on nauloja? "))
breads = float(input("monta sulla on leipää? "))

total_weight_gram = bullets*bullet + nails*nail + breads*bread
total_kg = int(total_weight_gram/1000)

print("Yhteispaino on " + str(total_kg) +" kilo ja " + str(total_weight_gram - (total_kg*1000)) + " gramma.")