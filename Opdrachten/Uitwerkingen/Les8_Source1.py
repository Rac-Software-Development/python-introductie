import time


def zeef_van_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    current_prime = 2
    while current_prime * current_prime <= limit:
        if is_prime[current_prime]:
            for multiple in range(
                current_prime * current_prime, limit + 1, current_prime
            ):
                is_prime[multiple] = False
        current_prime += 1

    prime_numbers = []
    for number in range(2, limit + 1):
        if is_prime[number]:
            prime_numbers.append(number)

    return prime_numbers


def zoek_priemgetallen(number):
    if number in faculteit_cache:
        print("Resultaat gevonden in cache")
        return faculteit_cache[number]
    else:
        print("Resultaat niet gevonden in cache")
        result = zeef_van_eratosthenes(number)
        faculteit_cache[number] = result
        return result


faculteit_cache = {}

while True:
    priemgetallen_doel = input(
        "Geef een getal om de priemgetallen van te bereken of geef [Enter] om te stoppen: "
    )
    if priemgetallen_doel == "":
        break

    timer = time.time()
    priemgetallen_resultaat = zoek_priemgetallen(int(priemgetallen_doel))
    result_time = time.time() - timer
    print(f"De priemgetallen onder de {priemgetallen_doel} zijn:")
    for priemgetal in priemgetallen_resultaat:
        print(priemgetal)
    print(f"Resultaat duurde: {result_time:.2f} seconden")

print("Tot ziens!")
