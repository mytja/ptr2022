import copy
from typing import List

def parse(i):
    s = i.split(" ")
    return int(s[0]), int(s[1]), int(s[2])

class Route:
    def __init__(self, station1: int, station2: int, cost: int) -> None:
        self.station1 = station1
        self.station2 = station2
        self.cost = cost

    @staticmethod
    def fromList(list: List[str]) -> List:
        l = []
        for i in list:
            station1, station2, cost = parse(i)
            l.append(Route(station1, station2, cost))
        return l

    def __repr__(self):
        return f'od {self.station1} do {self.station2} ob ceni {self.cost}'

# povezave = Route.fromList([
#     "0 1 10",
#     "0 2 20",
#     "1 2 5",
#     "2 4 10",
#     "3 4 10",
#     "3 8 150",
#     "4 5 20",
#     "4 8 80",
#     "5 6 10",
#     "5 9 5",
#     "6 7 20",
#     "6 9 5",
#     "7 8 20",
# ])

n = int(input())
DESTINATION_STATION = n - 1

# Ni pomembno za nas
m = int(input())

najmanjsa_cena = None
izbrane_povezave = []

p = []

while True:
    i = input()
    if i == "":
        break
    p.append(i)

povezave = Route.fromList(p)

def find_all_possible_destinations(from_station: int):
    l = []
    for povezava in povezave:
        if povezava.station1 == from_station or povezava.station2 == from_station:
            l.append(povezava)
    return l

def recursive(trenutna_pot: List[Route], zadnja_postaja: int, cena: int, ustations: List[int]):
    global najmanjsa_cena, izbrane_povezave

    if (len(trenutna_pot) != 0 and
        (trenutna_pot[-1].station2 == DESTINATION_STATION or trenutna_pot[-1].station1 == DESTINATION_STATION) and
        (najmanjsa_cena is None or cena <= najmanjsa_cena)):

        #print("Našel najboljšo pot", trenutna_pot, cena)

        if najmanjsa_cena == cena and len(trenutna_pot) <= len(izbrane_povezave):
            return
        najmanjsa_cena = cena
        izbrane_povezave = trenutna_pot
    
    poti_na_voljo = find_all_possible_destinations(zadnja_postaja)

    for pot in poti_na_voljo:
        #print(f"Našel poti {poti_na_voljo}, izmed teh sem izbral {pot}. Zadnja postaja je {zadnja_postaja}, cena pa {cena}, trenutna pot pa {trenutna_pot}")
        
        used_stations = copy.deepcopy(ustations)

        if pot.station2 in used_stations and pot.station1 in used_stations:
            # To pomeni, da se vračamo na eno "že znano" postajo, kar je v resnici samo zapravljanje denarja.
            continue
            
        if pot.station1 not in used_stations:
            used_stations.append(pot.station1)
        if pot.station2 not in used_stations:
            used_stations.append(pot.station2)

        testna_pot = copy.deepcopy(trenutna_pot)
        testna_pot.append(pot)

        nova_postaja = pot.station1 if zadnja_postaja == pot.station2 else pot.station2

        recursive(testna_pot, nova_postaja, cena + pot.cost, used_stations)

recursive([], 0, 0, [])

def fmt_output():
    postaje = [0]
    for i in izbrane_povezave:
        if i.station1 != postaje[-1]:
            postaje.append(i.station1)
            continue
        postaje.append(i.station2)
    for i in postaje:
        print(i, end=" ")
    print()
    print(f"Cena: {najmanjsa_cena}")

fmt_output()
