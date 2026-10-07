def cislo_text(cislo):
    # Převedeme vstup na číslo, abychom mohli porovnávat velikost
    n = int(cislo)

    if n == 100:
        return "sto"

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    nact = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if n < 10:
        return jednotky[n]
    if n < 20:
        return nact[n - 10]

    prvni_cislice = int(cislo[0])
    druha_cislice = int(cislo[1])
    
    if druha_cislice == 0:
        return desitky[prvni_cislice]  
    else:
        return desitky[prvni_cislice] + " " + jednotky[druha_cislice]
    
if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)