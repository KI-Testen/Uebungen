import joblib as jl     # wir benötigen die joblib um das Modell zu laden

model = jl.load("../Kap04.2_Datensätze_aufteilen/modell-8.pkl")
#model = jl.load("data/modell-8.pkl") # alternatives Modell, wenn du Übung 4.2 nicht bis zum Ende abgeschlossen hast.
model