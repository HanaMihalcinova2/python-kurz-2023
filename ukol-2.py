# ukol-02
# Zadání
# Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. 
# Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. 
# Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. 
# Obě informace si ulož. 

kod_soucastky = (input(f'Jaký je kód součástky? '))
mnozstvi_soucastky = int(input(f'Jaké je požadováno množství součástky? '))

# Následně naprogramuj následující varianty:

# 1 Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.

if kod_soucastky not in sklad:
    print(f'Bohužel součástka ' , kod_soucastky, f' není skladem.')

# 2 Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. 
# Následně součástku odeber ze slovníku, protože je vyprodaná.


if kod_soucastky in sklad:
    if sklad[kod_soucastky] < mnozstvi_soucastky:
        print(f'Součástka ', kod_soucastky, f' je na skladě v omezeném množství ' , sklad[kod_soucastky], f' ks. ')
        sklad.pop(kod_soucastky)

# 3 Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

if kod_soucastky in sklad:
    if sklad[kod_soucastky] >= mnozstvi_soucastky:
        print(f'Poptávku po součástce ', kod_soucastky, f'lze v požadovaném množství ' , mnozstvi_soucastky, f' uspokojit. ')
        sklad[kod_soucastky]=sklad[kod_soucastky]- mnozstvi_soucastky

print(sklad)        