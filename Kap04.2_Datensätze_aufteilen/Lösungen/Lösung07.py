# iris-Datensatz (X) und (y) in Trainings-, Validierungs- und Testdatensatz aufteilen
rs = 8

X_trainval, X_test, y_trainval, y_test = train_test_split( X, y, test_size=0.1, random_state=rs )
X_train, X_val, y_train, y_val = train_test_split( X_trainval, y_trainval, test_size=1/9, random_state=rs )

# den Entscheidungsbaum mit maximaler Tiefe 8 erzeugen und per '.fit()'-Methode mit den Trainigsdaten trainieren
model_dtree = tree.DecisionTreeClassifier(max_depth=8)
model_dtree.fit(X_train, y_train)

# die Genauigkeit auf allen drei Datensätzen vergleichen
genauigkeit()