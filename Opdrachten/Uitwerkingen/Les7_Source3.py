# Ordering at Mac Donald's
eat_in = False
aborted = False


SEPERATOR_CHARACTER = "/"
def get_valid_answer_text(valid_answers):
    valid_answers_text = ""
    if len(valid_answers) > 0:
        # Deze regel kan simpeler, maar dit is duidelijker
        # We kiezen er voor om de opties niet meteen in de "question" string mee te geven,
        # maar de lijst met mogelijke antwoorden mee af te drukken als we de vraag stellen
        valid_answers_text = " ["
        for answer in valid_answers:
            valid_answers_text = valid_answers_text + answer + SEPERATOR_CHARACTER
        valid_answers_text = valid_answers_text[:-1]  # Deze regel verwijdert de laatste /
        valid_answers_text = valid_answers_text + "]"
    return valid_answers_text


def ask_question(question, valid_answers=()):
    valid_answers_upper = []
    # Hier maken we alvast een lijst met de geldige antwoorden in hoofdletters
    for answer in valid_answers:
        valid_answers_upper.append(answer.upper())

    # We bouwen de vraag op uit de vraagtekst en de geldige antwoorden (als die er zijn)
    question_string = question
    question_string = question_string + get_valid_answer_text(valid_answers)
    question_string = question_string + ": "

    # We blijven de vraag stellen tot we een geldig antwoord hebben
    answer_str = ""
    while answer_str not in valid_answers_upper:
        answer_str = input(question_string)
        answer_str = answer_str.upper()

    # We geven het antwoord terug in hoofdletters
    return answer_str


def eat_in_choice():
    eat_in = False
    question_1 = ask_question("Hier opeten of meenemen", ["Opeten", "Meenemen"])
    if question_1 == "OPETEN":
        # Eat in part
        print("Hier opeten")
        eat_in = True
    elif question_1 == "MEENEMEN":
        # Take away part
        print("Meenemen")
        eat_in = False
    return eat_in


def get_burger_choice():
    question_3 = ask_question(
        "Burgers", ["Hamburger", "Cheeseburger", "Big Mac", "Quarter Pounder"]
    )
    if question_3 == "HAMBURGER":
        print("Hamburger")
    elif question_3 == "CHEESEBURGER":
        print("Cheeseburger")
    elif question_3 == "Big MAC":
        print("Big Mac")
    elif question_3 == "QUARTER POUNDER":
        print("Quarter Pounder")


def get_warm_drink_choice():
    question_5 = ask_question("Warme drank", ["Koffie", "Cappucino", "Chocolademelk"])
    if question_5 == "KOFFIE":
        print("Koffie")
    elif question_5 == "CAPPUCINO":
        print("Cappucino")
    elif question_5 == "CHOCOLADEMELK":
        print("Chocolademelk")


def get_cold_drink_choice():
    question_6 = ask_question(
        "Koude drank ", ["Coca Cola", "Cola Zero", "7-Up", "Fanta", "Fristi"]
    )
    if question_6 == "COCA COLA":
        print("Coca Cola")
    elif question_6 == "COLA ZERO":
        print("Cola Zero")
    elif question_6 == "7-UP":
        print("7-Up")
    elif question_6 == "FANTA":
        print("Fanta")
    elif question_6 == "FRISTI":
        print("Fristi")


print("Welkom bij de Mac Donald's")
eat_in = eat_in_choice()
if eat_in:
    food_answer = ask_question("Burgers of drankjes", ["Burgers", "Drankjes"])
    if food_answer == "BURGERS":
        get_burger_choice()
    elif food_answer == "DRANKJES":
        drink_choice = ask_question("Drankjes", ["Warme", "Koude"])
        if drink_choice == "WARME":
            get_warm_drink_choice()
        elif drink_choice == "KOUDE":
            get_cold_drink_choice()
if eat_in:
    print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
else:
    print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")
