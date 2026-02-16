import artikel_funktions as a
import os
gesammtnetto = 0
artikel = 1
os.system("cls")

# Artikel hinzufügen bis 0 gedrückt
while artikel !=0:
    artikel = a.artikel_eingabe()
    if artikel == 0:
         break    
    ok = False
    while not(ok):
        menge = input("\nGeben Sie die gewünscht Menge ein ")
        ok = (a.menge_ok(menge))
    
    artikelpreis = a.preis_ermittlung(artikel,menge)
    preis = float(a.stueckpreis(artikel))
    gesammtnetto += artikelpreis
    print("\n","*"*30,"\n")
#    print("Hinzugefügt: Artikel: %3i  Menge: %5.0fStk  Stückpreis: %5.2f€  Preis: %7.2f€ \n") % (artikel, menge, preis, artikelpreis)
    print(f"Hinzugefügt: Artikel: {artikel}  Menge: {menge}Stk  Stückpreis: {preis:5.2f}€  Preis: {artikelpreis:7.2f}€")
    print("\n","*"*30,"\n")

#Gesammtrechnung
print("\n Nettobetrag insgesammt: ",round(gesammtnetto,2),"€")
print("\n Mehrwertseuer:          ",round((gesammtnetto*0.19),2),"€")
print("\n Bruttobetrag insgesammt:",round((gesammtnetto*1.19),2),"€")
print("\n (Bruttobetrag in DM: ",round((gesammtnetto*1.19*1.95583),2),"DM)\n")



