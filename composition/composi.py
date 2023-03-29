francais = {
    "matier" : "francais",
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 4,
}
espaniol = {
    "matier" : "espaniol",
    "devoir" : [19, 10],
    "composition" : 12,
    "coeff" : 3
}
anglais = {
    "matier" : "anglais",    
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 3,
}
maths = {
    "matier" : "maths",
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 3,
}
svt = {
    "matier" : "svt",
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 2
}
pc = {
    "matier" : "pc",
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 2,
}
eg = {
    "matier" : "economie generale",
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 2
}
hg = {
    "matier" : "histoire geographie",
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 4
}
eps = {
    "matier" : "EPS",
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 1
}


def calc_moyen(matiers):
    moyenDevoir = sum(matiers["devoir"])/len(matiers["devoir"])
    moyen = (moyenDevoir + matiers["composition"]) / 2
    total = matiers["coeff"] * moyen
    return total



listerDesMatiers = ["francais","espaniol", "anglais","maths", "svt","pc", "eg", "hg", "eps"]

fr = calc_moyen(francais)    
es = calc_moyen(espaniol)    
an = calc_moyen(anglais)    
ma = calc_moyen(maths)    
sv = calc_moyen(svt)    
pc = calc_moyen(pc)    
eg = calc_moyen(eg)    
hg = calc_moyen(hg)
ep = calc_moyen(eps)    

moyenGenerale = (fr + es + an + ma + sv + pc + eg + hg + ep)/24
print("_"*50)
print("moyen en francais : ", format(fr, ".2f"))
print("_"*50)
print("moyen en espaniol : ", format(es, ".2f"))
print("_"*50)
print("moyen en anglais : ", format(an, ".2f"))
print("_"*50)
print("moyen en maths : ", format(ma, ".2f"))
print("_"*50)
print("moyen en svt : ", format(sv, ".2f"))
print("_"*50)
print("moyen en pc : ", format(pc, ".2f"))
print("_"*50)
print("moyen en economie generale : ", format(eg, ".2f"))
print("_"*50)
print("moyen en histoire et geographie : ", format(hg, ".2f"))
print("_"*50)
print("moyen en E P S : ", format(ep, ".2f"))
print("_"*50)
print("Moyen Generale : ",format(moyenGenerale,".2f"))
print("_"*50)



