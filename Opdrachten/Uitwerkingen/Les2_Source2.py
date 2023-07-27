import math

a = 0.87
b = 22.7
c = 5.03
term1 = b**2
term2 = 4 * a * c
term3 = term1 - term2
print(f'{term1}, {term2}, {term3}')
term4 = math.sqrt(term3)
term5 = -b + term4
term6 = 2 * a
y = term5 / term6

print(f'De waarde van y = {y} als a = {a}, b = {b} en c = {c}')

