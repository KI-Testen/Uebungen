RP = 161
RN = 593
FP = 2
FN = 14
n = RP+RN+FP+FN
Genauigkeit  = (RP+RN)/n
Präzision    = RP/(RP+FP)
Sensitivität = RP/(RP+FN)
F1_Wert      = 2*(Präzision*Sensitivität)/(Präzision+Sensitivität)
print(f"die Genauigkeit ist {Genauigkeit*100:3.2f}%")
print(f"die Präzision ist {Präzision*100:3.2f}%")
print(f"die Sensitivität ist {Sensitivität*100:3.2f}%")
print(f"die F1-Wert ist {F1_Wert*100:3.2f}%")