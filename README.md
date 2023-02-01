# Duckzilla

Met de energietransitie is het zelf produceren van energie nu belangrijker dan ooit. Om dit te doen hebben huizen tegenwoordig zonnepanelen, windmolens of andere installaties om energie op te wekken. De hoeveelheid energie die deze huizen opwekken is vaak meer dan het huishouden nodig heeft. Het overschot kan verkocht worden aan de energieleverancier maar de infrastructuur kan dit vaak niet aan. Om deze pieken op te kunnen vangen kunnen batterijen geplaatst worden. Deze kunnen op de piekmomenten energie opslaan en op een later moment weer energie leveren. 

Om de kosten hiervan zo laag mogelijk te houden is het belangrijk om zo min mogelijk kabels te hoeven leggen tussen de batterijen en de huizen. Hierbij mogen de huizen wel kabels delen. 

Voor dit probleem zijn drie wijken gegeven, deze bestaan allemaal uit een grid van 50*50 met daarin 150 huizen en 5 batterijen. Een stuk kabel kost 9 euro en een batterij 5000.

## Aan de slag

### Vereisten

Deze code is geschreven in Python 3.8.10. In requirements.txt staan de benodigde pakketen om de code te draaien. Deze zijn te installeren met de volgende instructie: 

    pip install -r requirements.txt

### Gebruik

Het programma kan gebruikt worden met het volgende commando met daarachter een instructie voor het algoritme wat gedraait moet worden:

    python main.py              genereert een leeg grid

    -r x                        voor random algoritme voor x seconden paden 90 graden
    --random_bf x               voor random algoritme voor x seconden, paden met breadthfirst
    --random_iteration x        random met een hillclimber voor x seconden paden 90 graden
    --random_iteration_bf x     random met een hillclimber voor x sconden paden met breadthfirst
    -g x                        greedy 1 keer paden 90 graden
    --greedy_bf x               greedy 1 keer paden met breadthfirst
    -gi x                       greedy 1 keer dan hillclimber paden 90 graden
    --greedy_iteration_bf x     greedy 1 keer dan hillclimber paden met breadthfirst
    -help                       geeft aan hoe de commando's gebruikt kunnen worden

### Structuur
as
De volgende lijst beschrijft in welke mappen de bestanden te vinden zijn:
- **/code**: bevat alle code van dit project
    - **/code/algorithms**: bevat de code voor de algoritmes
    - **/code/classes**: bevat de benodigde classes voor de case
    - **/code/viusualization**: bevat de code voor de plaatjes en de output
- **/data**: bevat de databestanden om de verschillende wijken in te laden
- **/output**: bevat de bestanden die gegenereerd worden door de code

## Auteurs

- Eva van Bastelaar
- Steven Kooi*
- Anou Prins

\* Steven heeft meegewerkt in de eerste 2 weken