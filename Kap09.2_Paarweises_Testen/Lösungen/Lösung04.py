# LÖSUNG mit nur 6 Testfällen
import lib.pairwise as pw    # Importiere die Hilfsfunktionen zur Pairwise-Prüfung

# Die Funktion "pw.parse_parameters(text)" legt die Parameter un ihre möglichen Werte anhand des übergebenen Textes in der Variablen "parameter" ab.
parameter = pw.parse_parameters('''
Oberflaeche: Teer, Beton
Wetter:      Sonne, Regen
Strassentyp: Landstrasse, Autobahn
Verkehr:     voll, leer
Sicht:       klar, neblig
Tempomat:    V2.1, V3.4
SH-Ass:      V1.0
SW-Ass:      V2.3, V2.3.3
''')

# Die Funktion "pw.parse_tests(text)" legt die im übergebenen Text beschriebene Parametrisierung der Testfälle in der Variablen "tests" ab.
tests = pw.parse_tests('''
TF Oberflaeche Wetter Strassentyp Verkehr Sicht   Tempomat SH-Ass SW-Ass
1  Teer        Sonne  Landstrasse voll    klar    V2.1     V1.0   V2.3
2  Beton       Regen  Landstrasse voll    neblig  V3.4     V1.0   V2.3
3  Teer        Regen  Autobahn    leer    klar    V3.4     V1.0   V2.3
4  Beton       Sonne  Autobahn    leer    neblig  V2.1     V1.0   V2.3.3
5  Beton       Regen  Landstrasse leer    klar    V2.1     V1.0   V2.3.3
6  Teer        Sonne  Autobahn    voll    neblig  V3.4     V1.0   V2.3.3
''')
pw.print_tests(tests)   # Gibt die Tabelle der Testfälle aus

# Die Funktion "pw.check(parameter,tests)" überprüft, ob die in den Testfällen "tests" angegebenen Parameter-Werte-Paare vollständig sind.
# Dabei werden nur die Parameterspalten geprüft, die auch in der Parameterliste "parameter" angegeben sind!
pw.check(parameter, tests, verb=2)