import numpy as np #librairi 
import matplotlib.pyplot as plt #pour les illustration graphiqie
import random as rd# pour generer aleatoirement les cordonnees des point des villes quand on descine les villes par des points ....
import tkinter as tk # pour créer votre interface graphique




# Demander à l'utilisateur le nombre de villes à générer
# simpledialog.askinteger("Nombre de villes", "Entrez le nombre de villes à générer :")
while True:
        try:
            num_cities = int(simpledialog.askstring("Nombre de villes", "Entrez le nombre de villes à générer :"))
            if num_cities > 0:
                N= num_cities
                break
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier.")





 # DIMENSION DE LA POPULATION
while True:
        try:
            dimension_population = int(simpledialog.askstring("Dimension population", "Entrez la Dimension de la population :"))
            if dimension_population > 0:
                M= dimension_population
                break
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier.")
#k=0 #compteur pour la boucle apres
villes_dessinees = False  # Variable globale pour suivre si les villes ont été dessinées ou non




                    #     2  Evaluation de la "fitness" (qualité) des individus

# la fonction fitness : pour evaluer chaque chromosome(individue)
def fitness():# calcule la distance totale parcourue en suivant le chemin représenté par les indices de la variable chemin
    global chemin
    distance = 0.0
    xy=np.column_stack((x[chemin],y[chemin])) # Cette ligne crée un tableau bidimensionnel où chaque ligne représente les coordonnées (x, y) d'une ville dans l'ordre défini par le chemin actuel. La fonction np.column_stack() est utilisée pour empiler les tableaux x et y sur les colonnes, de sorte que chaque colonne contienne les coordonnées (x, y) d'une ville.
    distance=np.sum(np.sqrt(np.sum((xy- np.roll(xy,-1,axis=0))**2,axis=1))) # alcule la distance totale parcourue en suivant le chemin défini par les indices de la variable chemin. Elle utilise la fonction np.roll() pour décaler les éléments du tableau xy d'une position vers le haut, de sorte que la première ville visite la deuxième, la deuxième visite la troisième, et ainsi de suite. Ensuite, elle calcule la distance entre chaque paire de villes consécutives, puis somme ces distances pour obtenir la distance totale parcourue.
    return distance # la distance totale calculée comme mesure de fitness de l'individu.
"""J'ai défini une fonction pour calculer la distance entre deux villes. 
J'ai utilisé une formule de distance, telle que la distance euclidienne 
dans un espace bidimensionnel, car mes villes sont représentées par des coordonnées.
J'ai utilisé cette fonction pour calculer la distance totale parcourue par chaque individu dans la population.
J'ai noté que plus la distance est courte, meilleure est la fitness de l'individu. J'ai donc inversé la distance 
(par exemple, en prenant l'inverse de la distance) pour obtenir un score de fitness où une valeur plus élevée indique
 une meilleure adaptation.
J'ai attribué à chaque individu son score de fitness calculé.
J'ai répété ce processus pour tous les individus de la population.
"""


#+++++++
# les villes et leurs cordonnees , (chaque ville est représentée par ses coordonnées x et y dans un espace bidimensionnel)
x=np.random.uniform(0,1,N)#NumPy pour générer des coordonnées x et y aléatoires dans l'intervalle [0, 1] pour N villes
y=np.random.uniform(0,1,N)
chemin = np.arange(N)#crée un tableau NumPy contenant une séquence de nombres allant de 0 à N-1, représentant l'ordre initial dans lequel les villes sont visitées.




                  #    determiner la population initiale et le calcul de la fitness sur cette population

print('\n\n\n           MA POPULATION INITIAL ou chaque element et ca fitness calculer : \n\n\n  ')
population =[]  # une liste de listes représentant la population d'individus. Chaque individu est lui-même une liste représentant un chemin à travers les villes.la population c'est un ensmble de chromosome (on a 100) et chaque chromosome a 100 genes == on utilise une matrice
for i in range(0,M,1) : # iterer avec i de 0 a M en avancant de 1
    #iniialiser la matrice : 
    population.append([0]*N)#append ajoute un element a la matrice
    for j in range(0,N,1) :
        villeVisiter=1   #booleen je l'utilise pour ne pas avoir de redendance de ville dans le meme parcours(qui est une contrainte de porbleme de voyageur)  pour controler le choix du numero
        if j == 0 : 
            element=rd.randint(0,N-1)# (rd=random) ranint donne un entier random car les element de la population c'est des int
        else : 
            while villeVisiter==1 :# tant que =1 repeter le randint
                element =rd.randint(0,N-1)
                cmpt=0 #un petit compteur pour compter le nombre de redendance de chque numero deja rempli 
                for k in range(0,j,1):# pour verifier les element deja remplie de 0 a J car on remplie jusqua maintenat jusqua j 
                    if population[i][k]==element :# si il y'a un element deja chosi egale au nombre random donner alors : 
                        villeVisiter=1
                        cmpt=cmpt+1
                if cmpt==0: villeVisiter=0

        population[i][j]=element
        chemin[j]= population[i][j]
        d=fitness()
    print('chromosome numero ',i+1, population[i],'fitness = ', d)