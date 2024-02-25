#Lösung
### Sensitivität (engl. recall) = RP / (RP + FN)
from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred, average= None) # "None" berechnet die Sensitivität für jede Klasse getrennt.
print("Sensitivität für average = None: ", recall)
recall = recall_score(y_test, y_pred, average='micro')  # "micro" für mehrklassige Klassifikationen berechnet die Metriken global, indem die Summe der richtig Positiven, falschen Negativen und falschen Positiven gezählt werden.
print("Sensitivität für average = micro: ", recall)
recall = recall_score(y_test, y_pred, average='macro')  # "macro" für mehrklassige Klassifikationen berechnet den ungewichteten Mittelwert über alle Klassen. Dabei wird das Ungleichgewicht der Klasse nicht berücksichtigt.
print("Sensitivität für average = macro: ", recall)
recall = recall_score(y_test, y_pred, average='weighted')  # "weighted" für mehrklassige Klassifikation berechnet den Durchschnitt gewichtet nach der Anzahl der Instanzen in den Klassen.
print("Sensitivität für average = weighted: ", recall)