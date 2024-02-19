# Python-Code als Lösungshilfe für die Zuordnungsaufgabe in Abschnitt 3.3
# (CC) BY-NC-SA 4.0 - Röttger, Runze, Dietrich - aus dem Buch "Basiswissen KI-Testen" ISBN 978-3-86490-947-4

szenarien = {1:"Es soll ein Algorithmus trainiert werden, der verdorbenes Obst erkennt. Dafür steht ein mit den Klassen verdorben und nicht-verdorben (Kennzeichen-Ausgabe) korrekt gekennzeichneter/annotierter Datensatz Obstbildern zur Verfügung.",
             2:"Ein Algorithmus soll in einem strategischen Spiel seine Züge entsprechend der gegnerischen Spielstrategie so anpassen, dass er gewinnt.",
             3:"Es soll ein Algorithmus trainiert werden, der aufgrund der Berufserfahrung in Jahren das Gehalt als numerische und kontinuierliche Ausgabe in Euro ermittelt.",
             4:"Es soll ein Datensatz mit Informationen zum Inhalt der Warenkörbe von Kunden analysiert werden, ohne dass eine vorformulierte Ausgabe vorgesehen ist. Es sollen anhand von gemeinsam auftretenden Merkmalen Beziehungen und Abhängigkeiten abgeleitet werden.",
             5:"Ein Algorithmus soll Zelltypen aus einer Biopsie anhand der Genexpression in die zwei diskreten Kategorien entartete Zelle und nicht-entartete Zelle sortieren.",
             6:"Ein Datensatz enthält Kundeninformationen zum Kaufverhalten, die nach Kundentyp gruppiert werden sollen.",
             7:"Eine intelligente Raumklimaregulierung in einem Großraumbüro passt durch die Parameter Temperatur, Luftfeuchtigkeit und Jalousien das Raumklima so an, dass möglichst viele Mitarbeiter das Raumklima positiv bewerten."}

mlarten = {"A":"Regression", "B":"Klassifikation", "C":"Clustering", "D":"Assoziation", "E":"Bestärkendes Lernen"}

