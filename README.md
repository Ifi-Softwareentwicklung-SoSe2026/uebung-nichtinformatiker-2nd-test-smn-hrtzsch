<!--
author:   Volker Göhler
version:  0.1.1
language: de
narrator: Deutsch Female
edit: true
comment:  Übung Python für Nicht-Informatiker
-->

[![LiaScript Course](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/Ifi-Softwareentwicklung-SoSe2026/Uebung_NichtInformatiker/refs/heads/main/README.md)

> Hinweis: Der Badge-Link zeigt auf den Branch `main`. Für andere Branches einfach `refs/heads/main` in der URL durch `refs/heads/<branch-name>` ersetzen. Wird das Repository umbenannt oder verschoben, muss die URL im Badge entsprechend angepasst werden.

# Aufgabe 03 – Python für Nicht-Informatiker

Softwareentwicklung SoSe2026
============================

## Lernziele dieser Übung

In dieser Übung bearbeitest du ein durchgehendes Python-Szenario zur Auswertung einfacher Missions- und Messdaten. Dabei sollen folgende Inhalte aktiv genutzt werden:

- Operationen (`+`, `-`, `*`, `/`, `%`, `**`, logische Operatoren wie `and`/`or`)
- `type()`
- `input()`
- `if`, `elif`, `else`
- `while`, `for` mit `in range(...)`
- Listen inklusive `zip()`, `enumerate()`, `split("-")`, `liste.index(element)`
- Dictionaries inklusive `element in dictionary`
- Tupel
- Funktionen/Methoden (auch mit zwei Rückgabewerten)
- Libraries verwenden (`import ...`)
- NumPy: Arrays, `loadtxt`, `reshape`, `linspace`, `arange`
- Matplotlib (`matplotlib.pyplot`) für einfache Plots

## 📌 Allgemeine Vorgehensweise

1. Arbeite mit deinem GitHub-Classroom-Repository.
2. Lege einen Branch `integration` an.
3. Erstelle für jede Teilaufgabe kleine, nachvollziehbare Commits.
4. Öffne einen Pull Request nach `main` und arbeite Review-Kommentare ein.
5. Führe den PR nach Freigabe zusammen (`merge`).

## 🛠️ Aufgabe 0: Git und GitHub kennenlernen

Dimensionen
==========

| Dimension | Werkzeuge & Features |
|-----------|----------------------|
| **Lokal** (VS Code + Git) | clone, add/stage, commit, branch/switch, merge, Konflikte lösen |
| **Remote** (GitHub) | push/pull, Pull Requests, Review-Kommentare einarbeiten, Issues |

### 🔧 Lokale Git-Arbeit (kurz)

1. Repository klonen (kopiert den Remote-Stand auf den lokalen Rechner)
2. Branch `integration` erstellen und wechseln (`git switch -c integration`)
3. Änderungen committen (aussagekräftige Commit-Message) (`git add .` + `git commit -m "..."`)
4. Branch pushen (`git push -u origin integration`)
5. Pull Request auf GitHub erstellen

### 🌐 Direkt auf GitHub im Webportal (Remote-only)

Diese Variante nutzt **kein lokales Git**. Alles passiert direkt auf github.com.

1. Öffne dein Repository im Browser.
2. Erstelle über die Branch-Auswahl einen neuen Branch (z. B. `webportal-edit`).
3. Öffne eine Datei und nutze den Web-Editor (Stift-Symbol), um Änderungen vorzunehmen.
4. Committe direkt im Browser auf deinen Branch.
5. Erstelle über **Pull request** einen PR nach `main` (Button: Compare & pull request).
6. Reagiere auf Review-Kommentare direkt im PR (Antworten + neue Web-Commits).
7. Merge den PR nach Freigabe.

## Agenten

- Maria ist ein Senior Developer der euch Issues generiert hat, die ihr bearbeiten sollt. Text dazu ist der Vollständigkeit halber in diesem Dokument enthalten. Maria könnt ihr mit `/help` ansprechen, um weitere Informationen zu erhalten (im Kommentarfeld). Wenn ihr ein Issue bearbeitet hat wird gegebenfalls ein weiteres Issue von Maria erstellt, das auf eure Lösung aufbaut.
- Lisa ist ein Tester der eure Lösung auf Korrektheit überprüft. Sie wird eure PRs testen und ggf. Review-Kommentare hinterlassen.

## Aufgabe: Sortieren von Bohrkernproben nach Dichte

In einem Bergbaubetrieb wurden mehrere Bohrkernproben entnommen. Jede Probe hat eine ID, einen Namen (z. B. "Granit_A1"), eine Dichte (in g/cm³) und eine Tiefe (in Metern). Die Proben sollen nach ihrer Dichte sortiert werden, um sie in einem Lager optimal anzuordnen. Nutze Bubble Sort, um die Proben in aufsteigender Reihenfolge zu sortieren.

Schreibe das Program in Python in die Datei `aufgabe.py` und implementiere die folgenden Schritte in eigenen Funktionen. Die Funktionen sollen in der main Funktion aufgerufen werden. Das Program kann mit `python aufgabe.py` gestartet werden.

### Schritt 1: Dateninitialisierung

Erstelle eine Liste von Tupeln, wobei jedes Tupel die Daten einer Bohrkernprobe enthält:

| ID | Name | Dichte (g/cm³) | Tiefe (m) |
| --- | --- | --- | --- |
| 101 | Granit_A1 | 2.7 | 150.5 |
| 102 | Kalkstein_B2 | 2.4 | 80.2 |
| 103 | Basalt_C3 | 3.0 | 200.0 |
| 104 | Sandstein_D4 | 2.2 | 50.0 |
| 105 | Schiefer_E5 | 2.8 | 120.3 |
| 106 | Gneis_F6 | 2.9 | 180.7 |
| 107 | Quarzit_G7 | 2.6 | 90.1 |
| 108 | Tonstein_H8 | 2.1 | 40.5 |
| 109 | Marmor_I9 | 2.5 | 110.0 |
| 110 | Konglomerat_J10 | 2.3 | 70.2 |

### Schritt 2: Berechnung der durchschnittlichen Dichte

Nutze NumPy, um die Dichten in ein Array umzuwandeln und die durchschnittliche Dichte aller Proben zu berechnen.
Hinweis: Nutze `np.mean()`.


### Schritt 3: Implementierung von Bubble Sort

Schreibe eine Funktion `bubble_sort(proben)`, die die Liste der Bohrkernproben nach Dichte aufsteigend sortiert.

Bubble Sort ist ein einfacher Sortieralgorithmus, der eine Liste schrittweise durchläuft und benachbarte Elemente vertauscht, wenn sie in der falschen Reihenfolge stehen. Der Name kommt daher, dass kleine Werte (wie Luftblasen im Wasser) nach oben "aufsteigen", während große Werte nach unten "absinken".


Visualisierung des Algorithmus
-------------------

Stell dir vor, du hast eine Reihe von Bohrkernproben in einem Regal, die nach Dichte sortiert werden sollen:

Erster Durchlauf:
--------------

Du beginnst bei der ersten Probe und vergleichst sie mit der zweiten.
Falls die erste Probe eine höhere Dichte hat als die zweite, tauschst du sie.
Das wiederholst du für alle benachbarten Proben bis zum Ende des Regals.
Nach dem ersten Durchlauf ist die Probe mit der höchsten Dichte ganz rechts im Regal.


Zweiter Durchlauf:
----------------

Jetzt ignorierst du die letzte Probe (sie ist bereits sortiert) und wiederholst den Vorgang.
Nach diesem Durchlauf ist die zweithöchste Dichte an der vorletzten Position.


Weiter so, bis keine Vertauschungen mehr nötig sind:
--------------------------

Irgendwann durchläuft der Algorithmus die Liste, ohne eine einzige Vertauschung durchzuführen.
Dann ist das Regal vollständig sortiert.


Zusammenfassung der Logik
=========================

- Laufe über die Liste der Proben.
- Solange die Liste nicht sortiert ist:

- Gehe durch die Liste
- Vergleiche benachbarte Elemente
- Tausche sie, falls nötig
- Merke dir, ob ein Tausch stattgefunden hat

- Falls kein Tausch stattfand: Beende die Schleife
- Gib die sortierte Liste zurück


**Bonus:** Erweitere die Funktion so, dass sie zwei Rückgabewerte liefert:

- Die sortierte Liste.
- Die Anzahl der durchgeführten Vertauschungen.


### Schritt 4: Datenausgabe

Gib die sortierten Proben in einem formatierten String aus. Nutze f-Strings und `enumerate()`, um die Position jeder Probe in der sortierten Liste anzuzeigen.

### Schritt 5: Visualisierung der Dichteverteilung

Nutze Matplotlib, um ein Balkendiagramm der Dichten zu erstellen:

- X-Achse: Name der Probe.
- Y-Achse: Dichte.
- Titel: "Dichteverteilung der Bohrkernproben".
- Nutze `plt.bar()` und `plt.xticks(rotation=45)`.

### Schritt 6: Interaktive Abfrage der Dichte

1. Erstelle ein Dictionary `dichte_zu_name`, das die Dichte als Schlüssel und eine Liste der Probennamen mit dieser Dichte als Wert enthält.
2. Nutze `input()`, um den Benutzer nach einer Dichte zu fragen, und gib alle Proben mit dieser Dichte aus. Falls die Dichte nicht existiert, gib eine Fehlermeldung aus.

## ✅ Akzeptanzkriterien

- Der Code läuft ohne Fehler.
- Jede logische Unteraufgabe ist in einer eigenen Funktion implementiert.
- Es gibt mindestens einen Plot mit beschrifteten Achsen.
- Der Workflow mit Pull Request und Review ist dokumentiert bzw. durchgeführt.
