# LÖSUNG
# Die Funktion "pw.parse_tests(text)" legt die im übergebenen Text beschriebene Parametrisierung der Testfälle in der Variablen "tests" ab.
tests = pw.parse_tests('''
Oberflaeche Wetter Strassentyp Verkehr Sicht   Tempomat
Teer        Sonne  Landstrasse voll    klar
Beton       Regen  Landstrasse voll    neblig
Teer        Regen  Autobahn    leer    klar
Beton       Sonne  Autobahn    leer    neblig
Beton       *      Landstrasse leer    klar
Teer        *      Autobahn    voll    neblig
''')
pw.print_tests(tests)   # Gibt die Tabelle der Testfälle aus

# Die Funktion "pw.check(parameter,tests)" überprüft, ob die in den Testfällen "tests" angegebenen Parameter-Werte-Paare vollständig sind.
# Dabei werden nur die Parameterspalten geprüft, die auch in der Parameterliste "parameter" angegeben sind!
pw.check(parameter, tests)