antworten = { 1: {
    "A": [False,"um welche Art der Ausgabe es sich hier handelt!"],
    "B":  [True,"Für das Training des Algorithmus ist ein Datensatz vorhanden, der zudem gekennzeichnet ist. Daher können wir überwachtes Lernen anwenden. Da die Ausgaben des Algorithmus eine eingegrenzte Menge unterscheidbarer Klassen (verdorben, nicht-verdorben) ist, handelt es sich um eine Klassifikation."],
    "C": [False,"ob es sich um eine Form des überwachten oder des unüberwachten Lernens handelt!"],
    "D": [False,"ob es sich um eine Form des überwachten oder des unüberwachten Lernens handelt!"],
    "E": [False,"ob die Definition des bestärkenden Lernens passt! Bestärkendes Lernen: Die Erstellung eines ML-Modells durch einen Prozess des Ausprobierens und Belohnens, um ein Ziel zu erreichen [ISO/IEC TR 29119-11]."]},
             2: {
    "A": [False,"um welche Art des Lernens es hier geht!"],
    "B": [False,"um welche Art des Lernens es hier geht!"],
    "C": [False,"um welche Art des Lernens es hier geht!"],
    "D": [False,"um welche Art des Lernens es hier geht!"],
    "E":  [True,"Beim Training des Algorithmus soll eine Strategie entwickelt werden, um das Spiel zu gewinnen. Die Spielregeln und das Verhalten des Gegners stellen dabei eine definierte Umgebung dar, mit der der Algorithmus interagieren kann. Die Belohnungsfunktion wird durch das Gewinnen des Spiels definiert. Strategische Spiele sind klassische Beispiele für das bestärkende Lernen."]},
             3: {
    "A":  [True,"Da es sich hier um einen Algorithmus handelt, der einen numerischen und kontinuierlichen Zusammenhang darzustellen soll, handelt es sich um Regression. Hierbei wird angenommen, dass ein Datensatz mit dem Gehalt in Abhängigkeit von den Berufsjahren vorliegt (überwachtes Lernen). Beim überwachten Lernen unterscheidet sich Regression von Klassifikation dadurch, dass bei der Regression kontinuierliche Daten als Ausgabe erzeugt werden, während bei der Klassifikation eine diskrete und kategoriale Ausgabe vorgesehen ist."],
    "B": [False,"um welche Art der Ausgabe es sich hier handelt!"],
    "C": [False,"ob es sich um eine Form des überwachten oder des unüberwachten Lernens handelt!"],
    "D": [False,"ob es sich um eine Form des überwachten oder des unüberwachten Lernens handelt!"],
    "E": [False,"ob die Definition des bestärkenden Lernens passt! Bestärkendes Lernen: Die Erstellung eines ML-Modells durch einen Prozess des Ausprobierens und Belohnens, um ein Ziel zu erreichen [ISO/IEC TR 29119-11]."]},
             4: {
    "A": [False,"ob es sich um eine Form des überwachten oder des unüberwachten Lernens handelt!"],
    "B": [False,"ob es sich um eine Form des überwachten oder des unüberwachten Lernens handelt!"],
    "C": [False,"ob es wirklich um die Gruppierung von Warenkörben geht, oder eher um die Analyse von Zusammenhängen zwischen verschiedenen Variablen, die einen Warenkorb beschreiben."],
    "D":  [True,"Da keine vordefinierte Ausgabe vorliegt, handelt es sich hier um eine Form des unüberwachten Lernens. Da hier Beziehungen und Abhängigkeiten abgeleitet werden sollen (z. B. in Form von Regeln wie \"Warenkörbe, die Produkt A enthalten, enthalten auch oft Produkt B\"), handelt es sich um Assoziation. Es handelt sich nicht um Clusterbildung, da es hier nicht um die Gruppierung von Warenkörben geht, sondern um die Analyse von Zusammenhängen zwischen verschiedenen Variablen, die einen Warenkorb beschreiben."],
    "E": [False,"ob die Definition des bestärkenden Lernens passt! Bestärkendes Lernen: Die Erstellung eines ML-Modells durch einen Prozess des Ausprobierens und Belohnens, um ein Ziel zu erreichen [ISO/IEC TR 29119-11]."]},
             5: {
    "A": [False,"um welche Art der Ausgabe es sich hier handelt!"],
    "B":  [True,"Für den Algorithmus sind hier zwei voneinander klar abgegrenzte (diskrete und kategoriale) Ausgabeklassen vorgesehen. Daher handelt es sich um eine Klassifikation. Hierbei wird angenommen, dass ein gekennzeichneter Datensatz zum Training und Test vorliegt (überwachtes Lernen)."],
    "C": [False,"ob es sich um eine Form des überwachten oder des unüberwachten Lernens handelt!"],
    "D": [False,"ob es sich um eine Form des überwachten oder des unüberwachten Lernens handelt!"],
    "E": [False,"ob die Definition des bestärkenden Lernens passt! Bestärkendes Lernen: Die Erstellung eines ML-Modells durch einen Prozess des Ausprobierens und Belohnens, um ein Ziel zu erreichen [ISO/IEC TR 29119-11]."]},
             6: {
    "A": [False,"um welche Art der Ausgabe es sich hier handelt!"],
    "B": [False,"ob Ausgabe wirklich diskret und kategorial ist!"],
    "C":  [True,"Hier geht es darum, ähnliche Datenpunkte zu Gruppen (Clustern) zusammenzufassen. Die Gruppen sind nicht vorgegeben, daher handelt es sich um eine Form des unüberwachten Lernens und nicht um eine Klassifikation."],
    "D": [False,"ob wirklich Beziehungen und Abhängigkeiten abgeleitet werden sollen!"],
    "E": [False,"ob die Definition des bestärkenden Lernens passt! Bestärkendes Lernen: Die Erstellung eines ML-Modells durch einen Prozess des Ausprobierens und Belohnens, um ein Ziel zu erreichen [ISO/IEC TR 29119-11]."]},
             7: {
    "A": [False,"um welche Art des Lernens es hier geht!"],
    "B": [False,"um welche Art des Lernens es hier geht!"],
    "C": [False,"um welche Art des Lernens es hier geht!"],
    "D": [False,"um welche Art des Lernens es hier geht!"],
    "E": [True,"Hier wird ein Algorithmus gesucht, der durch Interaktionen mit der Umgebung (Anpassen von Raumparametern) das Raumklima so verändern soll, dass es positiv bewertet wird. Die Belohnungsfunktion wird durch die Bewertung der Mitarbeiter bereitgestellt. Wenn in der Szenariobeschreibung historische Daten erwähnt worden wären, wäre auch ein Optimierungsalgorithmus des überwachten Lernens eine gute Wahl."]}}


def antwort(szenario=None, mlart=None):
    if not szenario in szenarien:
        print("Du solltest als ersten Parameter die Nummer eines Szenarios eingeben, etwa so: antwort(szenario=1,...)")
    elif not mlart in mlarten:
        print(f"Bitte gib als zweiten Parameter den Buchstaben der ML-Art (\"A\"...\"E\") an. Etwa so: antwort(szenario={szenario},mlart=\"A\")")
    elif antworten[szenario][mlart][0]==True:
        print(f"RICHTIG!")
        if antworten[szenario][mlart][1]:
            print("* Szenario:", szenarien[szenario])
            print("  Die ML-Art ist '{0}'".format(mlarten[mlart]))
            print("* Begründung:",antworten[szenario][mlart][1])
    elif antworten[szenario][mlart][0]==False:
        print("Das ist leider falsch. Das Szenario ist nicht '{0}'.".format(mlarten[mlart]))
        if antworten[szenario][mlart][1]:
            print("Überlege noch einmal,",antworten[szenario][mlart][1])
    