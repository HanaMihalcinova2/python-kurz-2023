""" 
ukol-05
Zadání
Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
 """
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
""" 
1. Vytvoř seznam průměrných teplot pro každý den.
2. Vytvoř seznam ranních teplot.
3. Vytvoř seznam nočních teplot.
4. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu. 
"""

prum_teploty = []
for teplota in teploty:
    prum_teploty.append(round(sum(teplota)/ len(teplota),1))
print (f'Průměrné denní teploty pro každý den jsou: {prum_teploty}')

ranni = [teplota[0] for teplota in teploty]
print(f'Ranní teploty jsou: {ranni}') 

nocni = [teplota[3] for teplota in teploty]
print(f'Noční teploty jsou: {nocni}') 

dvou=[]
dvou = [[teplota[1],teplota[3]] for teplota in teploty]

""" 
ukol-05
Zadání
Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
 """
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
""" 
1. Vytvoř seznam průměrných teplot pro každý den.
2. Vytvoř seznam ranních teplot.
3. Vytvoř seznam nočních teplot.
4. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu. 
"""

prum_teploty = []
for teplota in teploty:
    prum_teploty.append(round(sum(teplota)/ len(teplota),1))
print (f'Průměrné denní teploty pro každý den jsou: {prum_teploty}')

ranni = [teplota[0] for teplota in teploty]
print(f'Ranní teploty jsou: {ranni}') 

nocni = [teplota[3] for teplota in teploty]
print(f'Noční teploty jsou: {nocni}') 

dvou=[]
dvou = [[teplota[1],teplota[3]] for teplota in teploty]
print(f'Polední a noční teploty jsou: {dvou}') 