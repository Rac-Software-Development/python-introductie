# Opdracht
Onderstaand vindt je diverse opdrachten waar je mee aan de slag kunt.
Type de opdrachten altijd zelf, zodat je de Python syntax in de vingers krijgt. Bij gemaakte fouten ga je de errors herkennen. Op een gegeven moment weet je wat je moet doen om dit te herstellen.
Type onderstaande opgaven in en kijk wat voor output je op het scherm krijgt. Pas een waarde aan en kijk wat het effect is. Dit zijn de basis dingen waar we later alles op gaan bouwen. Het is essentieel dat je deze zaken goed snapt.


## Integers
Rekenen met integers heb je in de vorige les al een beetje gedaan. We gaan nu naar wat grotere getallen kijken. Python kan namelijk met enorme getallen omgaan. Dit kost uiteraard enorme rekenkracht waardoor sommige PC's langere tijd non-responsive kunnen worden. Hier zijn de getallen niet extreem gekozen.

```python
# Display large numbers in a readable format
people = 7861304740
print(people)
people = 7_861_304_740
print(people)
```

### Output
![Antwoord 1](./Images/Les2-Antwoord_1.png)


```python
# Calculations with big numbers
meals = 3
people_eat = people * meals
print(people_eat)

days = 365
meals_per_year = people_eat * days
print(meals_per_year)

# What is the data type?
type(meals_per_year)

```

### Output
![Antwoord 2](./Images/Les2-Antwoord_2.png)

## Float
Het floating point data type kan gebroken getallen weergeven. Dit zagen we bij de delingen die we eerder hebben gemaakt.

```python
# Ethernet capacity
ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)

```

### Output
![Antwoord 3](./Images/Les2-Antwoord_3.png)


```python
# Print capacity used on the ethernet
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)

```

### Output
![Antwoord 4](./Images/Les2-Antwoord_4.png)


```python
# Speed of light in m/s
speed_of_light = 299_792_458

# Distance Rotterdam / New York in km
distance_Rotterdam_NewYork = 5_862.03
# Distance Rotterdam to New York in meters divided by the speed of light
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(f'Time to reach New York is: {time_to_reach_NYC} seconds => {time_to_reach_NYC * 1000.0} milliseconds.')

# What is the data type?
type(time_to_reach_NYC)

```

### Output
![Antwoord 6](./Images/Les2-Antwoord_6.png)


## String
De string is een enorm uitgebreid datatype, waarvan we gaande weg steeds meer gaan gebruiken. In eerste instantie gaan we hem gebruiken om regels te bewaren/weer te geven.

```python
ship = 'Titanic'
print(ship)
ship = "Titanic"
print(ship)
ship = """Titanic"""
print(ship)

```

### Output
![Antwoord 7](./Images/Les2-Antwoord_7.png)


```python
# Note: The sentence could contain an apostrophe
# Using an apostrophe is possible if you use the double quotes to surround the string
sentence = "He doesn’t think it’s a good idea to spend all his money on video games."
print(sentence)

```

### Output
![Antwoord 8](./Images/Les2-Antwoord_8.png)


```python
# Gebruik """ """ als je meerdere regels tekst moet tonen
paragraph = """Computer Technology means all designs, drawings, procedures (including design, manufacturing, test and maintenance procedures), specifications, software (other than as described within the meaning of the term "Software" defined elsewhere herein), printed circuit board art work, integrated circuit masks, test equipment, tools, fixtures, documentation, training materials, and information, in whatever form, related to, useful, utilizable or necessary in the design, manufacture, test and/or maintenance of the computer system, or relate to any Technology Licenses."""
print(paragraph)
# With the len() function you can ask how many characters the string has
characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")

```

### Output
![Antwoord 9](./Images/Les2-Antwoord_9.png)


```python
year = 1936
inventor = "Alan Turing"
name_of_machine = "automatic machine"
# Note: Within the text double quotes are used. We need to use single quotes to embrace the string
invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine" ({name_of_machine}).'
print(invention)

# What is the data type?
type(invention)

```

### Output
![Antwoord 10](./Images/Les2-Antwoord_10.png)


## Boolean
De boolean is een True of False indicatie. Deze toestand kan uit de waarde van variabelen komen of uit vergelijkingen.

```python
logged_in = False
print(logged_in)

netwerk_activity = True
print(netwerk_activity)

```

### Output
![Antwoord 11](./Images/Les2-Antwoord_11.png)


