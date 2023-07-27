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
- Als het getal deelbaar is door 3 (bijvoorbeeld 3, 6 en 9) print "Fizz"
- Als het getal deelbaar is door 5 (dus 5, 10, 15) print "Buzz"
- Als het getal deelbaar is door 3 en 5 (dus 15, 30) print "FizzBuzz"
- In alle andere gevallen, print het getal zelf

Stel dat je door de getallen 1 tot 10 zou lopen zou dit bijvoorbeeld de uitkomst zijn: 
```
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz
```

Opdracht: Schrijf een programma dat de Fizz Buzz opdracht uitvoert door met module te controleren of de getallen deelbaar zijn. We helpen je wat op weg door alvast een lijst met getallen te maken. Gebruik een "for ... in" loop om door de lijst te lopen.  

```python
numbers = list(range(1, 31))
```

Als je het jezelf moeilijker wilt maken kun je proberen ditzelfde programma op te lossen niet met een "for .. in" maar met een "while" loop en één van de vele functies die je kunt aanroepen op een lijst object. Je zou hier ook de "walrus" operator kunnen toepassen, een recente toevoeging aan Python.

### Uitwerking
Een voorbeeld uitwerking: [Les5_Source1.py](Uitwerkingen%2FLes5_Source1.py)


## Breaks en continues
Een andere techniek die je veel zult gebruiken is het onderbreken van een loop. De twee meest voorkomende manieren zijn "break" en "continue". Met een "break" stop je de loop helemaal. Met een "continue" ga je naar de volgende iteratie van de loop en voer je opvolgende code in de loop niet uit.

```python
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
    if i == 7:
        break
```

Breaks gebruik je bijvoorbeeld als je lijsten of dictionaries moet doorzoeken. Als je betreffende waarde al hebt gevonden (of zeker weet dat die er niet in zit) gebruik je een break om de loop te stoppen en versneld door te gaan met de rest van je programma.

Je gaat een programma schrijven dat alle priemgetallen onder de 100 uitrekent. Ter herinnering, een priemgetal is een cijfer dat alleen deelbaar is door zichzelf, door alle andere getallen komt er een niet geheel getal uit. Lus door alle mogelijke delers en gebruik een "break" om te stoppen met zoeken als je een deler hebt gevonden. Print het priemgetal iedere keer dat je zeker weet dat je er één hebt.  

1, 2, 3, 5 en 7 zijn bijvoorbeeld priemgetallen.

Begin je programma met de volgende code:  
```python 
numbers = list(range(1, 100))
```

### Uitwerking
Een voorbeeld uitwerking: [Les5_Source2.py](Uitwerkingen%2FLes5_Source2.py)


## Geneste lijsten
Wat je ook regelmatig zult tegenkomen is een geneste lijst, oftewel een lijst met lijsten. Bijvoorbeeld: 
```python
mylist = [ ["appel", "peer"] , ["komkommer", "paprika"] ]
```
In dit geval geeft "mylist[0][1]" dus het eerste element van de buitenste lijst (["appel", "peer"]), gevolgd door daar dan weer het tweede element uit ("peer").

Opdracht 1: In het klassieke bingo spel krijg je een kaart met willekeurige getallen van 1 tot 99, bijvoorbeeld 16 getallen in een 4x5 rooster. Vervolgens worden er een aantal getallen omgeroepen en heb je één rij of kolom helemaal vol, dan heb je "bingo" en win je. 

Schrijf een programma dat een bingokaart genereert, in 4x4 formaat (4 rijen, 4 kolommen). Gebruik als uitgangspunt de volgende code om een lijst met willekeurige cijfers te genereren: 
```python
# We hebben de random module nodig om willekeurige getallen te genereren
import random
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

### Uitwerking
Een voorbeeld uitwerking: [Les5_Source3.py](Uitwerkingen%2FLes5_Source3.py)



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

### Uitwerking
Een voorbeeld uitwerking: [Les5_Source4.py](Uitwerkingen%2FLes5_Source4.py)
