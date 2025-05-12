import random
leiterspiel_dict = {3: 10, 5: -3, 8: 22, 10: -5, 20: 15, 24: -10, 40: 20, 45: -15, 98: -20,}

Feld = 0
while Feld != 100: 
    Wurf = random.randint(1,6)
    print("Würfelzahl:" , Wurf)
    Feld = Feld + Wurf
    print("Aktuelles Feld:", Feld)

    Aktion = leiterspiel_dict[Feld]
    if Aktion > 0: 
        Feld = Feld + Aktion 
        print("Sie waren auf einer Leiter, neues Feld:", Feld)
    elif Aktion < 0: 
        Feld = Feld + Aktion
        print("Sie waren auf einer Rutsche:", Feld)
     
        

if Feld == 100 : 
    print("Spiel beendet")

