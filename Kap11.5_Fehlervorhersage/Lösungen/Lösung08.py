# Dies ist eine Kopie des etwas weiter obenstehenden Codes. Hier ist nur die maximale Tiefe des Entscheidungsbaums auf 5 limitiert worden

from sklearn.model_selection import train_test_split   # zum Aufteilen der Trainings- und Testdaten
from sklearn                 import tree

# 1. Trainings- und Testdaten aufteilen
X_train, X_val, y_train, y_val = train_test_split( X, y, test_size=0.1, random_state=4 )

# 2. Einen Entscheidungsbaum mit maximaler Tiefe 5 erzeugen
# 3. und das Modell per '.fit()'-Methode mit den Trainigsdaten trainieren
model_dtree = tree.DecisionTreeClassifier(max_depth=5, random_state=16)
model_dtree.fit(X_train, y_train)

# 4. Die Genauigkeit über alle Ergebnisklassen ermitteln: "Wieviel Prozent aller Ergebnisse waren richtig?"
print('Tiefe des Entscheidungsbaums: {0}'.format(model_dtree.get_depth()))
print('Die Genauigkeit auf den Trainingsdaten    liegt bei {0:3.2f}%'.format(model_dtree.score(X_train, y_train)*100))
print('Die Genauigkeit auf den Validierungsdaten liegt bei {0:3.2f}%'.format(model_dtree.score(X_val  , y_val  )*100))