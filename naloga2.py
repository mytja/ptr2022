stMesecev = int(input("Vnesite število mesecev: "))

fN1 = 1
fN2 = 1
mesec = 1

while mesec < stMesecev:
    t = fN1 + fN2
    fN1 = fN2
    fN2 = t
    mesec += 1

print(fN2)