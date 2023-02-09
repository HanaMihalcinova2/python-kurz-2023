#Zadání
#Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

#Soubor si ulož a načti do slovníku.

import json
with open('body.json', encoding='utf-8') as soubor:
    #print(type(soubor))
    body = json.load(soubor) #slovnik
print(body)

#Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

#print(body.keys())
#print(body.values())

x = body.keys()
print(x)
 
for x,y in body.items():
    print(f' {x}  {y} ')

#Výsledný slovník ulož jako JSON do souboru prospech.json.