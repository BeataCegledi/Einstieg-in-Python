# 🐍 Einstieg in Python – Artikelverwaltung

> Modulares Konsolenprogramm zur Artikelerfassung und Rechnungsstellung – entwickelt im Rahmen der Berufsschulausbildung zur Fachinformatikerin Anwendungsentwicklung.

## 📋 Projektbeschreibung

Dieses Projekt besteht aus zwei Dateien und zeigt den Einsatz von **modularer Programmierung** in Python: Funktionen werden in einem separaten Modul definiert und vom Hauptprogramm importiert. Der Nutzer gibt Artikelnummern und Mengen ein; das Programm berechnet die Rechnung mit Netto, MwSt und Brutto – inklusive historischer DM-Umrechnung.

## 📁 Projektstruktur

| Datei | Rolle | Beschreibung |
|---|---|---|
| `artikel_funktions.py` | **Modul** | Enthält alle Hilfsfunktionen: Eingabevalidierung, Preisliste, Berechnung |
| `artikel_hauptprogram.py` | **Hauptprogramm** | Importiert das Modul, steuert die Hauptschleife und Ausgabe |

## 🚀 Funktionsumfang

### Verfügbare Artikel
| Artikelnummer | Stückpreis |
|---|---|
| 17 | 2,20 € |
| 22 | 24,50 € |
| 38 | 15,00 € |
| 47 | 9,95 € |
| 125 | 12,95 € |

### Rechnungsformel
| Position | Berechnung |
|---|---|
| Netto | Summe aller Positionspreise |
| MwSt | Netto × 19% |
| Brutto | Netto × 1,19 |
| DM-Betrag | Brutto × 1,95583 (historischer Kurs) |

## 🧠 Verwendete Python-Konzepte

| Konzept | Anwendung im Projekt |
|---|---|
| Eigene Funktionen | `def` mit Parametern, `return`, Docstrings |
| Modulimport | `import artikel_funktions as a` |
| `while`-Schleife | Hauptschleife + Eingabevalidierung |
| `try` / `except` | Fehlerbehandlung bei Nutzereingaben |
| Dictionary | Preisliste als Key-Value-Struktur |
| f-Strings | Formatierte, ausgerichtete Rechnungsausgabe |

## ▶️ Ausführen

```bash
python artikel_hauptprogram.py
```

> **Voraussetzungen:** Python 3.x · Beide Dateien müssen im selben Ordner liegen

## 👩‍💻 Über die Entwicklerin

Dieses Projekt demonstriert mein Verständnis von **modularer Programmierung**: Code sinnvoll aufteilen, Funktionen mit Docstrings dokumentieren und Module importieren – eine wichtige Grundlage für größere Softwareprojekte.
