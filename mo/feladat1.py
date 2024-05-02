import random

vNev=input("Kérem a vezetéknevét: ")
kNev=input("Kérem a keresztnevét: ")
jelszo=vNev[:2].lower()+kNev[-2:].upper()+str(random.randint(100,999))
print("Generált jelszó:",jelszo)
