# =============================================================================
# artikel_funktions.py
# Autor: Beata Cegledi
# Beschreibung: Funktionsmodul fuer die Artikelverwaltung.
#               Enthaelt Hilfsfunktionen zur Eingabe, Preisbestimmung
#               und Preisberechnung – wird von artikel_hauptprogram.py importiert.
# =============================================================================


def menge_ok(menge):
    """
    Prueft ob die eingegebene Menge gueltig ist.
    Gueltig: ganzzahlig, positiv, maximal 1000.
    Gibt True zurueck wenn OK, sonst False.
    """
    try:
        menge = int(menge)
        if 0 < menge <= 1000:
            return True
        else:
            print("\nUngueltige Eingabe – Menge muss zwischen 1 und 1000 liegen.")
            return False
    except ValueError:
        print("\nDie Eingabe muss eine ganze Zahl sein.")
        return False


def artikel_eingabe():
    """
    Fragt den Nutzer nach einer gueltigen Artikelnummer.
    Erlaubte Nummern: 17, 22, 38, 47, 125 (oder 0 zum Beenden).
    Gibt die Artikelnummer als Integer zurueck.
    """
    erlaubt = [0, 17, 22, 38, 47, 125]
    while True:
        try:
            artikelnummer = int(input("\nArtikelnummer eingeben (0 = Beenden): "))
            if artikelnummer in erlaubt:
                return artikelnummer
            else:
                print("\nFalsche Eingabe – erlaubt sind: 17, 22, 38, 47, 125")
        except ValueError:
            print("\nBitte nur Zahlen eingeben.")


def stueckpreis(artikelnummer):
    """
    Gibt den Stueckpreis (EUR) fuer eine Artikelnummer zurueck.
    Unbekannte Artikelnummern geben 0.00 zurueck.

    Preisliste:
        17  -> 2.20 EUR
        22  -> 24.50 EUR
        38  -> 15.00 EUR
        47  -> 9.95 EUR
        125 -> 12.95 EUR
    """
    preisliste = {
        17: 2.20,
        22: 24.50,
        38: 15.00,
        47: 9.95,
        125: 12.95
    }
    return preisliste.get(int(artikelnummer), 0.00)


def preis_ermittlung(artikelnummer, menge):
    """
    Berechnet den Gesamtpreis fuer einen Artikel.
    Formel: Stueckpreis * Menge
    Gibt den Artikelgesamtpreis als Float zurueck.
    """
    return float(stueckpreis(artikelnummer)) * int(menge)
