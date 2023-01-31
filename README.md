# Duckzilla

### Is nog niet af

Groene energie is de energie van de toekomst, en zelf produceren is de mode van nu. Veel huizen hebben tegenwoordig zonnepanelen, windmolens of andere installaties om zelf energie mee te produceren. Fortuinlijk genoeg produceren die installaties vaak meer dan voor eigen consumptie nodig is. Het overschot zou kunnen worden terugverkocht aan de leverancier, maar de infrastructuur (het *grid*) is daar veelal niet op berekend. Om de pieken in consumptie en produktie te kunnen managen moeten er batterijen geplaatst worden.

## Aan de slag

### Vereisten

text enzo

    pip install -r requirements.txt

### Gebruik

Het programma kan gebruikt worden met het volgende commando:

    python main.py

    -r x                        voor random algoritme voor x seconden paden 90 graden
    --random_bf x               voor random algoritme voor x seconden, paden met breadthfirst
    --random_iteration90 x      random met een hillclimber voor x seconden paden 90 graden
    --random_iteration_bf x     random met een hillclimber voor x sconden paden met breadthfirst
    -g x                        greedy 1 keer paden 90 graden
    --greedy_bf x               greedy 1 keer paden met breadthfirst
    -gi x                       greedy 1 keer dan hillclimber paden 90 graden
    --greedy_iteration_bf x     greedy 1 keer dan hillclimber paden met breadthfirst

### Structuur

## Auteurs
- Eva van Bastelaar
- Steven Kooi
- Anou Prins