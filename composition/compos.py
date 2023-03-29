def calc_moyen(matiers):
    moyenDevoir = sum(matiers["devoir"])/len(matiers["devoir"])
    moyen = (moyenDevoir + matiers["composition"]) / 2
    total = matiers["coeff"] * moyen
    affichage = f"le moyen {matiers['matier']} : {moyen}"
    return affichage

print(calc_moyen(francais))    
print(calc_moyen(espaniol))    
print(calc_moyen(anglais))    
print(calc_moyen(maths))    
print(calc_moyen(svt))    
print(calc_moyen(pc))    
print(calc_moyen(eg))    
print(calc_moyen(hg))
print(calc_moyen(eps))    





