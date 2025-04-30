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