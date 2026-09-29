'''
Edzőtermi Bérlet- és Alkalomkezelő Rendszer
===========================================
Rövid leírás
------------
A program egy sportoló vagy edzőtermi tag egyenlegét, fennmaradó alkalmait és belépési előzményeit tartja nyilván.
A fájlban pozitív értékek képviselik a feltöltött alkalmakat/jóváírásokat, a negatívak pedig a felhasználásokat.

Funkciólista
------------
[x] Adattároló fájl: berlet.txt

[x] Belépés: Tagazonosító ellenőrzése

[x] Funkcióválasztó menü:
	[x] Aktuális egyenleg / Alkalmak lekérdezése
	[x] Alkalom felhasználása / Belépés regisztrálása (egyenleg csökkentése extra szolgáltatási díj számításával)
	[x] Bérlet feltöltése / Alkalom vásárlása (egyenleg növelése)
	[x] Látogatási előzmények (minden belépés vagy az utolsó N alkalom kilistázása)

[x] Statisztikák
	[x] Összes felhasznált alkalom
	[x] Összes vásárolt alkalom
	[x] Leghosszabb/Legnagyobb egyösszegű feltöltés

[x] Kilépés

[x] Adatok elmentése
'''
import subprocess
from colorama import Fore, Back, Style



# GLOBÁLIS VÁLTOZÓK
tagazonosito = 4444
egyenleg = 0
belepodij = 2000
adatfajl = "berlet.txt"
engedely = False
Koltesek = []


#######################################
# FUNKCIÓK
#######################################
def adatolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global Koltesek
            Koltesek = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")

        
def mentes(fajl):
    try:
        with open(fajl, "w", encoding="UTF-8") as f:
            for i in range(len(Koltesek)):
                f.write(f"{Koltesek[i].rstrip()}\n")
            
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")


def egyenleg():
    szamlaegy = 0
    
    for sz in Koltesek:
        szamlaegy += int(sz)
    
    print(f"\nAz egyenleged: {szamlaegy} Ft")
    
    return  szamlaegy


def alkalom(osszeg):
    print("Alkalom: ")
    
    osszeg += round(belepodij * 0.05)
    
    if osszeg > egyenleg():
        print("\nNem áll rendelkezésre a megfelelő összeg!")
    else:        
        Koltesek.append(f"-{osszeg}")
    
    egyenleg()


def berlet(osszeg):
    print("Bérlet: ")
    Koltesek.append(f"+{osszeg}")
    
    egyenleg()


# darab = 0 -> összes tranzakció
# darab !=0 -> utolsó darab tranzakcio
def tortenet(db):
    print("Költések: ")
    
    if db == 0:
        kezdet = 0
    else:
        kezdet = len(Koltesek)-db
    
    for i in range(kezdet, len(Koltesek)):
        print(f"\t{Koltesek[i].rstrip()}")


def osszesfelh_alk():
    osszeg = 0
    
    for sz in Koltesek:        
        if int(sz) < 0:
            osszeg += int(sz)
    
    return osszeg


def osszesvas_alk():
    osszeg = 0
    
    for sz in Koltesek:        
        if int(sz) > 0:
            osszeg += int(sz)
    
    return osszeg   


def legnagyobb_egyosszeg():
    min_ertek = 0
    
    for sz in Koltesek:
        if int(sz) < min_ertek:
            min_ertek = int(sz)
            
    return min_ertek



#######################################
# A PROGRAM
#######################################

# BEJELENTKEZÉS
hibas_belepesszam = 2

tagan = int(input("Add meg a tagazonosítódat!: "))

if tagan == tagazonosito:
        engedely = True
        print(f"{Fore.GREEN} Sikeres belépés!")

while(not engedely and hibas_belepesszam > 1):
    print(f"{Fore.RED} Hibás tagazonosító!")
    tagan = int(input("Add meg a tagazonosítódat!: "))
    hibas_belepesszam -= 1
  
    if tagan == tagazonosito:
        engedely = True
        print(f"{Fore.GREEN} Sikeres belépés!")

if not engedely:
    print(f"{Fore.RED} Hibás tagazonosító!")

print(f"{Fore.RESET}", end="")

adatolvasas(adatfajl)

# Beolvasás teszt (kiírás)
# print(f"{tranzakciok}")


# FUNKCIÓVÁLASZTÓ MENÜ
cim = "\nSZÁMLAKEZELŐ PROGRAM\n====================\n"
menu = [
    "1. Aktuális egyenleg / Alkalmak lekérdezése",
    "2. Alkalom felhasználása",
    "3. Bérlet feltöltése",
    "--------------",
    "4. Látogatási előzmények",
    "5. Összes felhasznált alkalom",
    "6. Összes vásárolt alkalom ",
    "7. Legnagyobb költés",
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
        a = int(input("Alkalom felhasználása: "))
        alkalom(a)
    elif valasztas == 3:
        b = int(input("Bérlet feltöltése: "))
        berlet(b)
    elif valasztas == 4:
        m = int(input("Előzmény mérete (db) Minden: [0]: "))
        tortenet(m)
    elif valasztas == 5:
        print(f"\nÖsszes felhasznált alkalom: {osszesfelh_alk()} Ft")
    elif valasztas == 6:
        print(f"\nÖsszes vásárolt alkalom: {osszesvas_alk()} Ft")
    elif valasztas == 7:
        print(f"Legnagyobb egyösszegű feltöltés: {legnagyobb_egyosszeg()} Ft")
    elif valasztas == 9:
        mentes(adatfajl)
        exit()

    input(f"Üss egy billentyűt a folytatáshoz...")
    subprocess.run(["cls"], shell=True)