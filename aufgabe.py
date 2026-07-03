import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np


def initialisiere_proben():
    proben = [
        (101, "Granit_A1", 2.7, 150.5),
        (102, "Kalkstein_B2", 2.4, 80.2),
        (103, "Basalt_C3", 3.0, 200.0),
        (104, "Sandstein_D4", 2.2, 50.0),
        (105, "Schiefer_E5", 2.8, 120.3),
        (106, "Gneis_F6", 2.9, 180.7),
        (107, "Quarzit_G7", 2.6, 90.1),
        (108, "Tonstein_H8", 2.1, 40.5),
        (109, "Marmor_I9", 2.5, 110.0),
        (110, "Konglomerat_J10", 2.3, 70.2),
    ]
    return proben


def berechne_durchschnittliche_dichte(proben):
    dichten = np.array([p[2] for p in proben])
    return np.mean(dichten)


def bubble_sort(proben):
    n = len(proben)
    vertauschungen = 0
    for i in range(n):
        getauscht = False
        for j in range(0, n - i - 1):
            if proben[j][2] > proben[j + 1][2]:
                proben[j], proben[j + 1] = proben[j + 1], proben[j]
                vertauschungen += 1
                getauscht = True
        if not getauscht:
            break
    return proben, vertauschungen


def gebe_sortierte_proben_aus(proben):
    print("\nSortierte Proben (aufsteigend nach Dichte):")
    for position, probe in enumerate(proben, start=1):
        print(f"{position}. {probe[1]} – Dichte: {probe[2]} g/cm³, Tiefe: {probe[3]} m")


def visualisiere_dichteverteilung(proben):
    proben_namen = [p[1] for p in proben]
    dichten = [p[2] for p in proben]
    plt.bar(proben_namen, dichten)
    plt.title("Dichteverteilung der Bohrkernproben")
    plt.xlabel("Probenname")
    plt.ylabel("Dichte (g/cm³)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("dichteverteilung.png")
    print("Visualisierung gespeichert: dichteverteilung.png")


def suche_proben_nach_dichte(proben):
    dichte_zu_name = {}
    for p in proben:
        dichte = p[2]
        if dichte not in dichte_zu_name:
            dichte_zu_name[dichte] = []
        dichte_zu_name[dichte].append(p[1])
    eingabe = input("Gib eine Dichte in g/cm³ ein: ")
    try:
        gesuchte_dichte = float(eingabe)
    except ValueError:
        print(f"Ungültige Eingabe: '{eingabe}' ist keine Zahl.")
        return
    if gesuchte_dichte in dichte_zu_name:
        namen = dichte_zu_name[gesuchte_dichte]
        print(f"Proben mit Dichte {gesuchte_dichte} g/cm³: {', '.join(namen)}")
    else:
        print(f"Keine Probe mit Dichte {gesuchte_dichte} g/cm³ gefunden.")


def main():
    print("Willkommen zum Dichteanalyse-Programm!")
    proben = initialisiere_proben()
    durchschnitt = berechne_durchschnittliche_dichte(proben)
    print(f"Durchschnittliche Dichte aller Proben: {durchschnitt:.2f} g/cm³")

    sortierte_proben, anzahl_tausche = bubble_sort(proben)
    gebe_sortierte_proben_aus(sortierte_proben)
    print(f"\nAnzahl der Vertauschungen: {anzahl_tausche}")

    visualisiere_dichteverteilung(sortierte_proben)

    suche_proben_nach_dichte(sortierte_proben)


if __name__ == "__main__":
    main()
