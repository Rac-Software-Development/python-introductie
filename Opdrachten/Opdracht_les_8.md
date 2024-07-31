# Opdracht
Onderstaand vind je diverse opdrachten waar je mee aan de slag kunt. Type de opdrachten altijd zelf, zodat je de Python syntax in de vingers krijgt. Bij gemaakte fouten ga je de errors herkennen en leer je sneller wat je moet doen om deze te herstellen.

* Probeer vanaf hier eerst zelf de opdrachten te maken en kijk pas naar de voorgestelde code als je er echt niet uitkomt.

We verwijzen in volgende opdrachten misschien naar de code die je voor deze opdrachten schrijft. Het is dus belangrijk dat je deze opdrachten eerst maakt en opslaat in een bestand. Je kan dit bestand bijvoorbeeld de naam `Les8.py` geven.

# Scope
Na de voorgaande hoofdstukken is dit een wat korter - maar wel een lastig concept. Waarschijnlijk ben je er al achter dat variabelen afhankelijk van waar je deze gebruikt een beperkte houdbaarheid hebben in Python. De uitvoer van onderstaande code bijvoorbeeld: 

```python
def set_variable():
    a = "Rotterdam"
    print("Vanuit de functie: " + a)
    
set_variable()
print("Buiten de functie: " + a)
```

..geeft als uitvoer:

```
Vanuit de functie: Rotterdam
Traceback (most recent call last):
line 5, in <module>
    print("Buiten de functie: " + a)
NameError: name 'a' is not defined```
```

Dus de variabele "a" die wij aanmaken in de functie `set_variable` is niet beschikbaar buiten de functie. Dit is een concept dat "scope" heet. Variabelen die je aanmaakt in een functie zijn alleen beschikbaar in die functie. 
 
Variabelen aangemaakt buiten functies noemen we "globaal", en zijn beschikbaar op alle plaatsen in jouw python script. Bovenstaande code zou correct werken met de volgende aanpassing:

```python
def set_variable():
    print("Vanuit de functie: " + a)

# Variabele gedefinieerd buiten een functie
a = "Rotterdam"
set_variable()
print("Buiten de functie: " + a)
```

Afhankelijk van de programmeertaal die je gebruikt is scope meer of minder complex. Voorlopig werken wij met twee "scopes"
- Functie scope: variabelen die je aanmaakt in een functie zijn alleen beschikbaar in die functie. Dit noemen we "lokale variabelen"
- Globale scope: variabelen die je aanmaakt buiten een functie zijn beschikbaar in de hele file. Deze noem je in praktijk "globale variabelen".

# Globale variabelen
Zoals gezien in het laatste voorbeeld zijn variabelen aangemaakt buiten functies door het hele python script beschikbaar. Maar stel dat je diezelfde naam nu in jouw functie gebruikt?

```python
def set_variable():
    a = "Den Haag"
    print("Vanuit de functie: " + a)

a = "Rotterdam"
set_variable()
print("Buiten de functie: " + a)
```
Waarschijnlijk zal jouw ontwikkeltool al iets van een waarschuwing geven, laten we die even negeren.
Denk even na over wat je verwacht dat de uitkomst is. Hij zal je wellicht verbazen:

```
Vanuit de functie: Den Haag
Buiten de functie: Rotterdam
```

Dus ondanks dat de functie de variabele overschrijft en vanuit de functie "Den Haag" afdrukt is de waarde daarbuiten nog steeds "Rotterdam". 

Een probleem van globale variabelen is dat je al snel het overzicht kwijt raakt. En stel dat je in functie A() vetrouwt op een globale variabele met een verwachte waarde, maar een collega nieuwe code toevoegt die deze in functie B() wijzigt zonder jouw weten? Omdat dit op een hele andere plaats in de code is zoek je jezelf een ongeluk. 

Python probeert je hier te helpen door, tenzij je anders verteld, bij aanpassen van een globale variabele een nieuwe functie scope variabele te maken. Dus de "a" in de functie is eigenlijk een hele andere "a" dan die buiten de functie. Op systeemniveau verwijst deze zelfs naar een ander geheugenadres. 

Wil je nu toch echt een globale variabele wijzigen in een functie, dan dien je dat te melden aan Python met het sleutelwoord "global":

```python
def set_variable():
    global a
    a = "Den Haag"
    print("Vanuit de functie: " + a)

