class animaux :    
    def __init__(self, regimealimentaire, poidnouriture):
        self.regimealimentaire = regimealimentaire
        self.poidnouriture = poidnouriture
    
    def __str__(self):
        return "il est  " + self.regimealimentaire + " il mange " + self.poidnouriture + "gramme\n"


class mamifere(animaux) :
    def __init__(self, domestique , nonmarin , nb_patte, regimealimentaire, poidnouriture):
        super().__init__(regimealimentaire, poidnouriture)
        self.nb_patte = nb_patte
        self.domestique = domestique
        self.nonmarin = nonmarin
    
    def __str__(self):
        return"il est  " + self.regimealimentaire + "\nil mange " + self.poidnouriture + "gramme \nil est " + self.domestique + "\nil est " + self.nonmarin + "\nil a " + self.nb_patte + "pattes"

class nonmamifere(animaux) :
    def __init__(self, domestique , nonmarin , nb_patte, regimealimentaire, poidnouriture):
        super().__init__(regimealimentaire, poidnouriture)
        self.nb_patte = nb_patte
        self.domestique = domestique
        self.nonmarin = nonmarin
        
    def __str__(self):
        return"il est  " + self.regimealimentaire + "\nil mange " + self.poidnouriture + "gramme \nil est " + self.domestique + "\nil est " + self.nonmarin + "\nil a " + self.nb_patte + " pattes"

if __name__ == "__main__":
    monzoo = {}
    monzoo["poule"] = nonmamifere("domestique","nonmarin","2", "onmivor", "200")
    monzoo["lion"] = mamifere("non-domestique","nonmarin","4", "carnivor", "3000")
    monzoo["lapin"]= mamifere("domestique","nonmarin","4", "vegetarien", "100")
    monzoo["mouton"]= mamifere("domestique","nonmarin","4", "vegetarien", "500")
    monzoo["chien"] = mamifere("domestique","nonmarin","4", "omninivor", "500")
    monzoo["pieuvre"]= nonmamifere("non-domestique","marin","pas de ", "carnivor", "200")
    monzoo["lapin"]= mamifere("domestique","nonmarin","4", "vegetarien", "100")
    #print(monzoo["poule"])
    for mykey in monzoo:
        print(mykey+ "\n" +str(monzoo[mykey]))
