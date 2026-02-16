
# Fehlerprüfung Menge    
def menge_ok(menge):
    try:
        menge = int(menge)
        if (menge) > 0 and (menge) < 1000:
            okay = True
        else:       
            print("\nUngültige Eingabe, Menge muss positiv sein und maximum 1000")
            okay = False    
    except ValueError:
        print("\nDie Eingabe muss eine Zahl sein")
        okay = False
    return okay

      
# Eingabe Artikelnummer
def artikel_eingabe(): 
    okay = False
    while not okay:
        try:
            artikelnummer = int(input("\nGeben Sie die Artikelnummer ein: Drücke (0) zum beenden! "))
            if artikelnummer in [0,17,22,38,47,125]:
                okay = True
            else: 
                print("\nFalsche Eingabe, nur 17, 22, 38, 47 und 125 ist erlaubt!")
        except ValueError:
            print("\nDie Eingabe muss eine Zahl sein")
    return artikelnummer
 
# Stückpreis bestimmen
def stueckpreis(an):
    an = int(an)
    if an == 17:
        preis = 2.20
    elif an == 22:
        preis = 24.50
    elif an == 38:
        preis = 15.00
    elif an == 47:
        preis = 9.95
    elif an == 125:
        preis = 12.95
    else:
        preis = 0     
    return preis    
 
#Modul 3: Ermitteln des Preises
def preis_ermittlung(artikel,stueck):
    stueck = int(stueck)
    stpreis = float(stueckpreis(artikel))
    artikelpreis = (stueck * stpreis)                 
    return artikelpreis
   