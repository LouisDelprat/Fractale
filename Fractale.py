import turtle as tl

# Programme permettant de tracer un arbre fracal
# Auteur : Louis Delprat


def arbre(hauteur,profondeur,epaisseur,angle_g,angle_d,rapport_g,rapport_d):
    """
    la fonction permet de créer un arbre où l'utilisateur peut choisir si l'arbre penche d'un coté ou de l'autre.
    rapport_g: permet de choisir la rapport de hauteur du coté gauche
    rapport_d: permet de choisir la rapport de hauteur du coté droit
    angle_g: permet de choisir l'angle de l'arbre du coté gauche
    angle_d: permet de choisir l'angle de l'arbre du coté droite
    
    paramètres d'entrée:
    hauteur: doit etre un nombre positif 
    profondeur: doit etre un nombre positif
    epaisseur: doit etre un nombre positif
    angle_g: doit etre un nombre
    angle_d: doit etre un nombre
    rapport_g: doit etre un nombre positif
    rapport_d: doit etre un nombre positif
    """
    
    
    # Permet de faire les tests pour savoir si la fonction est correctement parametrée
    if isinstance(hauteur,(int,float)) == False or isinstance(profondeur,(int,float)) == False or isinstance(epaisseur,(int,float)) == False or isinstance(angle_g,(int,float)) == False or isinstance(angle_d,(int,float)) == False or isinstance(rapport_g,(int,float)) == False or isinstance(rapport_d,(int,float)) == False:
        raise Exception("les valeurs entrées doit être des nombres")
    
    if hauteur <=0 or profondeur <=0 or epaisseur <=0  or rapport_g <=0 or rapport_d <=0:
        raise Exception("les valeur entrées (sauf les valeurs pour les angles) doivent être positives")
    
    
    a=tl.pensize()
    w=tl.pencolor()
    tl.pensize(epaisseur)

    # La partie de code suivant permet de tracer l'arbre. On va commancer par tracer les branches puis les feuilles
    if profondeur == 1: # Permet de dessiner les feuilles de l'arbre
        tl.pencolor("green")
        tl.fd(hauteur)
        tl.bk(hauteur)
        
    elif profondeur >= 2: # permet de dessiner les branches de l'arbre de façon recursive.
        tl.pencolor("sienna")
        tl.fd(hauteur)
        tl.lt(angle_g)
        arbre(hauteur*rapport_g,profondeur-1,epaisseur*0.7,angle_g,angle_d,rapport_g,rapport_d)
        tl.rt(angle_g + angle_d)
        arbre(hauteur*rapport_d,profondeur-1,epaisseur*0.7,angle_g,angle_d,rapport_g,rapport_d)
        tl.lt(angle_d)
        tl.bk(hauteur)
        
    tl.pensize(a)
    tl.pencolor(w) 
        


# Programme principal
# modifier l'appel à la fonction arbre pour de nouvlles images
tl.tracer(0)
tl.lt(90)

arbre(100,10,16,20,35,0.7,0.8)
#arbre(100,10,16,90,35,0.8,0.3)

tl.update()
tl.mainloop()





















