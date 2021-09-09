import sys
print ("----------------------------------------------------------------")
print ("-             Sollicitatie Ruimtevuilnisman                    -") 
print ("----------------------------------------------------------------")
print ("Er wordt u een antaal relevente vragen gesteld. ") 
print ("Gelieve die naar eer en geweten in te vullen. ")
print ("Als blijkt dat u aan de criteria voldoet dan komt u in. ")
print ("Aanmerking voor een serieus sollicitatiegesprek! ")
print ("Ontspan maar blijf wakker, hier komen de vragen. ")
print ("----------------------------------------------------------------")

naam = input("Wat is uw naam? ")
geslacht = input("Was is uw geslacht? (Man of Vrouw) ")
lengte = input("Wat is uw netto lichaamslengte in hele cm, dus exclusief uw kapsel? ")
gewicht = input("Wat is uw lichaamsgewicht in hele kg? ")
Certificaat = input("Heeft uw een certificaat overleven met een gevaarlijk personeel? J/N ")
dressuur = input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? ")
mbo = input("Heeft uw een diplome Mbo ondernemen? J/N ")
rijbewijs = input("Heeft uw een geldig vrachtwagen rijbewijs? J/N ")
hoed = input("Bezit uw en hoge hoed? J/N ")
Ruimte = input("Bent uw ooit in ruimte geweest? J/N ")
handstand = input("Kan uw een handstand? J/N ")
koreaans = input("Kunt uw koreaans praten J/N ")
hoogtevrees = input("Heeft u last van hoogtevrees J/N ")
if geslacht == "Man":
    Man = input("Heeft uw een snor breder dan 10 Cm? J/N ")
else:
    Vrouw = input("Heeft uw rood krulhaar langer dan 20 Cm? J/N ")
if Man == "j":
    print("")
elif Vrouw == "j":
    print("")
if Certificaat == "j":
    if gewicht >= "90":
        if lengte >= "150":
            if hoed == "j":
                if rijbewijs == "j":
                    if mbo == "j":
                        if dressuur >= "4":
                         print("beste " + naam + " U komt in aanmerking voor een serieus sollicitatiegesprek! ")
                         sys.exit()
print("beste " + naam + " U komt niet in aanmerking voor een serieus sollicitatiegesprek! het spijt ons ")