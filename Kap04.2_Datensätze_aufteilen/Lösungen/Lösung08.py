from sklearn.model_selection import KFold    # Wir nutzen die Klasse 'KFold' der scikit-Bibliothek

# Mit KFold eine 9-fach Kreuzvalidierung definieren
folds = KFold(n_splits=9)

avg_acc = 0 # Mittlere Genauigkeit mit 0 initialisiern

# Über alle Split-Kombinationen Der Eingaben (X_trainval) und Ausgaben (y_trainval) iterieren und jeweils:
for (i_train, i_val) in folds.split(X_trainval):
    # den Entscheidungsbaum mit maximaler Tiefe 8 anlegen,
    model_dtree = tree.DecisionTreeClassifier(max_depth=8)
    
    # per '.fit()'-Methode mit den Trainigsdaten trainieren. Achtung: i_train sind nur die Indizes, nicht die Daten
    model_dtree.fit(X_trainval.iloc[i_train], y_trainval.iloc[i_train])
    
    # die Genauigkeit per '.score' anahand ver Validierungsdaten berechnen. Hinweis: benutze i_val
    acc = model_dtree.score(X_trainval.iloc[i_val],y_trainval.iloc[i_val])*100
    
    print(f" - Modellgenauigkeit auf den fold-Validierungsdaten liegt bei {acc:03.2f}%")
    avg_acc += acc  # Genauigkeit aufaddieren

avg_acc /= folds.get_n_splits() # nun noch den Mittelwert aus der akkumulierten Genauigkeiten berechnen:
print(f"Die mittlere Genauigkeit aller Modelle liegt bei {avg_acc:3.2f}%")