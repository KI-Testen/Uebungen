# LÖSUNG
import lib.pairwise as pw    # Importiere die Hilfsfunktionen zur Pairwise-Prüfung

# Einlesen der Parameter und Testfälle
parameter = pw.parse_parameters("Lösungen/Parameter2.csv")
pw.print_parameters(parameter)