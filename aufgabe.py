import matplotlib
matplotlib.use('Agg')

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


def main():
    print("Willkommen zum Dichteanalyse-Programm!")
    proben = initialisiere_proben()
    durchschnitt = berechne_durchschnittliche_dichte(proben)
    print(f"Durchschnittliche Dichte aller Proben: {durchschnitt:.2f} g/cm³")


if __name__ == "__main__":
    main()
