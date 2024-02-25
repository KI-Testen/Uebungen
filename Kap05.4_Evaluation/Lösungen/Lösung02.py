### Präzision (engl. precision) = RP / (RP + FP)  
from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred, average= None) # "None" berechnet die Präzision für jede Klasse getrennt.
print("Präzision für average = None: ", precision)
precision = precision_score(y_test, y_pred, average='micro')  # "micro" für mehrklassige Klassifikationen berechnet die Metriken global, indem die Summe der richtig Positiven, falschen Negativen und falschen Positiven gezählt werden.
print("Präzision für average = micro: ", precision)
precision = precision_score(y_test, y_pred, average='macro')  # "macro" für mehrklassige Klassifikationen berechnet den ungewichteten Mittelwert über alle Klassen. Dabei wird das Ungleichgewicht der Klasse nicht berücksichtigt.
print("Präzision für average = macro: ", precision)
precision = precision_score(y_test, y_pred, average='weighted')  # "weighted" für mehrklassige Klassifikation berechnet den Durchschnitt gewichtet nach der Anzahl der Instanzen in den Klassen.
print("Präzision für average = weighted: ", precision)