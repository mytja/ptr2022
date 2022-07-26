# Potrebuje Python 3.7+
# Ta program sprejema vse vrednosti kovancev

cekini = {}

while True:
    i = input("")
    if i == "":
        break
    i = int(i)
    if i not in cekini:
        cekini[i] = 0
    cekini[i] += 1

# Uredimo dict
cekini = dict(sorted(cekini.items()))

total = 0

for k, i in cekini.items():
    print(f"{k}€: {i}x")
    total += k * i

print(f"Skupaj: {total}€")
