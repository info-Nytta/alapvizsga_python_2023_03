def fajl_olvas(fajl):
    nyit=open(fajl,mode="r",encoding="UTF-8-sig")
    adatok = []
    for sor in nyit:
        adatok.append(sor.replace("\n", "").strip().split("\t"))
    nyit.close()
    return adatok

def szerkezet(adatok):
    dic=[]
    for sor in adatok:
        dic.append({"ev":int(sor[0]),"nev":sor[1],"szulhely":sor[2]})
    return dic

def sved_dijazott(adatok):
    ossz=0
    for sor in adatok:
        if sor["szulhely"]=="Svédország":
            ossz+=1
    return ossz

def orszag_dijazott(adatok,orszag):
    dijazottak=[]
    for sor in adatok:
        if sor["szulhely"]==orszag:
            dijazottak.append({"ev":sor["ev"],"nev":sor["nev"]})
    return dijazottak

def nev_keres(adatok,nev):
    i=0
    while i<len(adatok) and adatok[i]["nev"]!=nev:
        i+=1
    if i<len(adatok):
        return i
    else:
        return -1

def tobb_dij(adatok):
    evek=[]
    i=0
    for i in range(len(adatok)-1):
        if adatok[i]["ev"]==adatok[i+1]["ev"]:
            evek.append(adatok[i]["ev"])
    return evek

def fajl_ir(fajl, szoveg):
    fajl_write=open(fajl,mode="w",encoding="utf-8")
    fajl_write.write(szoveg)
    fajl_write.close()