# Opdracht
Onderstaand vind je diverse opdrachten waar je mee aan de slag kunt. Type de opdrachten altijd zelf, zodat je de Python syntax in de vingers krijgt. Bij gemaakte fouten ga je de errors herkennen en leer je sneller wat je moet doen om deze te herstellen.

* Probeer vanaf hier eerst zelf de opdrachten te maken en kijk pas naar de voorgestelde code als je er echt niet uitkomt.

We verwijzen in volgende opdrachten misschien naar de code die je voor deze opdrachten schrijft. Het is dus belangrijk dat je deze opdrachten eerst maakt en op slaat in een bestand. Je kan dit bestand bijvoorbeeld de naam `Les1.py` geven.

# Functies
Functies zijn een manier om code te groeperen en te hergebruiken. Je kan een functie zien als een klein programmaatje binnen je programma. Je kan een functie aanroepen en deze kan dan een waarde teruggeven. Je kan ook een functie aanroepen en deze kan dan een actie uitvoeren. Een functie kan ook beide doen, een waarde teruggeven en een actie uitvoeren.

Code splitsen in functies heeft een heleboel voordelen:
* Je voorkomt dat je code gaat dupliceren. Gedupliceerde code is lastig leesbaar en onderhoudbaar.
* Je kunt code hergebruiken, zowel in hetzelfde programma als in andere programma's.
* Je kunt code makkelijker testen en debuggen.
* Het is makkelijker om samen te werken in code die gesplitst is in functies

Code die je schrijft moet je zo snel mogelijk in functies zetten. Je zult zien dat je code veel leesbaarder wordt en dat je veel minder fouten maakt. 

## Functie aanroepen
Een functie aanroepen doe je door de naam van de functie te gebruiken met daarachter haakjes. Bijvoorbeeld:

```python
def print_hello():
    print('Hello')
    
print_hello()
```

Functies kun je argumenten meegeven. Deze argumenten kun je gebruiken binnen de functie. Bijvoorbeeld:

```python
def print_hello(name):
    print(f'Hello {name}')

print_hello('John')    
```

### Rekenmachine
We gaan een simpele rekenmachine maken die de volgende functies heeft: 
- `add` telt twee getallen bij elkaar op en drukt het resultaat af
- `subtract` trekt twee getallen van elkaar af en drukt het resultaat af
- `multiply` vermenigvuldigt twee getallen met elkaar en drukt het resultaat af
- `divide` deelt twee getallen door elkaar en drukt het resultaat af

De functies moeten als volgt werken:
- `add(1, 2)` drukt `3` af
- `subtract(1, 2)` drukt `-1` af
- `multiply(1, 2)` drukt `2` af
- `divide(1, 2)` drukt `0.5` af

..daarnaast moet de rekenmachine ook nog een functie hebben die de gebruiker vraagt om twee getallen en een operator, en vervolgens de juiste functie aanroept. Bijvoorbeeld:

```python
input1 = input('Geef het eerste getal: ')
input2 = input('Geef het tweede getal: ')
operator = input('Geef de operator (+, -, * of /): ')
```

Let wel, hier gebeurt nog iets bijzonders. De functie `input` geeft een string terug en daar kunnen we niet mee rekenen. Voer bijvoorbeeld de volgende code uit: 
```python
string1 = "1"
string2 = "2"
print(string1 + string2)  # drukt "12" af
print(string1 - string2)  # geeft een error (strings kun je niet van elkaar aftrekken)
```
We moeten dus de string omzetten naar een getal. Dat kan met de functie `int` of `float`. Bijvoorbeeld:

```python
input1 = input('Geef het eerste getal: ')
number1 = int(input1)
print(number1 + number1)  # drukt "2" af
```

### Uitwerking
Een voorbeeld uitwerking: [Les7_Source1.py](Uitwerkingen%2FLes7_Source1.py)


## Functies met standaard waarden
Je kunt een functie argument een standaard waarde geven. Als je de functie aanroept zonder dat argument, dan wordt de standaard waarde gebruikt. Bijvoorbeeld:

```python
def print_hello(name='John'):
    print(f'Hello {name}')
    
print_hello() # drukt "Hello John" af
print_hello('Jane') # drukt "Hello Jane" af
```

### Rekenmachine met extra output
Pas de functies van de rekenmachine aan om een derde waarde te accepteren, "debug", met een standaard waarde van `False`. Als de waarde `True` is, druk dan naast het antwoord de hele som af én een waarschuwing als één van de getallen een 0 is. Bijvoorbeeld:

```python
add(1, 2, True) # drukt "Debug: 1 + 2" en daarna "3" af
add(1, 2) # drukt "3" af
```

Voeg een vraag toe voor de gebruiker om te vragen of hij debug informatie wil zien.

### Uitwerking
Een voorbeeld uitwerking: [Les7_Source2.py](Uitwerkingen%2FLes7_Source2.py)


## Functie met return waarde
Een functie kan een waarde teruggeven. Dit doe je met het `return` statement. Bijvoorbeeld:

```python
def add(a, b):
    return a + b

result = add(1, 2)
print(result)
```

### Refactoring
"Refactoring" is een kreet die je nog veel zult tegenkomen. Refactoring slaat op het herschrijven van code, zonder dat de input of output verandert. Dat doe je vaak omdat je de code beter leesbaar wilt maken, of omdat je de code wilt hergebruiken.

We gaan de code van een vorige opdracht refactoren. Als je onze uitwerking bekijkt van [Les3_Source5.py](Uitwerkingen%2FLes3_Source5.py) zijn daar een paar zaken niet heel netjes: 
- We vragen gebruikers steeds te kiezen uit een aantal zaken ("KOUD of WARM"), maar die keuze dwingen we niet af. Je kunt nog steeds "LAUW" invoeren waar "KOUD" of "WARM" verwacht wordt. We willen die keuze afdwingen, dat kan bijvoorbeeld met een `while` loop: 
```python
answer = ""
while answer != "KOUD" and answer != "WARM":
    answer = input("Wil je warme of koude drank? (KOUD/WARM) ")
```
- Je ziet een aantal regels code rondom vragen steeds terugkomen. Maak een aparte functie die vragen kan stellen en het antwoord terug geeft als return, met controle op de antwoorden zoals hierboven beschreven. Bijvoorbeeld: 
```python
def ask_question(question, valid_answers):
    ... 
    return answer
```
- We hebben keuzes die leiden tot andere keuzes, waardoor we een hele lange lap code krijgen. We willen overzicht krijgen door de code op te splitsen in functies voor in het restaurant eten / meenemen, voor de burgers keuze, voor warme drankjes en een functie voor koude drankjes. De uiteindelijke code zou er dan ongeveer zo uit kunnen zien: 
```python  
    food_answer = ask_question("Burgers of drankjes?", ["Burgers", "Drankjes"])
    if food_answer == "BURGERS":
        get_burger_choice()
    elif food_answer == "DRANKJES":
        drink_choice = ask_question("Drankjes", ["Warme", "Koude"])
```

Neem de oude code en refactor deze, waarbij je bovenstaande drie verbeteringen doorvoert. 

### Uitwerking
Een voorbeeld uitwerking: [Les7_Source3.py](Uitwerkingen%2FLes7_Source3.py)
