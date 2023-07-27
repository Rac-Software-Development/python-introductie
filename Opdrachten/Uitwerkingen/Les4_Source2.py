# Tuple
computer_suppliers = ("Apple",
                      "Asus",
                      "Dell",
                      "Lenovo",
                      "Acer",
                      "Samsung",
                      "MSI",
                      "Hewlett-Packard (HP)",
                      "Toshiba",
                      "Microsoft",
                      "Chuwi",
                      "Sony")

print(computer_suppliers)
print()

# a]
number_of_computer_suppliers = len(computer_suppliers)
print(f"De tuple bevat {number_of_computer_suppliers} computer leveranciers.")

print(computer_suppliers)
print()

# b]
computer_supplier = computer_suppliers[7]
characters_in_name = len(computer_supplier)
print(f"De naam van {computer_supplier} bestaat uit {characters_in_name} karakters.")
print()

# c]
index_of_computer_supplier = computer_suppliers.index("Samsung")
print(f"De index van computer leverancier {computer_suppliers[index_of_computer_supplier]} is {index_of_computer_supplier}.")
print()

