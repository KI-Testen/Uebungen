#Lösung
### F1-Wert (engl. F1-score) = 2*(Präzision*Sensitivität) / (Präzision + Sensitivität)
from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred, average= None) # "None" berechnet die F1-Werte aus Präzision und Sensitivität für jede Klasse getrennt.
print("Präzision für average = None: ", f1)
f1 = f1_score(y_test, y_pred, average='micro')  # "micro" für mehrklassige Klassifikationen berechnet die Metriken global, indem die Summe der richtig Positiven, falschen Negativen und falschen Positiven gezählt werden.
print("Präzision für average = micro: ", f1)
f1 = f1_score(y_test, y_pred, average='macro')  # "macro" für mehrklassige Klassifikationen berechnet den ungewichteten Mittelwert über alle Klassen. Dabei wird das Ungleichgewicht der Klasse nicht berücksichtigt.
print("Präzision für average = macro: ", f1)
f1 = f1_score(y_test, y_pred, average='weighted')  # "weighted" für mehrklassige Klassifikation berechnet den Durchschnitt gewichtet nach der Anzahl der Instanzen in den Klassen.
print("Präzision für average = weighted: ", f1)