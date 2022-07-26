import copy

PROSTORNINA = 40

p = []
# p = [
#     "7 11",
#     "12 25",
#     "5 9",
#     "1 1",
#     "18 25",
#     "3 4",
#     "15 17",
#     "2 3",
#     "2 2",
# ]

najvecji_volumen = 0
najvecja_teza = 0
najvecje = []

while True:
    i = input()
    if i == "":
        break
    p.append(i)

def parse(i):
    s = i.split(" ")
    return int(s[0]), int(s[1])

def recursive(siri_na_voljo, volumen = 0, teza = 0):
    global najvecja_teza, najvecje, najvecji_volumen

    if volumen >= najvecji_volumen and teza >= najvecja_teza:
        najvecja_teza = teza
        najvecji_volumen = volumen
        najvecje = siri_na_voljo

    for sir in siri_na_voljo:
        siri = copy.deepcopy(siri_na_voljo)
        siri.remove(sir)

        trenuten_volumen_sira, trenutna_teza_sira = parse(sir)

        trenuten_volumen = volumen + trenuten_volumen_sira
        trenutna_teza = teza + trenutna_teza_sira

        if trenuten_volumen > PROSTORNINA:
            # Uff, to pa ne bo šlo v nahrbtnik
            continue

        recursive(siri, trenuten_volumen, trenutna_teza)



def calculate_missing(ls):
    l = []

    for i in p:
        if i not in ls:
            l.append(i)
    
    return l

recursive(p)

for i in calculate_missing(najvecje):
    print(i)

print(f"Zaplenjena prostornina: {najvecji_volumen}")
print(f"Zaplenjena teža: {najvecja_teza}")
