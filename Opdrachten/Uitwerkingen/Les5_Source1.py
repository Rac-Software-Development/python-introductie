numbers = list(range(1, 31))
for number in numbers:
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if result == "":
        result = number
    print(result)
