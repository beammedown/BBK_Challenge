class Bank():
    def __init__(self, a_münzen: int, reg_zeit: int, muenzen_pro_tag: int, muenzenlist: list) -> None:
        self.anzahlmuenzen = a_münzen
        self.registrierungszeit = reg_zeit
        self.muenzen_pro_tag = muenzen_pro_tag
        self.muenzenlist = muenzenlist
        
    def get_a_muenzen(self):
        return self.anzahlmuenzen

    def get_reg_zeit(self):
        return self.registrierungszeit
    
    def get_muenzen_pro_tag(self):
        return self.muenzen_pro_tag
    
    def get_muenzenlist(self):
        return self.muenzenlist


t = []
f = open("f_banks_of_the_world.txt")
l = f.read().splitlines()
for s in l:
    t.append(s.split())


a_unterschiedlich_münzen = t[0][0]
a_banken = t[0][1]
a_tage = t[0][2]

L_werte_gesamt_Münzen = []

for i in range(len(t[0])):
    L_werte_gesamt_Münzen.append(int(t[1][i]))

del t[0]
del t[0]
L_Banken = []
L2 = []

zähler1 = 0
zähler2 = 1
for i in range(int(len(t)/2)):
    a_münzen = t[zähler1][0]
    reg_zeit = t[zähler1][1]
    muenzen_pro_tag = t[zähler1][2]
    zähler1 += 2
    L2 = []
    for h in range(len(t[zähler2])):
        L2.append(int(t[zähler2][h]))
    zähler2 += 2
    L_Banken.append(Bank(a_münzen=a_münzen, reg_zeit=reg_zeit, muenzen_pro_tag=muenzen_pro_tag, muenzenlist=L2))


instanze = L_Banken[999]
print(instanze.get_muenzenlist())






