francais = {
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 4,
}
espaniol = {
    "devoir" : [19, 10],
    "composition" : 12,
    "coeff" : 3
}
anglais = {
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 3,
}
maths = {
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 3,
}
svt = {
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 2
}
pc = {
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 2,
}
eg = {
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 2
}
hg = {
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 4
}
eps = {
    "devoir" : [15, 11],
    "composition" : 10,
    "coeff" : 1
}

def main(): 
    if menu == "1":
        md = sum(francais["devoir"])/len(francais["devoir"])
        print("moyen devoir francais :",md)
        moyen = (md + francais["composition"]) / 2
        print("moyen francais :",moyen)
        total = francais["coeff"] * moyen

    elif menu == "2":
        md = sum(espaniol["devoir"])/len(espaniol["devoir"])
        print("moyen devoir espaniol :",md)
        moyen = (md + espaniol["composition"]) / 2
        print("moyen espaniol :",moyen)
        total = espaniol["coeff"] * moyen

    elif menu == "3":
        md = sum(anglais["devoir"])/len(anglais["devoir"])
        print("moyen devoir anglais :",md)
        moyen = (md + anglais["composition"]) / 2
        print("moyen anglais :",moyen)
        total = anglais["coeff"] * moyen

    elif menu == "4":
        md = sum(maths["devoir"])/len(maths["devoir"])
        print("moyen devoir maths :",md)
        moyen = (md + maths["composition"]) / 2
        print("moyen maths :",moyen)
        total = maths["coeff"] * moyen

    elif menu == "5":
        md = sum(svt["devoir"])/len(svt["devoir"])
        print("moyen devoir svt :",md)
        moyen = (md + svt["composition"]) / 2
        print("moyen svt :",moyen)
        total = eps['coeff'] * moyen
    elif menu == "6":
        md = sum(pc["devoir"])/len(pc["devoir"])
        print("moyen devoir pc :",md)
        moyen = (md + pc["composition"]) / 2
        print("moyen pc :",moyen)
        total = eps['coeff'] * moyen

    elif menu == "7":
        md = sum(eg["devoir"])/len(eg["devoir"])
        print("moyen devoir economie :",md)
        moyen = (md + eg["composition"]) / 2
        print("moyen economie :",moyen)
        total = eps['coeff'] * moyen
    elif menu == "8":
        md = sum(hg["devoir"])/len(hg["devoir"])
        print("moyen devoir histore geographie :",md)
        moyen = (md + hg["composition"]) / 2
        print("moyen histore geographie :",moyen)
        total = eps['coeff'] * moyen
    elif menu == "9":
        md = sum(eps["devoir"])/len(eps["devoir"])
        print("moyen devoir EPS :",md)
        moyen = (md + eps["composition"]) / 2
        print("moyen EPS :",moyen)
        total = eps['coeff'] * moyen
while True:
    menu = str(input("1-francais\n2-espaniol\n3-anglais\n4-maths\n5-svt\n6-pc\n7-eps\n8-eg\n9-hg\n\nentre votre choix entre ::>> "))
    ls=['1','2','3','4','5','6','7','8','9']
    if menu not in ls:
        break
        print("bye")
    else:
        main()



