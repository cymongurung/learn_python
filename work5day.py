#create a program that converts Nepali currency to USD, Euro , Japanese


nepali_currency = int(input("Enter nepali currency amount:"))

rupees_to_usd = nepali_currency / 133
rupees_to_euro = nepali_currency / 1.195
rupees_to_yan = nepali_currency / 142


print(f"USD is $ {rupees_to_usd}")
print(f"EURO is E {rupees_to_euro}")
print(f"YAN is Y {rupees_to_yan}")

