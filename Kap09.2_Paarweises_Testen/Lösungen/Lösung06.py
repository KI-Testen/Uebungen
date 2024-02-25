# LÖSUNG
# Prüfe die vom Tool erzeugten Testfälle, ob diese vollständig sind.
tests = pw.parse_tests("Lösungen/Testfälle2.csv")
#pw.print_tests(tests)
pw.check(parameter, tests, verb=3)