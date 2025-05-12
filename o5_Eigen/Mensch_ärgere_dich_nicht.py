import random

i=0
while i <3 or Wurf == 6 : 
    Wurf = random.randint(1,6)
    print(Wurf)
    i = i+1

    if Wurf == 6 :
        i = 3
        print("Go")
        continue
    


else :
    print("Nächster Spieler")