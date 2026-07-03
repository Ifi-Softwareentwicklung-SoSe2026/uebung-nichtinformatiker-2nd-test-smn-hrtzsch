# Bohrkernproben mit Python analysieren

Diese Datei dient der Middleware als strukturierte Grundlage fuer die automatisch erzeugten Issues von Maria. Die ausfuehrliche fachliche Beschreibung steht in `README.md`.

Die Uebung ist bewusst in mehrere kleine Pull Requests aufgeteilt. Nach jedem erfolgreichen Merge erstellt Maria automatisch das naechste Issue. Bearbeite jeden Part auf einem eigenen Branch und verknuepfe den PR mit `Closes #<Issue-Nummer>`.

# Part 1 -- Datenmodell und durchschnittliche Dichte

<!-- agent-assignment-part:{"kind":"python","required_checks":["workflow:.github/workflows/python-run.yml"]} -->

Implementiere in `aufgabe.py` den Einstieg in das Dichteanalyse-Programm.

Aufgaben:

- Lege eine `main()`-Funktion an oder nutze die vorhandene `main()`-Funktion weiter.
- Erstelle eine eigene Funktion zur Dateninitialisierung, z. B. `initialisiere_proben()`.
- Die Funktion soll eine Liste von Tupeln mit allen zehn Bohrkernproben aus der `README.md` zurueckgeben.
- Jedes Tupel enthaelt ID, Name, Dichte und Tiefe.
- Importiere NumPy und berechne die durchschnittliche Dichte in einer eigenen Funktion, z. B. `berechne_durchschnittliche_dichte(proben)`.
- Gib die durchschnittliche Dichte in `main()` nachvollziehbar aus.
- Das Programm muss mit `python aufgabe.py` ohne Fehler laufen.

Akzeptanzkriterien:

- `aufgabe.py` enthaelt eine `main()`-Funktion.
- Die zehn vorgegebenen Proben sind als Liste von Tupeln angelegt.
- NumPy wird verwendet, insbesondere `np.mean()`.
- Der Workflow `.github/workflows/python-run.yml` ist erfolgreich.

# Part 2 -- Bubble Sort und formatierte Ausgabe

<!-- agent-assignment-part:{"kind":"python","required_checks":["workflow:.github/workflows/python-run.yml"]} -->

Erweitere deine Loesung um die Sortierung der Bohrkernproben nach Dichte.

Aufgaben:

- Schreibe eine eigene Funktion `bubble_sort(proben)`.
- Sortiere die Proben aufsteigend nach der Dichte.
- Verwende Bubble Sort: Vergleiche benachbarte Elemente und vertausche sie bei Bedarf.
- Beende den Algorithmus, sobald in einem Durchlauf kein Tausch mehr notwendig ist.
- Gib die sortierten Proben in einer eigenen Ausgabefunktion formatiert aus.
- Nutze fuer die Positionsnummerierung `enumerate()` und fuer die Ausgabe f-Strings.
- Bonus: Gib zusaetzlich die Anzahl der Vertauschungen aus.

Akzeptanzkriterien:

- Die Sortierung erfolgt aufsteigend nach Dichte.
- Die Sortierung ist als Bubble-Sort-Logik erkennbar und nutzt benachbarte Vertauschungen.
- Die Ausgabe zeigt alle zehn Proben in sortierter Reihenfolge.
- `enumerate()` und f-Strings werden sinnvoll verwendet.
- Der Workflow `.github/workflows/python-run.yml` ist erfolgreich.

# Part 3 -- Visualisierung mit Matplotlib

<!-- agent-assignment-part:{"kind":"python","required_checks":["workflow:.github/workflows/python-run.yml"]} -->

Erweitere das Programm um eine einfache Visualisierung der Dichteverteilung.

Aufgaben:

- Importiere `matplotlib.pyplot`.
- Erstelle eine eigene Funktion fuer die Visualisierung, z. B. `visualisiere_dichteverteilung(proben)`.
- Erzeuge ein Balkendiagramm mit `plt.bar()`.
- Die X-Achse zeigt die Probennamen.
- Die Y-Achse zeigt die Dichte.
- Der Plot besitzt den Titel `Dichteverteilung der Bohrkernproben`.
- Drehe die X-Beschriftungen, damit sie lesbar bleiben, z. B. mit `plt.xticks(rotation=45)`.
- Speichere den Plot in eine Datei, z. B. `dichteverteilung.png`, statt ein interaktives Fenster zu erwarten.

Akzeptanzkriterien:

- Das Programm laeuft im GitHub-Workflow ohne grafische Oberflaeche.
- Es wird ein Matplotlib-Balkendiagramm erzeugt.
- Achsen und Titel sind fachlich korrekt beschriftet.
- Die Visualisierung ist in einer eigenen Funktion gekapselt.
- Der Workflow `.github/workflows/python-run.yml` ist erfolgreich.

# Part 4 -- Interaktive Suche nach Dichte

<!-- agent-assignment-part:{"kind":"python","required_checks":["workflow:.github/workflows/python-run.yml"]} -->

Erweitere das Programm abschliessend um eine interaktive Suche nach Proben mit einer bestimmten Dichte.

Aufgaben:

- Erstelle ein Dictionary `dichte_zu_name` oder eine vergleichbare Struktur.
- Die Dichte ist der Schluessel; der Wert ist eine Liste der Probennamen mit dieser Dichte.
- Nutze `input()`, um eine Dichte vom Benutzer abzufragen.
- Wandle die Eingabe sinnvoll in eine Zahl um.
- Gib alle Proben mit dieser Dichte aus.
- Falls die Dichte nicht existiert, gib eine verstaendliche Meldung aus.
- Achte darauf, dass die bisherigen Funktionen aus Part 1 bis 3 weiterhin funktionieren.

Akzeptanzkriterien:

- Die Suche nutzt ein Dictionary.
- Vorhandene Dichten liefern alle passenden Probennamen.
- Nicht vorhandene Dichten werden sinnvoll behandelt.
- Das Programm bleibt modular: Daten, Durchschnitt, Sortierung, Ausgabe, Visualisierung und Suche sind getrennt.
- Der Workflow `.github/workflows/python-run.yml` ist erfolgreich und nutzt die bereitgestellte Testeingabe.
