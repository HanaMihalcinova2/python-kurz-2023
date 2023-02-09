# ukol-04

## Zadání
# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

# 1. Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.

tel_cislo = input("Zadej telefonni číslo, kam chceš poslat zprávu: ")

if len(tel_cislo) = 9:
    #print("Telefonní číslo má "{len(tel_cislo)} "čísel.")

print(len(tel_cislo))

# if len(tel_cislo) = 13:
#    print("Telefonní číslo má 13 čísel s předvolbou +420")


# 1. Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# zprava = int(input("Zadej zprávu, kterou chceš poslat: "))

# if len(zprava) : 100 
"""
Tvůj program bude obsahovat dvě funkce:
1. První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu `True`, jinak vrátí hodnotu `False`.
1. Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné,
vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou
vypíše uživateli.

Tipy: 
* Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme
v kurzu zatím neřešili.
* Pro kontrolu předvolby použijte _slicing_ (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem `"+420"`.
"""