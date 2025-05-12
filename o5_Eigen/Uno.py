Nachziehstapel = ["gr7", "gl2", "+4", "rot1"]
while len(Nachziehstapel) != 0:
    aktuelleKarte = Nachziehstapel .pop(0)

    if aktuelleKarte == "+4" :
        print("+4 kann gespielt werden")
        break
    else :
        print("Karte passt nicht")
if len(Nachziehstapel) == 0:    
    print("Nachziehstapel ist leer")

