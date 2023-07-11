user_input = ""
while user_input != ".":
    user_input = input("Please enter a number: ")
    if user_input == ".":
        print("Tot ziens")
    else:
        number_input = int(user_input)
        numbers = list(range(2, number_input - 1))
        is_prime = True
        for deler in numbers:
            if deler < number_input:
                if number_input % deler == 0:
                    is_prime = False
                    break
        if is_prime:
            print("Is prime: " + str(user_input))
        else:
            print("Not prime: " + str(user_input))