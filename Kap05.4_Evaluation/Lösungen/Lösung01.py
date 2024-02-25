### Genauigkeit (engl. accuracy) = (RP + RN) / (RP + FP + RN + FN)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true = y_test, y_pred = y_pred)
print("Genauigkeit: ", accuracy)