# 🐍 Einstieg in Python – Artikelverwaltung

Konsolenprogramm zur Artikelerfassung und Rechnungsstellung – entwickelt im Rahmen der Berufsschulausbildung zur Fachinformatikerin.

## Projektstruktur

| Datei | Beschreibung |
|---|---|
| `artikel_funktions.py` | Funktionsmodul: Eingabe, Preisliste, Berechnung |
| `artikel_hauptprogram.py` | Hauptprogramm: Schleife, Ausgabe, Gesamtrechnung |

## Funktionsumfang

Der Nutzer gibt Artikelnummern und Mengen ein. Das Programm berechnet für jeden Artikel den Positionspreis und gibt am Ende eine vollständige Rechnung mit Netto, MwSt und Brutto aus.

### Verfügbare Artikel
| Artikelnummer | Stückpreis |
|---|---|
| 17 | 2,20 € |
| 22 | 24,50 € |
| 38 | 15,00 € |
| 47 | 9,95 € |
| 125 | 12,95 € |

### Rechnungsformel
- Netto = Summe aller Positionspreise
- MwSt = Netto × 19%
- Brutto = Netto × 1,19
- DM = Brutto × 1,95583 (historischer Umrechnungskurs)

## Verwendete Python-Konzepte
- Eigene Funktionen mit Docstrings (`def`, `return`)
- Modulimport (`import artikel_funktions as a`)
- `while`-Schleife (Hauptschleife + Eingabevalidierung)
- `try` / `except` (Fehlerbehandlung)
- Dictionary (Preisliste)
- f-Strings (formatierte Ausgabe)

## Ausführen

```bash
python artikel_hauptprogram.py
```

> Voraussetzungen: Python 3.x – beide Dateien müssen im selben Ordner liegen
