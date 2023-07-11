numbers = list(range(1, 100))
for number in numbers:
    is_prime = True
    for deler in numbers:
        if number > deler > 1:
            if number % deler == 0:
                is_prime = False
                break
    if is_prime:
        print(number)
