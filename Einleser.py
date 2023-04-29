class Bank():
    def __init__(self, a_münzen: int, reg_zeit: int, muenz_pro_tag: int, muenzlist: list) -> None:
        self.anzahlmuenzen = a_münzen
        self.registrierungszeit = reg_zeit
        self.muenz_pro_tag = muenz_pro_tag
        self. muenzenlist = muenzlist
        
    def get_a_münzen(self):
        return self.a_münzen

    def get_reg_zeit(self):
        return self.reg_zeit
    
    def get_muenz_pro_tag(self):
        return self.muenz_pro_tag
    
    def get_muenzlist(self):
        return self.muenzlist

l=[]
f=open("a_example.txt")
t=f.read().splitlines()
for s in t:
    l.append(s)
a_unterschiedlich_münzen = t[0][0]
a_banken = t[0][1]
a_tage = t[0][2]

L_werte_gesamt_Münzen = []
zähler = -2
for i in range(int(len(t[1])/2)+1):
    zähler += 2
    L_werte_gesamt_Münzen.append(int(t[1][zähler]))

del t[0]
del t[0]
L_Banken = []
L2 = []
for i in range(int(len(t)/2)+1):
    a_münzen = t[i][0]
    reg_zeit = t[i][1]
    muenz_pro_tag = t[i][2]
    zähler = -2
    L2 = []
    for h in range(int(len(t[i+1])/2)+1):
        zähler += 2
        L2.append(int(t[i+1][zähler]))
    L_Banken.append(Bank(a_münzen=a_münzen,reg_zeit=reg_zeit,muenz_pro_tag=muenz_pro_tag,muenzlist=L2))







