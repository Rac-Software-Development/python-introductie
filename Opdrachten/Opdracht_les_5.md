# Opdracht
Onderstaand vindt je diverse opdrachten waar je mee aan de slag kunt.
Type de opdrachten altijd zelf, zodat je de Python syntax in de vingers krijgt. Bij gemaakte fouten ga je de errors herkennen. Op een gegeven moment weet je wat je moet doen om dit te herstellen.
Type onderstaande opgaven in en kijk wat voor output je op het scherm krijgt. Pas een waarde aan en kijk wat het effect is. Dit zijn de basis dingen waar we later alles op gaan bouwen. Het is essentieel dat je deze zaken goed snapt.

## Modulo
We gebruiken in deze oefeningen een aantal keren de kreet "is deelbaar". Een snelle manier om te zien of een getal netjes deelbaar is is door de restwaarde van een deling op te zoeken en als die 0 is noemen we dat "is deelbaar door". 

Programmeertalen gebruiken daarvoor de "modulo" operator, het "%" teken. 4 % 3 is 1 bijvoorbeeld. Plat gezegd past 3 past één keer in 4 en er blijft dan 1 over. Nog wat voorbeelden: 
- 4 % 2 is 0, want 2 past twee keer in 4 en er blijft dan 0 over. 
- 4 % 4 is 0, want 4 past één keer in 4 en er blijft dan 0 over.
- 4 % 5 is 4, want 5 past niet in 4 en er blijft dan 4 over. 

## Itereren over een lijst
Een techniek die je heel veel zult gebruiken is het doorlopen van een lijst en het uitvoeren van een actie op elk element uit deze lijst.  

