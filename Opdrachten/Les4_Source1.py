# List of Games
popular_games = ["Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
                 "Fortnite Battle Royale 39 Million 2017",
                 "Apex Legends 50 Million (1 Month) 2019",
                 "Leauge of Legends (LOL) 27 Million 2009",
                 "Counter Strike; Global Offensive 32 Million 2014",
                 "Heartstone 29 Million 20120",
                 "Minecraft 91 Million 2011",
                 "DOTA 2 5 million 2015",
                 "The Division 2 N/A 2019",
                 "The Splatoon 2"]

print(popular_games)
print()


# a]
print(f"5] {popular_games[4]}")
print(popular_games)
print()

# b]
dota_game = popular_games[7]
characters_in_name = len(dota_game)
print(f"The game {dota_game} has {characters_in_name} characters.")
print(popular_games)
print()

# c]
number_of_games = len(popular_games)
print(f"Er zitten {number_of_games} games in de lijst.")
print(popular_games)
print()

# d]
popular_games.insert(1, "Snake")
print(popular_games)
print()

# e]
index_of_splatoon = popular_games.index("The Splatoon 2")
splatoon = popular_games.pop(index_of_splatoon)
print(f"Helaas heeft de game {splatoon} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {splatoon}.")
print()

# f]
index_of_heartstone = popular_games.index("Heartstone 29 Million 20120")
popular_games[index_of_heartstone] = "Heartstone 29 Million 2012"
print(popular_games)
print()
