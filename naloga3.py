# Za čim večjo hitrost, se priporoča uporabljati pypy3 namesto CPythona (do 10x hitreje)

import copy

seznam_resitev = []

zaporedje = [1, "", 2, "", 3, "", 4, "", 5, "", 6, "", 7, "", 8, "", 9]
alreadyTried = []

def join(z) -> str:
    t = ""
    for i in z:
        t += str(i)
    return t

def calculate(t) -> bool:
    result = eval(t)
    #print(t, result)
    return result == 100

def recursiveAddMinus(t, seznam_resitev, alreadyTried):
    foundNone = False
    for v in t:
        if isinstance(v, str) and v == "":
            foundNone = True
            break
    
    if not foundNone:
        #print("Found none is false")
        return seznam_resitev

    for i, v in enumerate(t):
        if isinstance(v, str) and v == "":
            d1 = copy.deepcopy(t)
            d2 = copy.deepcopy(t)
       
            d1[i] = "-"
            d2[i] = "+"
            
            for d in [d1, d2]:
                _t = join(d)

                if _t in alreadyTried:
                    continue
                
                if _t not in seznam_resitev and calculate(_t):
                    seznam_resitev.append(_t)
                
                alreadyTried.append(_t)

                seznam_resitev = recursiveAddMinus(d, seznam_resitev, alreadyTried)
    
    return seznam_resitev

seznam_resitev = recursiveAddMinus(zaporedje, seznam_resitev, alreadyTried)
print("Najdene vse možne rešitve:")
for i in seznam_resitev:
    print(i)
