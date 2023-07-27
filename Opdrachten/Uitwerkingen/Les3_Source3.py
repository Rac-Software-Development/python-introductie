# Patient exposed to TB [Tuberculoses]
print("Patient exposed to TB")
question_1_str = input("Is the patient an adult or a child? [Adult/Child]: ")
question_1 = question_1_str.upper()
if question_1 == "ADULT":
    # Adult part
    print("Adult")
    question_2_str = input("Has common TB symptoms? [Yes/No]: ")
    question_2 = question_2_str.upper()
    if question_2 == "YES":
        print("Treat as likely TB patient and perform full TB exam.")
    elif question_2 == "NO":
        print("Have patient report back if unwell, return in 1 month for checkup.")
    else:
        print("Abort, unknown input.")
elif question_1 == "CHILD":
    # Child part
    print("Child")
    question_3_str = input("Can TB test be given? [Yes/No]: ")
    question_3 = question_3_str.upper()
    if question_3 == "YES":
        print("Administer TB test.")
        print("Assess TB test results and child's condition.")
    elif question_3 == "NO":
        question_4_str = input("Child well? [Yes/No]: ")
        question_4 = question_4_str.upper()
        if question_4 == "YES":
            print("6 months preventive isoniazid.")
            print("Have parent bring in if child shows any symptoms.")
        elif question_4 == "NO":
            print("Take full history.\nExamine for TB.")
            print("If TB likely diagnosis, treat for TB.")
            print("If other diagnosis more likely, treat as needed and watch for TB symptoms.")
        else:
            print("Abort, unknown input.")
    else:
        print("Abort, unknown input.")
else:
    print("Abort, unknown input.")
