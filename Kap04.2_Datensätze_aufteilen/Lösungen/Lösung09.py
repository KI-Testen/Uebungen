# Lege den Entscheidungsbaum mit maximaler Tiefe 8 an
model_dtree = tree.DecisionTreeClassifier(max_depth=8)
# Trainiere diesen per '.fit()'-Methode mit den Daten
model_dtree.fit(X_trainval, y_trainval)

# und prüfe das Modell mit den Testdaten (siehe weiter oben bei genauigkeit()!)
acc = model_dtree.score(X_test, y_test)*100

# Vergleiche die Genauigkeit aus der k-fachen Kreuzvalidierung und dem Test mit den Testdaten
print(f"Die geschätzte Genauigkeit des Modells mit k-facher Kreuzvalidierung bei {avg_acc:3.2f}%")
print(f"Die            Genauigkeit des Modells mit den Testdaten liegt bei       {acc:3.2f}%")