a = "Rotterdam"
set_variable()
print("Buiten de functie: " + a)
```
Nu mag de functie de globale variabele wel aanpassen:
```
Vanuit de functie: Den Haag
Buiten de functie: Den Haag
```

Let wel dat het hier gaat om het toewijzen van variabelen. Je kunt een globaal object dat met methodes is te wijzigen wel aanpassen in een functie zonder het "global" sleutelwoord te gebruiken:

```python
def set_variable():
    a.append("Den Haag")
    print("Vanuit de functie: " + str(a))

a = ["Rotterdam"]
set_variable()
print("Buiten de functie: " + str(a))```
```

## Vuistregels voor globale variabelen
In praktijk proberen we gebruik van globale variabelen te vermijden. Ze zijn lastig te beheren in praktijk. Als je ze toch gebruikt, houd dan rekening met de volgende vuistregels:
- Gebruik globale variabelen voor waardes die door het hele programma gebruikt worden en niet veranderen en schrijf de naam van de variabele in hoofdletters: 
```python
MAXIMUM_HEIGHT = 100
DEFAULT_PLAYER_NAME = "Veysel"
```
- Gebruik een globale variabele voor een wijzigbaar object dat in alle functies beschikbaar moet zijn. Bijvoorbeeld een lijst met alle vijanden in een shooter spel.
- Gebruik globale variabelen om gegevens op te slaan die tijd kosten om op te halen of te berekenen.


### Opdracht: Caching
Als opdracht gaan we een mechanisme maken om dat laatste punt te bewijzen. Een "cache" is een patroon waarin resultaten van een bewerking worden opgeslagen in het geheugen en bij een volgende invoer worden de gegevens niet berekend maar direct uit de cache teruggegeven. Dit kan alleen als bij een bepaalde invoer de uitvoer altijd hetzelfde is. 

We maken gebruik van het berekenen van alle priemgetallen tot een bepaald cijfer. Een priemgetal is een getal dat alleen deelbaar is door zichzelf én door 1. Dus stel dat we "10" invoeren, dan moet ons script de resultaten "2, 3, 5, 7" teruggeven. 

Het berekenen van grote priemgetallen is best lastig. Een bekende oplossing is de zeef van Eratosthenes, waarbij je gegeven een getal voor alle getallen daaronder kijkt welke er géén priemgetallen zijn en bewaard wat er overblijft. Die krijg je hier mee in een functie: 
```python
def zeef_van_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    current_prime = 2
    while current_prime * current_prime <= limit:
        if is_prime[current_prime]:
            for multiple in range(current_prime * current_prime, limit + 1, current_prime):
                is_prime[multiple] = False
        current_prime += 1
    
    prime_numbers = []
    for number in range(2, limit + 1):
        if is_prime[number]:
            prime_numbers.append(number)
    
    return prime_numbers

```
Alle onderdelen in deze functie komen je waarschijnlijk wel bekend voor, maar toch is dit al een complex geheel. Deze functie geeft een lijst object terug met alle priemgetallen. 

Maak met deze functie een programma als volgt:
- Maak een globale variabele met daarin een dictionary.
- Maak een functie die bij invoer van een getal controleert of deze al in de dictionary staat. Zo ja, geef deze terug als resultaat. Zo nee, voer de zeef_van_eratosthenes berekening uit, sla dat resultaat op in de cache en geef deze ook terug uit de functie. 
- Laat de gebruiker een getal invoeren
- Bereken hoeveel tijd er is verstreken tijdens aanroep van jouw functie. Met behulp van de time module van python kun je de huidige tijd meten in milliseconden en controleren hoeveel tijd er is verstreken:
```python
import time

tijd_nu = time.time()
doe_berekening()
tijd_verstreken = time.time() - tijd_nu
```
- Druk de verstreken tijd af

Getallen onder de 10000 zijn zo snel berekend, dat verschil zie je niet. Maar op mijn systeem begint de boel toch te hikken vanaf 1.000.000. Probeer eens twee maal dezelfde invoer grote invoer. Die zou bij de eerste keer tientallen secondes kunnen duren en in de uitvoer de tweede keer al direct klaar zijn. 

### Uitwerking
Een voorbeeld uitwerking: [Les8_Source1.py](Uitwerkingen%2FLes8_Source1.py)




