data1, meta1 = arff.loadarff('Data/NASA bug data 1.arff') # NASA bug data 1 laden
df1 = pd.DataFrame(data1)
data2, meta2 = arff.loadarff('Data/NASA bug data 2.arff') # NASA bug data 2 laden
df2 = pd.DataFrame(data2)
data3, meta3 = arff.loadarff('Data/NASA bug data 3.arff') # NASA bug data 3 laden
df3 = pd.DataFrame(data3)

print(df1.shape) # Dimensionen (Instanzen und Attribute) anzeigen
print(df2.shape)
print(df3.shape)