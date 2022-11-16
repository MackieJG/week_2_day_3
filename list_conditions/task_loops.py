ages = [5, 15, 64, 27, 84, 26]
odd_ages = [age for age in ages if age % 2 != 0]
print(odd_ages)


chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
long_names = [chicken for chicken in chicken_names if len(chicken) > 10]
print(long_names)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
found_h = [chicken for chicken in chicken_names if chicken[0] == "H"]
print(found_h)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
starting_letter = [word[0].lower() for word in words]
print(starting_letter)

