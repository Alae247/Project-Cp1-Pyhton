class CollectionDemographique:
    def _init_(self):
        self.liste = []

    def ajouter(self, donnee):
        self.liste.append(donnee)

    def trier(self):
        self.liste.sort()

    def departement(self):
        resultats = []
        for d in self.liste:
            resultats.append(d.departement)
        return resultats

    def annee(self):
        resultats = []
        for d in self.liste:
            resultats.append(d.annee)
        return resultats

    def age(self):
        resultats = []
        for d in self.liste:
            resultats.append(d.age)
        return resultats

    def sexe(self):
        resultats = []
        for d in self.liste:
            resultats.append(d.sexe)
        return resultats

    def population(self):
        resultats = []
        for d in self.liste:
            resultats.append(d.population)
        return resultats

    def filtre_departement(self, code):
        resultat = []
        for d in self.liste:
            if d.departement == code:
                resultat.append(d)
        return resultat

    def filtre_annee(self, annee):
        resultat = []
        for d in self.liste:
            if d.annee == annee:
                resultat.append(d)
        return resultat

    def filtre_age(self, age):
        resultat = []
        for d in self.liste:
            if d.age == age:
                resultat.append(d)
        return resultat

    def filtre_sexe(self, sexe):
        resultat = []
        for d in self.liste:
            if d.sexe == sexe:
                resultat.append(d)
        return resultat

    def filtre_age_diff(self, age):
        resultat = []
        for d in self.liste:
            if d.age != age:
                resultat.append(d)
        return resultat

    def filtre_sexe_diff(self, sexe):
        resultat = []
        for d in self.liste:
            if d.sexe != sexe:
                resultat.append(d)
        return resultat

class Reporting:
    def total_population_par_departement(donnees):
        resultats = {}
        for d in donnees:
            dept = d.departement
            pop = d.population

            if dept not in resultats:
                resultats[dept] = pop
            else:
                resultats[dept] = resultats[dept] + pop
        return resultats

    def population_totale(donnees):
        total = 0
        for d in donnees:
            total = total + d.population
        return total