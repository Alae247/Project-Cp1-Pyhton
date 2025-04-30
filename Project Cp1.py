with open('DS_ESTIMATION_POPULATION_CSV_FR/data.csv', 'r') as entree:
    lignes = entree.readlines()
class Conversion:
    def convertir_age(chaine_age):
        if chaine_age =="Y_LT5":
            return 0
        elif chaine_age =="Y_GE95":
            return 95
        
        nombre=""
        i = 1
        while i < len(chaine_age) and chaine_age[i]!= "T":
            nombre += chaine_age[i]
            i += 1
        if nombre !="":
            return int(nombre)
        else:
            return False
    
    def convertir_population(valeur):
        nombre_entier = ""
        i = 0
        while i < len(valeur) and valeur[i]!= ".":
            if valeur[i] >="0" and valeur [i] <="9":
                nombre_entier += valeur[i]
            i += 1
        if nombre_entier !="":
            return int(nombre_entier)
        else:
            return 0

class DonneeDemographique:
    def _init_(self, departement, annee, age, sexe, population):
        self.departement = departement
        self.annee = annee
        self.age = age
        self.sexe = sexe
        self.population = population

    def _str_(self):
        return (self.departement +"/"+ self.annee +"/"+ self.age +"ans / Sexe:"+ self.sexe +"/ Pop:"+ self.population

    def _lt_(self, autre):
        if self.departement != autre.departement:
            return self.departement < autre.departement
        if self.age != autre.age:
            return self.age < autre.age
        return self.sexe < autre.sexe
    

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