import subprocess
from colorama import Fore, Back, Style



# GLOBÁLIS VÁLTOZÓK
pin_kod = 1234
egyenleg = 0
hasznalati_dij = 1000
adatfajl = "01_Számlakezelo\\szamla.txt"
jogosult = False
tranzakciok = []


#######################################
# FUNKCIÓK
#######################################
def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global tranzakciok
            tranzakciok = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")

        
def mentes(fajl):
    try:
        with open(fajl, "w", encoding="UTF-8") as f:
            for i in range(len(tranzakciok)):
                f.write(f"{tranzakciok[i].rstrip()}\n")
            
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")


def egyenleg():
    szamla_egyenleg = 0
    
    for sz in tranzakciok:
        szamla_egyenleg += int(sz)
    
    print(f"\nAz egyenleged: {szamla_egyenleg} Ft")
    
    return szamla_egyenleg


def utalas(osszeg):
    print("Utalás: ")
    
    osszeg += round(hasznalati_dij * 0.05)
    
    if osszeg > egyenleg():
        print("\nNem áll rendelkezésre a megfelelő összeg!")
    else:        
        tranzakciok.append(f"-{osszeg}")
    
    egyenleg()


def penzbetet(osszeg):
    print("Betét: ")
    tranzakciok.append(f"+{osszeg}")
    
    egyenleg()


# darab = 0 -> összes tranzakció
# darab !=0 -> utolsó darab tranzakcio
def tortenet(darab):
    print("Tranzakciók: ")
    
    if darab == 0:
        kezdet = 0
    else:
        kezdet = len(tranzakciok)-darab
    
    for i in range(kezdet, len(tranzakciok)):
        print(f"\t{tranzakciok[i].rstrip()}")


def koltes_osszeg():
    osszeg = 0
    
    for sz in tranzakciok:        
        if int(sz) < 0:
            osszeg += int(sz)
    
    return osszeg


def betet_osszeg():
    osszeg = 0
    
    for sz in tranzakciok:        
        if int(sz) > 0:
            osszeg += int(sz)
    
    return osszeg   


def legnagyobb_kiadas():
    min_ertek = 0
    
    for sz in tranzakciok:
        if int(sz) < min_ertek:
            min_ertek = int(sz)
            
    return min_ertek



#######################################
# A PROGRAM
#######################################

# BEJELENTKEZÉS
hibas_belepesszam = 3

pk = int(input("Add meg a PIN kódodat!: "))

if pk == pin_kod:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")

while(not jogosult and hibas_belepesszam > 1):
    print(f"{Fore.RED} Hibás PIN kód!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -= 1
  
    if pk == pin_kod:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")

if not jogosult:
    print(f"{Fore.RED} Hibás PIN kód!")

print(f"{Fore.RESET}", end="")

adatbeolvasas(adatfajl)

# Beolvasás teszt (kiírás)
# print(f"{tranzakciok}")


# FUNKCIÓVÁLASZTÓ MENÜ
cim = "\nSZÁMLAKEZELŐ PROGRAM\n====================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Pénz kivétel/átutalás",
    "3. Pénz betét",
    "--------------",
    "4. Tranzakciótörténet",
    "5. Költések összege",
    "6. Betétek összege",
    "7. Legnagyobb kiadás",
    "--------------",
    "9. Kilépés"
]

menupontok = [1, 2, 3, 4, 5, 6, 7, 9]

while True:
    print(f"{Back.LIGHTCYAN_EX}{cim}")
    print(f"{Back.RESET}", end="")
    
    print(f"{Fore.LIGHTCYAN_EX}", end="")
    
    for me in menu:
        print(f"{me}")

    valasztas = int(input("Válassz tevékenységet: "))

    while valasztas not in menupontok:
        print("Nincs ilyen menüpont!\n")
        
        print(cim)    
        for me in menu:
            print(f"{me}")

        valasztas = int(input("Válassz tevékenységet: "))

    print(f"{Fore.RESET}", end="")

    # "Képernyő törlése"
    # print(f"{'\n' * 20}")

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
    elif valasztas == 5:
        print(f"\nÖsszes költés: {koltes_osszeg()} Ft")
    elif valasztas == 6:
        print(f"\nÖsszes pénzbetét: {betet_osszeg()} Ft")
    elif valasztas == 7:
        print(f"Legnagyobb kiadás: {legnagyobb_kiadas()} Ft")
    elif valasztas == 9:
        mentes(adatfajl)
        exit()

    input(f"Üss egy billentyűt a folytatáshoz...")
    subprocess.run(["cls"], shell=True)