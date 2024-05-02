import modul

dijazottak=modul.szerkezet(modul.fajl_olvas("dijazottak.txt"))

print("Az állomány",len(dijazottak),"díjazottat tartalmaz.")
print("Svéd díjazott összesen",modul.sved_dijazott(dijazottak),"alkalommal volt.")
orszag=input("Adja meg egy ország nevét: ")
dijak=modul.orszag_dijazott(dijazottak,orszag)
print("\tA bekért oszrág díjazottjai:")
if len(dijak)>0:
    for sor in dijak:
        print(f"\t{sor["ev"]}. évben: {sor["nev"]}")
else:
    print("\t\tEbből az országból nem volt díjazott")
mikorI=modul.nev_keres(dijazottak,"Kertész Imre")
print(f"Kertész Imre {dijazottak[mikorI]["ev"]}. évben kapta a díjat.")

kiirashoz=""
for elem in modul.tobb_dij(dijazottak):
    kiirashoz+=str(elem)+" "
modul.fajl_ir("tobb_dij.txt",kiirashoz)