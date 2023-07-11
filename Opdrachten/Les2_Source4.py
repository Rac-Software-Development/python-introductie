# Information
t = 4
v = 179875474.8
c = 299_792_458

# Breakup the formula
term1 = v**2
term2 = c**2
term3 = term1 / term2
term4 = 1 - term3
term5 = v * term4
term6 = 1 / term5
delta = t * term6

# Display result
print(f'Vanaf een komeet gezien zit u {delta} uur op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0} minuten op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0 * 60.0} seconden op de tuinstoel.')
