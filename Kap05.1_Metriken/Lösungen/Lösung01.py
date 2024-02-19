Genauigkeit  = (52+110)/193
Präzision    = 52/(52+8)
Sensitivität = (52)/(52+23)
F1_Wert      = 2*(Präzision*Sensitivität)/(Präzision+Sensitivität)
print(f"die Genauigkeit ist {Genauigkeit*100:3.2f}%")
print(f"die Präzision ist {Präzision*100:3.2f}%")
print(f"die Sensitivität ist {Sensitivität*100:3.2f}%")
print(f"der F1-Wert ist {F1_Wert*100:3.2f}%")