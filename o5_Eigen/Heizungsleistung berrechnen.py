
breite = float(input ("Raumbreite in m: "))
tiefe = float(input ("Raumtiefe in m: "))
höhe = float(input ("Raumhöhe in m: "))
außen = float(input ("Temperatur außen in °C: "))
innen = float(input ("Temperautr innen in °C: "))

Volumen = breite * tiefe * höhe 
dT = innen - außen
Heizleistung = Volumen * dT * 0.024

if dT < 0 :
    print("Achtung, die Temperatur liegt unter Null")

print (f"Die benötigte Heizleistung beträgt: {Heizleistung} kW")

