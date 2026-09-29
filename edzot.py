import subprocess






#Glob vált 
tag_id= 1234
akt_egyenleg = 0
napi_dij = 500
adatfajl = "Edzoterem\\berlet.txt"
jogosult = False
egyenleg = []

#Funkciók
def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global egyenleg
            egyenleg = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")

def egyenleg_fv():
    szamla_egyenleg = 0
    
    for sz in egyenleg:
        szamla_egyenleg += int(sz)
        
    print(f"\nAz egyenleged: {szamla_egyenleg} Ft")
    
    return szamla_egyenleg



# BEJELENTKEZÉS
hibas_belepesszam = 3

pk = int(input("Add meg a tagazonosítódat!: "))

if pk == tag_id:
        engedely = True
        print(f"{Fore.GREEN} Sikeres belépés!")

while(not engedely and hibas_belepesszam > 1):
    print(f"{Fore.RED} Hibás tagazonosító!")
    tagan = int(input("Add meg a tagazonosítódat!: "))
    hibas_belepesszam -= 1
  
    if tagan == tag_id:
        engedely = True
        print(f"{Fore.GREEN} Sikeres belépés!")

if not engedely:
    print(f"{Fore.RED} Hibás tagazonosító!")

print(f"{Fore.RESET}", end="")

adatbeolvasas(adatfajl)





# Beolvasás teszt (kiírás)
# print(f"{tranzakciok}")


# FUNKCIÓVÁLASZTÓ MENÜ
cim = "\nSZÁMLAKEZELŐ PROGRAM\n====================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Egyenleg teremhasználat",
    "3. Bérlet/ alkalom vásárlás",
    "--------------",
    "4. Előzmények",
    "5. Edzések száma",
    "6. Összes vásárolt alkalom",
    "7. Legnagyobb feltöltés",
    "--------------",
    "9. Kilépés"
]

menupontok = [1, 2, 3, 4, 5, 6, 7, 9]













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