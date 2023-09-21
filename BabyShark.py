import winsound
import time
G = 392
D = 294
E = 330
F = 349
eight = 259
steen = 129
quarter = 520
half = 1040

def playVerse(shark):
    print(shark)
    winsound.Beep(D, quarter)
    winsound.Beep(E, quarter)
    for i in range(3):
        winsound.Beep(G, eight)
        print("doo")
        winsound.Beep(G, eight)
        print("doo")
        winsound.Beep(G, eight)
        print("doo")
        winsound.Beep(G, eight)
        print("doo")
        winsound.Beep(G, steen)
        print("doo")
        winsound.Beep(G, eight)
        print("doo")
        winsound.Beep(G, steen)
        print(shark)
        if i == 2:
            winsound.Beep(F,half)
        else:
            winsound.Beep(D, eight)
            winsound.Beep(E, eight)
playVerse("Baby shark") 
playVerse("Mommy shark")
playVerse("Daddy shark")
playVerse("Grandma shark")
playVerse("Grandpa shark")
playVerse("Lets go hunt")
playVerse("Run away")
playVerse("Safe at last")
playVerse("In the end")