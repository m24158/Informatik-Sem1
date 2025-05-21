import random
AnzahlWurf = 0

if AnzahlWurf == 0 :
    print("Sie sind im Gefängnis")
    while True :
        string1 = input("Möchten sie sich freikaufen? (ja/nein):")
        if string1 == "ja" :
            print("Sie kommen aus dem Gefängnis: -50$")
            break 
        elif string1 == "nein" :
            while AnzahlWurf < 3 :
                Wurf = random.randint(1,6)
                Wurf2 = random.randint(1,6)
                print( Wurf, Wurf2)
                AnzahlWurf = AnzahlWurf + 1
                if Wurf == Wurf2   :
                    print("Pasch - Sie kommen aus dem Gefängnis")
                    break
                elif AnzahlWurf == 3 :
                    print("Würfelversuche vorbei, Sie müssen 50$ zahlen")
            break

        elif string1 != "ja" or "nein" :
            print("Bitte entscheidemn!")


        
        
         



    


