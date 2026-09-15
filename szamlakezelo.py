


#GLOBÁLIS VÁLTOZÓK
pin_kod = 1234
egyenleg = 0
hasznalati_dij = 1000
adatfajl = "szamla.txt"
jogosult = False
tranzakciok = []
##########################
#FUNKCIÓK
##########################
def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="utf-8") as f:
            global tranzakciok
            tranzakciok = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")
   
def mentes(fajl):
    try:
        with open(fajl, "w", encoding="utf-8") as f:
            f.writelines(tranzakciok)
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")
     
def egyenleg():
    szamla_egyenleg = 0
    
    for sz in tranzakciok:
        szamla_egyenleg += int(sz)

    print(f"Az egyenleged: {szamla_egyenleg} FT ")

    return szamla_egyenleg
def utalas(osszeg):
    print("Utalás: ")
    
    osszeg += round(hasznalati_dij * 0.05)
    tranzakciok.append(f"-{osszeg}")
        
    if osszeg > egyenleg():
        print("Nem áll rendelkezésre megelelő összeg")
    else:
        tranzakciok.append(f"-{osszeg}")
        
    egyenleg()
    
def penzbetet(osszeg):
    print("Betét: ")

    tranzakciok.append(f"+{osszeg}")

    egyenleg()
    
#mennyiseg kor = 0 ÖSSZES TRANZAKCIÓ
#mennyiseg kor !=0 utolsó mennyiség tranzakció
def tortenet(darab):
    print("Tranzakciók: ")
    
    if darab == 0:
        kezdet = 0
    else:
        kezdet = len(tranzakciok)-darab
    
    for i in range(kezdet, len(tranzakciok)):    
        print(f"\t{tranzakciok[i].rstrip()}")



#MŰKÖDÉS
#BEJELENTLEZÉS
hibas_belepesszam = 3

pk = int(input("Add meg a PIN kódodat!: "))

if pk == pin_kod:
        jogosult = True
        print("Sikeres belépés!")
        
while(not jogosult and hibas_belepesszam > 1 ):
    print("Hibás PIN kód!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -=1
    
    if pk == pin_kod:
        jogosult = True
        print("Sikeres belépés!")
    
if not jogosult:
    print("Hibás PIN kód!")

adatbeolvasas(adatfajl) 

#Beolvasás, teszt kiírása
print(f"{tranzakciok}")

#FUNKCIÓVÁLASZTÓ MENÜ   
cim = "\nSZÁMLAKEZELŐ PROGRAM\n================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Pénz kivétel/átutalás",
    "3. Pénz betét",
    "----------",
    "4. Tranzakciótörténet",
    "9. Kilépés"
]

menupontok = [ 1, 2, 3, 4, 9]

while True:
    print(cim)
    for me in menu:
        print(f"{me}")

    valasztas = int(input("Válassz tevékenységet: "))

    while valasztas not in menupontok:
        print("Nincs ilyen menüpont\n")
 
    print(cim)
    for me in menu:
        print(f"{me}")
    
    valasztas = int(input("Válassz tevékenységet: "))

    # "Képernyő törlése"
    print(f"{'\n' * 20}")

    if valasztas == 1:
        egyenleg()
    elif valasztas == 2:
        u = int(input("Kivétel vagy utalás összege: "))
        utalas(u)
    elif valasztas == 3:
        b = int(input("Betét összege: "))
        penzbetet(b)
    elif valasztas == 4:
        m = int(input("Előzmény mérete (db) Minden: [0]: "))
        tortenet(m)
    elif valasztas == 9:
        #mentes(adatfajl)
        exit()


