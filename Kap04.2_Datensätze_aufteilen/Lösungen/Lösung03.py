X = iris.drop(columns='class')   # Entfernt aus dem DataFrame die Spalte mit dem Namen 'class' (den Output)
y = iris.filter(items=['class']) # Filtert nur die Spalte 'class' heraus (also entfernt alle anderen) 