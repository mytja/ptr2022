import copy
import sys
from typing import List

# Algoritem bo iskal od največjega cekina proti najmanjšemu in vrne prvo rešitev, saj je ta rešitev navadno (če ne kar vedno) najboljša.
# To zahteva izjemno malo časa, primerljivo z neoptimiziranim algoritmom, ki poišče čisto vse možne kombinacije.
# Odločitev prepuščam uporabniku, je pa (izjemno) priporočljivo uporabljati optimizacije.
OPTIMIZE = True

def parse(i):
    s = i.split(" ")
    return int(s[0]), int(s[1])

_, M = parse(input())
cekini: List[int] = []

if M <= 0:
    print("Uau! Ti bi pa kar rad plačal račune, ki gredo v negativnost ali v ničlo.")
    sys.exit(1)

lowestAmountNeeded = None

while True:
    i = input()
    if i == "":
        break
    cekini.append(int(i))

cekini.sort(reverse=True)

def recursive(porabljeni_cekini: List[int], denarja_porabljenega: int):
    global lowestAmountNeeded

    if denarja_porabljenega > M:
        return False

    if denarja_porabljenega == M and (lowestAmountNeeded is None or len(porabljeni_cekini) < lowestAmountNeeded):
        lowestAmountNeeded = len(porabljeni_cekini)
        #print(porabljeni_cekini, len(porabljeni_cekini), denarja_porabljenega)
        return True

    for cekin in cekini:
        porabljeni_cekini_local = copy.deepcopy(porabljeni_cekini)
        nov_porabljen_denar = denarja_porabljenega + cekin
        porabljeni_cekini_local.append(cekin)

        if recursive(porabljeni_cekini_local, nov_porabljen_denar) and OPTIMIZE:
            return True

recursive([], 0)

if lowestAmountNeeded is None:
    print(-1)
    sys.exit(1)

print(lowestAmountNeeded)
