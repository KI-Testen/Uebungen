from sklearn import tree   # Wir benutzen das Entscheidungsbaum-Modell (tree) der Bibliothek scikit-learn

# Einen Entscheidungsbaum mit maximaler Tiefe ... erzeugen und per '.fit()'-Methode mit den Trainigsdaten trainieren
model_dtree = tree.DecisionTreeClassifier(max_depth=4)
model_dtree.fit(X_train, y_train)

# Die Genauigkeit über alle Ergebnisklassen ermitteln: "Wieviel Prozent der Ergebnisse waren richtig?"
print('Tiefe des Entscheidungsbaums: {0}'.format(model_dtree.get_depth()))
print('Die Genauigkeit auf den Trainingsdaten    liegt bei {0:3.2f}%'.format(model_dtree.score(X_train,y_train)*100))
print('Die Genauigkeit auf den Validierungsdaten liegt bei {0:3.2f}%'.format(model_dtree.score(X_val,  y_val  )*100))