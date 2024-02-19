from sklearn.model_selection import train_test_split   # importiere diese Methode aus der Bibliothek scikit-learn 

X_trainval, X_test, y_trainval, y_test = train_test_split( X, y, test_size=0.1, random_state=4 )