Een [hele](https://en.wikipedia.org/wiki/Fizz_buzz) [bekende](https://wiki.c2.com/?FizzBuzzTest) opdracht om te oefenen met programmeren is "Fizz Buzz". De regels zijn heel simpel:
- Loop door alle getallen van 1 tot 30
- Als het getal deelbaar is door 3 (bijvoorbeeld 3, 6 en 9) print dan "Fizz"
- Als het getal deelbaar is door 5 (dus 5, 10, 15) print dan "Buzz"
- Als het getal deelbaar is door 3 en 5 (dus 15, 30) print dan "FizzBuzz"
- In alle andere gevallen, print het getal zelf

Stel dat je door de getallen 1 tot 10 zou lopen zou dit bijvoorbeeld de uitkomst zijn: 
```
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz
```

Opdracht: Schrijf een programma dat de Fizz Buzz opdracht uitvoert. We helpen je wat op weg door alvast een lijst met getallen te maken. Gebruik een "for ... in" loop om door de lijst te lopen.  

```python
numbers = list(range(1, 31))
```

Als je het jezelf moeilijker wilt maken kun je proberen ditzelfde programma op te lossen niet met een "for .. in" maar met een "while" loop en één van de vele functies die je kunt aanroepen op een lijst object. Je zou hier ook de "walrus" operator kunnen toepassen, een recente toevoeging aan Python.

## Breaks en continues
Een andere techniek die je veel zult gebruiken is het onderbreken van een loop. De twee meest voorkomende manieren zijn "break" en "continue". Met een "break" stop je de loop helemaal. Met een "continue" ga je naar de volgende iteratie van de loop en voer je opvolgende code in de loop niet uit.

Breaks gebruik je bijvoorbeeld als je lijsten of dictionaries moet doorzoeken. Als je betreffende waarde al hebt gevonden (of zeker weet dat die er niet in zit) gebruik je een break om de loop te stoppen en versneld door te gaan met de rest van je programma.

Je gaat een programma schrijven dat alle priemgetallen onder de 100 uitrekent. Ter herinnering, een priemgetal is een cijfer dat alleen deelbaar is door zichzelf, door alle andere getallen komt er een niet geheel getal uit. Lus door alle mogelijke delers en gebruik een "break" om te stoppen met zoeken als je een deler hebt gevonden. Print het priemgetal iedere keer dat je zeker weet dat je er één hebt.  

1, 2, 3, 5 en 7 zijn bijvoorbeeld priemgetallen.

Begin je programma met de volgende code:  
```python 
numbers = list(range(1, 100))
```

## Geneste lijsten
Wat je ook regelmatig zult tegenkomen is een geneste lijst, oftewel een lijst met lijsten. Bijvoorbeeld: 
```python
mylist = [ ["appel", "peer"] , ["komkommer", "paprika"] ]
```
In dit geval geeft "mylist[0][1]" dus het eerste element van de buitenste lijst (["appel", "peer"]), gevolgd door daar dan weer het tweede element uit ("peer").

Opdracht 1: In het klassieke bingo spel krijg je een kaart met willekeurige getallen van 1 tot 99, bijvoorbeeld 16 getallen in een 4x5 rooster. Vervolgens worden er een aantal getallen omgeroepen en heb je één rij of kolom helemaal vol, dan heb je "bingo" en win je. 

Schrijf een programma dat een bingokaart genereert, in 4x4 formaat (4 rijen, 4 kolommen). Gebruik als uitgangspunt de volgende code om een lijst met willekeurige cijfers te genereren: 
```python
# Totaal aantal getallen op de kaart zal hoogte x breedte zijn
bingo_number_total = 4 ** 2
# Daarna maken we een lijst met 99 getallen waar we uit gaan kiezen
numbers_all = list(range(1, 100))
# We gooien alle ballen door elkaar
random.shuffle(numbers_all)
# ..en pakken de eerste 16 getallen
bingo_numbers = numbers_all[:bingo_number_total]
```
Een voorbeeld output zou er als volgt uit kunnen zien: 
```
[22, 35, 86, 45]
[11, 20, 31, 40]
[7, 91, 67, 0]
[10, 72, 27, 55]
```
Opdracht 2: Trek 50 willekeurige cijfers en streep die uit je bingo kaart weg. Bijvoorbeeld door er het getal 0 in te vullen. Druk het resultaat af. 

Opdracht 3: Nadat alle getallen zijn weggestreept, controleer de bingokaart en print "Bingo!" als je een volle rij of kolom hebt. Dit is een pittige opdracht - een oplossingsrichting is het totaal van iedere rij en iedere kolom te tellen en als er een rij of kolom is waarvan de som 0 is, dan heb je bingo.


## While loops
Een andere manier om door een lijst te lopen is met een "while" loop. Een "while" loop is een loop die blijft herhalen zolang een bepaalde conditie waar is.

Opdracht: In een eerdere opdracht heb je geleerd over invoer vragen aan de gebruiker. Maak nu een programma dat vraagt om getallen tot 100. Reken vervolgens uit of dat getal een priemgetal is (zie de voorgaande opdracht). Vraag daarna meteen om een nieuw getal. Laat de gebruiker afsluiten door een "." in te voeren.

Je zult tegen problemen aanlopen met het combineren van strings en integers. Je kunt dit oplossen door de input te forceren naar een integer, als volgt: 
```python
number_input = int("3")
```

Een voorbeeld uitvoer: 
```
Geef een getal: 5
5 is een priemgetal
Geef een getal: 4
4 is geen priemgetal
Geef een getal: .
Tot ziens!
```
Als uitbreiding: het is natuurlijk heel lastig dat je alleen cijfers of een punt kunt invoeren. Bij tekst faalt je programma met een lelijke fout. Je zou een voorsprong kunnen nemen op de stof door te kijken naar de "try ... except" constructie. 

# Uitwerkingen
Mocht je niet uit de opdrachten komen, dan kun je onderstaande uitwerkingen gebruiken ter inspiratie: 

- Itereren over een lijst
```python
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
```
-  Breaks en continues
```python
numbers = list(range(1, 100))
for number in numbers:
    is_prime = True
    for deler in numbers:
        if deler < number and deler > 1:
            if number % deler == 0:
                is_prime = False
                break
    if is_prime:
        print(number)
```

- Bingo!
```python
import random

# Vul de bingo kaart
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

print(bingo_card)
if bingo:
    print("Yes! Bingo!")
else:
    print("Jammer, geen bingo, morgen weer een dag")
```

- While loops
```python
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
```


