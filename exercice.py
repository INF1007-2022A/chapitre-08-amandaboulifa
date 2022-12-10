#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def CompareFichier(fich_1, fich_2) : 
    with open(fich_1) as f1, open(fich_2) as f2 : 
        i = 0
        for line1 in f1 : 
            i+=1

            for line2 in f2 : 
                if line1 == line2 : 
                    print("OK")
                else : 
                    result = "La différence est à la ligne " + str(i)
                    break
            return result

def TripleEspaces(fichier, fichier_copy) : 
    with open(fichier) as f1, open(fichier_copy, "w") as f2 : 
        f2.write(f1.read().replace(" ", "   "))
        
        #eu besoin corrigé pour comprendre que besoin de créer un nouveau ficher et le f1.read()

def Notes(f_notes, f_notes_copy) : 
    with open(f_notes) as f, open(f_notes_copy, "w") as f_copy : 
        for line in f : 
            for key, value in PERCENTAGE_TO_LETTER.items() : 
                if value[0] <= int(line) <= value[1] : 
                    f_copy.write(f"{line} {key}")

            #f_copy.write(f"{line} {[k for k, v in PERCENTAGE_TO_LETTER.items() if v in range(int(line[0]), int(line[1]))]}")

def LivreRecettes (fichier, fichier_copy) : 
    #EUHHHHHHHH JSP
    pass

def Nombres(fichier1) : 
    with open(fichier1) as f : 
        content = f.readlines()
        liste_nombres = []
        for line in content : 
            for i in line : 
                if i.isdigit() == True : 
                    liste_nombres.append(i)

        liste_nombres.sort()
        
        return liste_nombres

def LigneSurDeux (fichier, fichier_copy) : 
    with open(fichier) as f, open(fichier_copy, "w") as f_copy : 
        compteur = 0
        for line in f : 
            if compteur % 2 == 0 : 
                f_copy.write(f"{line}")
            compteur += 1
            



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    result_CompareFichier = CompareFichier("notes.txt", "exemple.txt")
    result_TripleEspaces = TripleEspaces("./exemple.txt", "./exemple_copy.txt")
    result_Notes = Notes("notes.txt", "notes_copy.txt")
    result_Nombres = Nombres("exemple.txt")
    result_LigneSurDeux = LigneSurDeux("exemple.txt", "lignesurdeux.txt")
    print(result_Nombres)
    
