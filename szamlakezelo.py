


#GLOBÁLIS VÁLTOZÓK
pin_kod = 1234
egyenleg = 0
hasznalati_dij = 1000
adatfajl = "szamla.txt"
jogosult = False


#MŰKÖDÉS
hibas_belepesszam = 3

pk = int(input("Add meg a PIN kódodat!: "))
if pk == pin_kod:
        jogosult = True
        print("Sikeres belépés!")
        
while(not jogosult and hibas_belepesszam > 0 ):
    print("Hibás PIN kód!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -=1
    
    if pk == pin_kod:
        jogosult = True
        print("Sikeres belépés!")
    
   
