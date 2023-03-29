francais = {
    "matier" : "francais",
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 4,
}
espaniol = {
    "matier" : "espaniol",
    "devoir" : [7, 3],
    "composition" : 5,
    "coeff" : 3
}
anglais = {
    "matier" : "anglais",    
    "devoir" : [11.5, 2.5],
    "composition" : 9,
    "coeff" : 3,
}
maths = {
    "matier" : "maths",
    "devoir" : [20, 48],
    "composition" : 0,
    "coeff" : 3,
}
svt = {
    "matier" : "svt",
    "devoir" : [18, 30],
    "composition" : 0,
    "coeff" : 2
}
pc = {
    "matier" : "pc",
    "devoir" : [14, 14],
    "composition" : 0,
    "coeff" : 2,
}
eg = {
    "matier" : "economie generale",
    "devoir" : [30, 30],
    "composition" : 0,
    "coeff" : 2
}
hg = {
    "matier" : "histoire geographie",
    "devoir" : [12, 11],
    "composition" : 6,
    "coeff" : 4
}
eps = {
    "matier" : "EPS",
    "devoir" : [10, 10],
    "composition" : 0,
    "coeff" : 1
}


def calc_moyen(matiers):
    moyenDevoir = sum(matiers["devoir"])/len(matiers["devoir"])
    moyen = (moyenDevoir + matiers["composition"]) / 2
    total = matiers["coeff"] * moyen
    affichage = f"le moyen {matiers['matier']} : {moyen}"
    return affichage


fram = calc_moyen(francais)    
espm = calc_moyen(espaniol)    
angm = calc_moyen(anglais)    
matm = calc_moyen(maths)    
svsm = calc_moyen(svt)    
pcsm = calc_moyen(pc)    
egsm = calc_moyen(eg)    
hgsm = calc_moyen(hg)
eptm = calc_moyen(eps)    


def Total(matier):
    moyenDevoir = sum(matier["devoir"])/len(matier["devoir"])
    moyen = (moyenDevoir + matier["composition"]) / 2
    total = matier["coeff"] * moyen
    return total

fra = Total(francais)
esp = Total(espaniol)
ang = Total(anglais)
mat = Total(maths)
svs = Total(svt)
pcs = Total(pc)
egs = Total(eg)
hgs = Total(hg)
ept = Total(eps)

moyenTo = (fra + esp + ang + mat + svs + pcs + egs + hgs + ept)/24

print("_"*50)
print(fram)
print("_"*50)
print(espm)
print("_"*50)
print(angm)
print("_"*50)
print(matm)
print("_"*50)
print(svsm)
print("_"*50)
print(pcsm)
print("_"*50)
print(egsm)
print("_"*50)
print(hgsm)
print("_"*50)
print(eptm)
print("_"*50)
print("Moyen : "+format(moyenTo,".2f")+"/20")






