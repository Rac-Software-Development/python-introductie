# Dictionary

phone_numbers = {"The Simpsons": "636-555-3226",
                 "Vegas Vacation": "555-0100",
                 "Ghostbusters": "555-23678",
                 "Billy Madison": "555-0840",
                 "Swingers": "213-555-4679",
                 "Bruce Almighty": "555-0123",
                 "Seinfeld": "555-FILK",
                 "Arrested Development": "555-0113",
                 "Die Hard With a Vengeance": "555-0001",
                 "The A-Team": "555-6162"}

print(phone_numbers)
print()

# a]
print(f"Het telefoonnummer van Bruce Almighty is {phone_numbers['Bruce Almighty']}.")
print(phone_numbers)
print()

# b]
phone_numbers["Harry Potter"] = "605-475-6961"
print(phone_numbers)
print()

# c]
old_phone_number = phone_numbers["Ghostbusters"]
new_phone_number = "555-2368"
phone_numbers["Ghostbusters"] = new_phone_number
print(f"Het telefoonnummr {old_phone_number} van de Ghostbusters is gewijzigd naar {new_phone_number}.")
print(phone_numbers)
print()

# d]
phone_number = phone_numbers.pop("Seinfeld")
print(f"Telefoonnummer {phone_number} van Sienfeld is verwijderd.")
print(phone_numbers)
print()

# e]
number_of_phone_numbers = len(phone_numbers)
print(f"In de dictionary zitten {number_of_phone_numbers} telefoonnummers.")
print(phone_numbers)
print()
