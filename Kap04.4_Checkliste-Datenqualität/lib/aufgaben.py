# Python-Code als Lösungshilfe für die Zuordnungsaufgabe in Abschnitt 4.4
# (CC) BY-NC-SA 4.0 - Röttger, Runze, Dietrich - aus dem Buch "Basiswissen KI-Testen" ISBN 978-3-86490-947-4

aspekte = {1:"Wurden irrelevante Daten/Merkmale aus den Trainingsdaten entfernt?",
           2:"Sind die im Training verwendeten Daten so aufbereitet, dass Angreifer keine sensiblen Daten aus dem Modell ableiten oder zurückgewinnen können?",
           3:"Ist eine passende Datenvorverarbeitung für die Trainingsdaten durchgeführt worden?",
           4:"Sind meine Daten vollständig und sind alle relevanten Informationen im Datensatz vorhanden?",
           5:"Sind im Datensatz alle Szenarien/Fälle/Kategorien ausgewogen repräsentiert?",
           6:"Sind die Daten korrekt und aktuell?",
           7:"Spiegeln die Daten wider, was die KI lernen soll, oder sind die Daten durch den Zeitpunkt, den Ort oder die Umstände unfair und nicht für das Training repräsentativ?",
           8:"Werden dieselben Vorverarbeitungsschritte für die Trainingsdaten auch für den Test und den Betrieb angewendet?",
           9:"Hat der Datensatz eine ausreichende Variation in den Daten, sodass das zu erlernende Muster für das KI-basierte System erlernbar ist?",
           10:"Sind redundante Daten aus dem Datensatz entfernt?"}

auswirkungen = {"a":"Verminderte Genauigkeit", "b":"Modell mit Bias", "c":"Kompromittiertes Modell"}

antworten = {
	1: {"a":  [True,""],
		"b": [False,""],
		"c": [False,""]},
	2: {"a": [False,""],
		"b": [False,""],
		"c":  [True,""]},
	3: {"a":  [True,""],
		"b": [False,""],
		"c": [False,""]},
	4: {"a":  [True,""],
		"b":  [True,""],
		"c": [False,""]},
	5: {"a": [False,""],
		"b":  [True,""],
		"c": [False,""]},
	6: {"a":  [True,""],
		"b": [False,""],
		"c": [False,""]},
	7: {"a": [False,""],
		"b":  [True,""],
		"c": [False,""]},
	8: {"a":  [True,""],
		"b": [False,""],
		"c": [False,""]},
	9: {"a": [False,""],
		"b":  [True,""],
		"c": [False,""]},
	10:{"a": [False,""],
		"b":  [True,""],
		"c": [False,""]},
}


def antwort(qualitätsaspekt=None, auswirkung=None):
    if not qualitätsaspekt in aspekte:
        print("Du solltest als ersten Parameter die Nummer des Qualitätsaspektes eingeben an dem es mangelt. Etwa so: antwort(qualitätsaspekt=1,...)")
    elif not auswirkung in auswirkungen:
        print(f"Bitte gib als zweiten Parameter den Buchstaben einer Auswirkung (\"a\"...\"c\") an. Etwa so: antwort(qualitätsaspekt={qualitätsaspekt},auswirkung=\"c\")")
    elif antworten[qualitätsaspekt][auswirkung][0]==True:
        print("RICHTIG!")
        print(f"  Wenn der Checklistenpunkt ({qualitätsaspekt}) '{aspekte[qualitätsaspekt]}'")
        print(f"  nicht erfüllt ist, kann das die Auswirkung: ({auswirkung}) '{auswirkungen[auswirkung]}' zur Folge haben.")
        if antworten[qualitätsaspekt][auswirkung][1]:
            print("* Begründung: ",antworten[qualitätsaspekt][auswirkung][1])
    elif antworten[qualitätsaspekt][auswirkung][0]==False:
        print(f"Das ist leider falsch. Die Auswirkung bei Mängeln bei ({qualitätsaspekt}) ist nicht: '{auswirkungen[auswirkung]}'.")
        if antworten[qualitätsaspekt][auswirkung][1]:
            print("weil ",antworten[qualitätsaspekt][auswirkung][1])
    