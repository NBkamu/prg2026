


#GLOBÁLIS VÁLTOZÓK
pin_kod = 1234
egyenleg = 0
hasznalati_dij = 1000
adatfajl = "szamla.txt"
jogosult = False


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

print(cim)
for me in menu:
    print(f"{me}")

valasztas = int(input("Válassz tevékenységet: "))

while valasztas not in menupontok:
    print("Nincs ilyen menüpont\n")
menupontok = [1, 2, 3, 4, 9]    
print(cim)
for me in menu:
    print(f"{me}")
    
valasztas = int(input("Válassz tevékenységet: "))

while valasztas not in menupontok:
    

if valasztas == 1:
    egyenleg()
elif valasztas == 2:
    utalas(123)
elif valasztas == 3:
    penzbetet(10000)
elif valasztas == 4:
    tortenet(0)
elif valasztas == 9:
    exit()

##########################
#FUNKCIÓK
##########################
def egyenleg():
    print("Az egyenleged: ")

def utalas(osszeg):
    print("Utalás: ")
    
def penzbetet(osszeg):
    print("Betét: ")

#mennyiseg kor = 0 ÖSSZES TRANZAKCIÓ
#mennyiseg kor !=0 utolsó mennyiség tranzakció
def tortenet(darab):
    print("Tranzakciók: ")
    
