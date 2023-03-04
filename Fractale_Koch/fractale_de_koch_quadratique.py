import turtle as t # Importe le module turtle en le renommant 't'

# Fonction récursive pour dessiner une fractale de Koch quadratique
def fractale_koch_quadratique(n_actuel: int, n_total: int, taille: float) -> None:
    """
    Dessine une fractale de Koch quadratique de façon récursive.
    
    Args:
    - n_actuel (int): la profondeur de la récursion actuelle.
    - n_total (int): la profondeur de la récursion souhaitée.
    - taille (float): la longueur du segment de base de la fractale.
    
    Returns:
    - None.
    """
    if n_actuel != n_total: # Condition de sortie de la récursion
        # Dessine les côtés gauche, haut, droite et bas de la fractale
        fractale_koch_quadratique(n_actuel+1, n_total, taille/4) # Côté gauche
        t.left(90)
        fractale_koch_quadratique(n_actuel+1, n_total, taille/4) # Côté haut
        t.right(90)
        fractale_koch_quadratique(n_actuel+1, n_total, taille/4) # Côté droit
        t.right(90)
        fractale_koch_quadratique(n_actuel+1, n_total, taille/4) # Côté bas
        fractale_koch_quadratique(n_actuel+1, n_total, taille/4) # Segment central
        t.left(90)
        fractale_koch_quadratique(n_actuel+1, n_total, taille/4) # Côté bas
        t.left(90)
        fractale_koch_quadratique(n_actuel+1, n_total, taille/4) # Côté gauche
        t.right(90)
        fractale_koch_quadratique(n_actuel+1, n_total, taille/4) # Côté haut
    else: # Cas de base de la récursion
        t.forward(taille) # Dessine un côté de la fractale

# Fonction pour dessiner une fractale de Koch quadratique dans un carré
def fractale_carre(n: int, d: float) -> None:
    """
    Dessine une fractale de Koch quadratique dans un carré de taille 'd' avec une profondeur de récursion 'n'.
    
    Args:
    - n (int): la profondeur de la récursion souhaitée.
    - d (float): la longueur du côté du carré contenant la fractale.
    
    Returns:
    - None.
    """
    for i in range(4): # Pour chaque côté du carré
        fractale_koch_quadratique(0, n, d) # Dessine une fractale de Koch quadratique
        t.right(90) # Tourne à droite de 90 degrés pour dessiner le côté suivant

t.tracer(0, 0) # Désactive l'animation pour que la figure soit dessinée instantanément

fractale_carre(5, 200) # Dessine une fractale de Koch quadratique dans un carré de taille 200, avec une profondeur de récursion de 5

t.update() # Met à jour l'écran pour afficher la figure dessinée
