import random

print("Sie sind im Gefängnis")
string1 = input("Möchten sie sich freikaufen? (ja/nein):")

if string1 == "ja" :
    print("Sie kommen aus dem Gefängnis; -50$")

elif string1 == "nein" :
    i = 0
    while i < 3 :
        Wurf = random.randint(1,6)
        Wurf2 = random.randint(1,6)
        print( Wurf, Wurf2)
        i = i+1 

        if Wurf == Wurf2   :
            print("Pasch - Sie kommen aus dem Gefängnis")
            break
    
    
        elif i == 3 :
            print("Würfelversuche vorbei, Sie müssen 50$ zahlen")

else : 
    print("Bitte entscheidemn!")

    


