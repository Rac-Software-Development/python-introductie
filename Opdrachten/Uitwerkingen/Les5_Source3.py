import random

# Vulk de bingo kaart
bingo_card = []
bingo_card_size = 4
bingo_number_total = bingo_card_size ** 2
bingo_numbers_all = list(range(1, 100))
random.shuffle(bingo_numbers_all)
bingo_numbers = bingo_numbers_all[:bingo_number_total]
for line in range(bingo_card_size):
    bingo_row = []
    for column in range(bingo_card_size):
          bingo_row.append(bingo_numbers.pop())
    bingo_card.append(bingo_row)

# Trek 50 willekeurige getallen
draw_number = 50
bingo_balls = list(range(1, 100))
random.shuffle(bingo_balls)
drawn_balls = bingo_balls[:draw_number]
# Streep de getallen weg die je op jouw kaart hebt staan
# Dit is niet de meest efficiënte manier, maar het werkt
for ball in drawn_balls:
    for line in range(bingo_card_size):
        for column in range(bingo_card_size):
            if bingo_card[line][column] == ball:
                bingo_card[line][column] = 0

# Controleer of je een bingo hebt
bingo = False
for index in range(bingo_card_size):
    if sum(bingo_card[index]) == 0:
        bingo = True
        break
    # De kolommen zijn wat lastiger..
    column_total = 0
    for column_index in range(bingo_card_size):
        column_total += bingo_card[column_index][index]
    if column_total == 0:
        bingo = True
        break

for line in bingo_card:
    print(line)
if bingo:
    print("Yes! Bingo!")
else:
    print("Jammer, geen bingo, morgen weer een dag")