def secti(a, b, c,):
    vysledek = a + b +c
    return vysledek

def je_delitelne_3(x):
    zbytek = x % 3
    if zbytek == 0:
        return True
    else:
        return False

if __name__=="__main__":
    x = je_delitelne_3(6)
    print("Je delitelne?", x)
    #x = secti(1, 2, 3)
    #print("Výsledek:",x)
