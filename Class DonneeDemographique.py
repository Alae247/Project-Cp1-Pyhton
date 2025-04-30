class DonneeDemographique:
    def _init_(self, departement, annee, age, sexe, population):
        self.departement = departement
        self.annee = annee
        self.age = age
        self.sexe = sexe
        self.population = population

    def _str_(self):
        return (self.departement +"/"+ self.annee +"/"+ self.age +"ans / Sexe:"+ self.sexe +"/ Pop:"+ self.population)

    def _lt_(self, autre):
        if self.departement != autre.departement:
            return self.departement < autre.departement
        if self.age != autre.age:
            return self.age < autre.age
        return self.sexe < autre.sexe