# LÖSUNG
# Die Funktion "pw.parse_tests(text)" legt die im übergebenen Text beschriebene Parametrisierung der Testfälle in der Variablen "tests" ab.
tests = pw.parse_tests('''
Oberflaeche Wetter Strassentyp Verkehr Sicht   Tempomat
Teer        Sonne  Landstrasse voll    klar    V2.1
Beton       Regen  Landstrasse voll    neblig  V3.4
Teer        Regen  Autobahn    leer    klar    V3.4
Beton       Sonne  Autobahn    leer    neblig  V2.1
Beton       Regen  Landstrasse leer    klar    V2.1
Teer        Sonne  Autobahn    voll    neblig  V3.4
''')
pw.print_tests(tests)              # Gibt die Tabelle der Testfälle aus
pw.check(parameter, tests, verb=1) # Prüft die Paarweisen Kombinationen