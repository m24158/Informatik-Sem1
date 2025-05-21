
def eingabe_der_Werte(): #lässt sich einklappen, dadurch kürzer
    breite = float(input ("Raumbreite in m: "))
    tiefe = float(input ("Raumtiefe in m: "))
    höhe = float(input ("Raumhöhe in m: "))
    außen = float(input ("Temperatur außen in °C: "))
    innen = float(input ("Temperautr innen in °C: "))

    Volumen = breite * tiefe * höhe 
    dT = innen - außen
    return Volumen, dT #Werte zurückgeben
Volumen, dT = eingabe_der_Werte() 

if dT < 0 :
    print("Achtung! Die Temperaturdifferenz ist kleiner als Null")

def berechnung_Heizleistung ():
   return Volumen * dT * 0.024

Heizleistung = berechnung_Heizleistung()


print (f"Die benötigte Heizleistung beträgt: {Heizleistung} kW")


