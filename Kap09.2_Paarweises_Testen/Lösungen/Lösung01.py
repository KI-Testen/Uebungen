# LÖSUNG
import lib.pairwise as pw    # Importiere die Hilfsfunktionen zur Pairwise-Prüfung

# Die Funktion "pw.parse_parameters(text)" legt die Parameter und ihre möglichen Werte anhand des übergebenen Textes in der Variablen "parameter" ab.
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
pw.print_parameters(parameter)  # Gibt die Liste der Parameter und der erlaubten Werte aus