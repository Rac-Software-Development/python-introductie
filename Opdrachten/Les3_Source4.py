# Shopping Cart
print("Shopping Cart")
question_1_str = input("Payment method? [Online/Offline]: ")
question_1 = question_1_str.upper()
if question_1 == "ONLINE":
    # Online part
    print("Online, place purchase order")
    question_2_str = input("Admin User? [Yes/No]: ")
    question_2 = question_2_str.upper()
    if question_2 == "YES":
        print("Enter payment details.")
        print("Place order.")
    elif question_2 == "NO":
        question_3_str = input("Approvel rules? [Approved/Rejected]: ")
        question_3 = question_3_str.upper()
        if question_3 == "APPROVED":
            print("Enter payment details.")
            print("Place order.")
        elif question_3 == "REJECTED":
            print("Purchase order rejected.")
        else:
            print("Abort, unknown input.")
    else:
        print("Abort, unknown input.")
elif question_1 == "OFFLINE":
    # Offline part
    print("Offline, place purchase order")
    question_4_str = input("Admin User? [Yes/No]: ")
    question_4 = question_4_str.upper()
    if question_4 == "YES":
        print("Order created automatically.")
    elif question_4 == "NO":
        question_5_str = input("Approvel rules? [Approved/Rejected]: ")
        question_5 = question_5_str.upper()
        if question_5 == "APPROVED":
            print("Order created automatically.")
        elif question_5 == "REJECTED":
            print("Purchase order rejected.")
        else:
            print("Abort, unknown input.")
    else:
        print("Abort, unknown input.")
else:
    print("Abort, unknown input.")
    