def meretBeker():
    meret=0
    while not (0<meret<10 and meret%2!=0):
        meret=int(input("Rajzméret (páratlan 1-10): "))
    return meret

def rajz(meret,x,y):
    for i in range(meret):
        for j in range(meret):
            if i==y-1 and j==x-1:
                print("x",end=" ")
            else:
                print(".",end=" ")
        print()

rajzMeret=meretBeker()
pozX=int(input(f"x koordináta: (1-{rajzMeret}): "))
pozY=int(input(f"y koordináta: (1-{rajzMeret}): "))
if 1<=pozX<=rajzMeret and 1<=pozY<=rajzMeret:
    rajz(rajzMeret,pozX,pozY)
else:
    print("HIBA: Nem megfelelő bemeneti érték!")