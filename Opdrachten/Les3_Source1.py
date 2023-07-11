connection_choice_str = input('Welke verbinding wilt U gebruiken [4G, 5G, Wifi open]: ')

# Convert answer to upper case
# The user can enter upper, lower or combined casing
connection_choice = connection_choice_str.upper()

if connection_choice == "4G":
    print(f"U bent verbonden via {connection_choice}!")
elif connection_choice == "5G":
    print(f"U bent verbonden via {connection_choice}")
elif connection_choice == "WIFI OPEN":
    print(f"U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    answer_str = input("Wilt u nog steeds een verbinding maken? [ja/nee]: ")
    answer = answer_str.upper()
    if answer == "JA":
        print(f"U bent verbonden via {connection_choice}!")
    else:
        print("U bent niet verbonden!")
else:
    print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")