```python
user_name = "John Doe"
entered_name = input("User name, please: ")
size_user_name = len(user_name)
size_entered_name = len(entered_name)
user_name_is_bigger = size_user_name > size_entered_name
entered_name_is_bigger = size_entered_name > size_user_name
print(f"The user name {user_name} has more characters then the entered name {entered_name} is: {user_name_is_bigger}")
print(f"The entered name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")

lights_on = False
lock_closed = True
# Not keert de waarde van een boolean om not True is hetzelfde als False
# Andersom is not False dus True
alarm_activated = not lights_on and lock_closed
print(f"The alarm is activated, is: {alarm_activated}")

```

### Output
![Antwoord 12](./Images/Les2-Antwoord_12.png)


## Berekening
Zet de volgende formule om naar Python code:

![Formule 1](./Images/Formule_1.png)



Bereken het antwoord als x = 9.1
Geef het anwtoord weer in de volzin:

De waarde van y = [antwoord berekening] als x = [waarde van x].

```python
import math

x = 9.1
term1 = (3 * x) - 1
term2 = 1 + x
term3 = (term2)**2
y = math.sqrt(term1) + term3
print(f'De waarde van y = {y} als x = {x}')

```

### Output
![Antwoord 13](./Images/Les2-Antwoord_Source_1.png)


## Berekening
Zet de volgende formule om naar Python code:

![Formule 2](./Images/Formule_2.png)


Bereken het antwoord als:
- a = 0.87
- b = 22.7
- c = 5.03

Geef het antwoord weer in een volzin:
De waarde van y = [antwoord berekening] als a = {waarde van a}, b = {waarde van b} en c = {waarde van c}


```python
import math

a = 0.87
b = 22.7
c = 5.03
term1 = b**2
term2 = 4 * a * c
term3 = term1 - term2
term4 = math.sqrt(term3)
term5 = -b + term4
term6 = 2 * a
y = term5 / term6

print(f'De waarde van y = {y} als a = {a}, b = {b} en c = {c}')

```

### Output
![Antwoord 14](./Images/Les2-Antwoord_Source_2.png)


## Containers
Op een terminal worden schepen gelost en geladen. Tijdens het lossen worden 331 containers gelost in 441 minuten. Na het lossen wordt het schip geladen met 287 containers in 295 minuten.
Bedenk een goede representieve variabele naam voor de *geloste* containers en ken het aantal geloste containers toe aan de variabele.
Bedenk een goede representieve variabele naam voor de *geladen* containers en ken het aantal geladen containers toe aan de variabele.
Bereken van zowel het laden als lossen de gemiddelde laad/lostijd. Geef deze weer op in een volzin: De gemiddelde tijd die het laden of lossen duurt.

```python
# Terminal information
containers_unloaded = 331
unload_time = 441
containers_loaded = 287
load_time = 295

# Calculate the averages containers per minute
average_unload_time = unload_time / containers_unloaded
average_load_time = load_time / containers_loaded

print(f'De gemiddelde lostijd bedraagt {average_unload_time} minuten per container')
print(f'De gemiddelde lostijd bedraagt {average_load_time} minuten per container')

```

### Output
![Antwoord 15](./Images/Les2-Antwoord_Source_3.png)


## Berekening
Tijd en ruimte zijn geen absolute concepten, maar relatief en afhankelijk van de snelheid van de waarnemer.
Met behulp van onderstaande formule kan worden berekend hoeveel de tijd versneld of vertraagd afhankelijk van de snelheid van de waarnemer.
U kijkt vanaf uw tuinstoel gedurende t = 4 uur naar een passeerde komeet die met een snelheid van v = 179875474.8 m/s langs de hemel trekt.
Hoeveel tijd zou er gepasseerd zijn als u op de komeet zou zitten en naar uw tuinstoel op de aarde keek, gegeven dat de lichtsnelheid c = 299792458 m/s?
Gegeven de formule: 

![Formule 3](./Images/Formule_3.png)

Bereken de delta en druk het berekende antwoord af op het scherm in de zin:

Vanaf een komeet gezien zit u {x} uur op de tuinstoel.
Waarbij de {x} wordt vervangen door het berekende antwoord.

```python
# Information
t = 4
v = 179875474.8
c = 299_792_458

# Breakup the formula
term1 = v**2
term2 = c**2
term3 = term1 / term2
term4 = 1 - term3
term5 = v * term4
term6 = 1 / term5
delta = t * term6

# Display result
print(f'Vanaf een komeet gezien zit u {delta} uur op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0} minuten op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0 * 60.0} seconden op de tuinstoel.')

```

### Output
![Antwoord 16](./Images/Les2-Antwoord_Source_4.png)