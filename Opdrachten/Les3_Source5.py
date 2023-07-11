# Ordering at Mac Donald's
eat_in = False
eat_out = False
aborted = False

print("Welkom bij de Mac Donald's")
question_1_str = input("Hier opeten of meenemen? [Opeten/Meenemen]: ")
question_1 = question_1_str.upper()
if question_1 == "OPETEN":
    # Eat in part
    print("Hier opeten")
    eat_in = True
elif question_1 == "MEENEMEN":
    # Take away part
    print("Meenemen")
    eat_out = True
else:
    aborted = True

if eat_in or eat_out:
    question_2_str = input("Burgers of drankjes? [Burgers/Drankjes]: ")
    question_2 = question_2_str.upper()
    if question_2 == "BURGERS":
        question_3_str = input("Burgers [Hamburger, Cheeseburger, Bic Mac, Quarter Pounder]: ")
        question_3 = question_3_str.upper()
        if question_3 == "HAMBURGER":
            print("Hamburger")
        elif question_3 == "CHEESEBURGER":
            print("Cheeseburger")
        elif question_3 == "BIC MAC":
            print("Big Mac")
        elif question_3 == "QUARTER POUNDER":
            print("Quarter Pounder")
        else:
            aborted = True
    elif question_2 == "DRANKJES":
        question_4_str = input("Drankjes [Warme/Koude]: ")
        question_4 = question_4_str.upper()
        if question_4 == "WARME":
            question_5_str = input("Warme drank: [Koffie, Cappucino, Chocolademelk]: ")
            question_5 = question_5_str.upper()
            if question_5 == "KOFFIE":
                print("Koffie")
            elif question_5 == "CAPPUCINO":
                print("Cappucino")
            elif question_5 == "CHOCOLADEMELK":
                print("Chocolademelk")
            else:
                aborted = True
        elif question_4 == "KOUDE":
            question_6_str = input("Koude drank: [Coca Cola, Cola Zero, 7-Up, Fanta, Fristi]: ")
            question_6 = question_6_str.upper()
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
            else:
                aborted = True
        else:
            aborted = True
    else:
        aborted = True

if aborted:
    print("Abort, unknown input.")
else:
    if eat_in:
        print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
    elif eat_out:
        print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")
