# =============================================================================
# artikel_hauptprogram.py
# Autor: Beata Cegledi
# Beschreibung: Hauptprogramm fuer die Artikelkasse.
#               Importiert Funktionen aus artikel_funktions.py.
#               Der Nutzer gibt Artikel ein, bis er 0 drueckt.
#               Am Ende: Netto, MwSt und Brutto-Ausgabe (inkl. DM-Umrechnung).
# =============================================================================

import artikel_funktions as a
import os

# --- Initialisierung ---
gesammtnetto = 0.0  # Summe aller Artikelpreise (netto)
artikel = 1         # Startwert (wird sofort durch Eingabe ersetzt)

os.system("cls")  # Konsole leeren

# =============================================================================
# HAUPTSCHLEIFE – Artikel hinzufuegen bis Artikelnummer 0 eingegeben wird
# =============================================================================
while artikel != 0:

    # Artikelnummer einlesen (Funktion aus Modul)
    artikel = a.artikel_eingabe()

    if artikel == 0:
        break  # Eingabe beendet

    # Menge einlesen und validieren (Funktion aus Modul)
    ok = False
    while not ok:
        menge = input("\nGewuenschte Menge eingeben: ")
        ok = a.menge_ok(menge)

    # Preise berechnen (Funktionen aus Modul)
    artikelpreis = a.preis_ermittlung(artikel, menge)
    preis = a.stueckpreis(artikel)

    # Gesamtnetto aktualisieren
    gesammtnetto += artikelpreis

    # Hinzugefuegten Artikel ausgeben
    print("\n", "*" * 40)
    print(f"Hinzugefuegt: Artikel {artikel} | Menge: {menge} Stk | Stueckpreis: {preis:5.2f} EUR | Preis: {artikelpreis:7.2f} EUR")
    print("*" * 40, "\n")

# =============================================================================
# GESAMTRECHNUNG – Netto, MwSt (19%), Brutto und Umrechnung in DM
# =============================================================================
mwst = round(gesammtnetto * 0.19, 2)
brutto = round(gesammtnetto * 1.19, 2)
dm = round(brutto * 1.95583, 2)  # Historischer EUR → DM Kurs

print("\n" + "=" * 50)
print(f"\n  Nettobetrag:              {gesammtnetto:>10.2f} EUR")
print(f"  Mehrwertsteuer (19%):     {mwst:>10.2f} EUR")
print(f"  Bruttobetrag:             {brutto:>10.2f} EUR")
print(f"\n  (Bruttobetrag in DM:      {dm:>10.2f} DM)")
print("\n" + "=" * 50 + "\n")
