import os

# Fonction qui présente le JEU
def Presentation(nb):
    print(' BIENVENU DANS LE JEU DU PENDU \n LE BUT DU JEU EST DE TROUVER UN MOT CACHE DE ' + str(nb) + ' LETTRES' )
	
#Fonction qui dessine le Pendu
def GraphPendu(index,max=8):
    if 0 <= index <max:
        liste=['',\
			   ' ______\n|      |\n|\n|\n|\n|\n|______________',\
               ' ______\n|      |\n|      O\n|\n|\n|\n|______________',\
               ' ______\n|      |\n|      O\n|      |\n|\n|\n|______________',\
               ' ______\n|      |\n|      O\n|     /|\n|\n|\n|______________',\
               ' ______\n|      |\n|      O\n|     /|\\\n|\n|\n|______________',\
               ' ______\n|      |\n|      O\n|     /|\\\n|     / \n|\n|______________',\
               ' ______\n|      |\n|      O\n|     /|\\\n|     / \\\n|______________']
        print(liste[index])

# Programme principal
if __name__ == "__main__":

	#Variables
	Pendu = False
	chaine = "nad"
	Listchaine = []
	tempchaine=""
	mon_dictionnaire = {}
	i = 0
	tentative = 0
	tentativemax = 7

	#Remplissage du dictionnaire
	while i < len(chaine):
		Listchaine.append("*")
		if chaine[i] in mon_dictionnaire:
			mon_dictionnaire[chaine[i]].append(i)
		else:
			liste = []
			liste.append(i)
			mon_dictionnaire[chaine[i]] = liste
		i += 1

	tempchaine = ''.join(Listchaine)
	print(tempchaine)

	#Recherche du mot
	while tempchaine != chaine and Pendu == False:
		cherche = input('Taper une lettre : ')
		if cherche in mon_dictionnaire:
			for cle in mon_dictionnaire:
				if cle == cherche:
					i = 0
					indice = 0
					while i < len(mon_dictionnaire[cle]):
						indice = mon_dictionnaire[cle][i]
						Listchaine[indice] = cherche
						i +=1
		else:
			#GraphPendu(tentative)
			tentative += 1
		tempchaine = ''.join(Listchaine)
		if tempchaine == chaine:
			print('Félicitation!!!\nVous avez trouvé le mot : ' + tempchaine)
		else:
			print(tempchaine)
			GraphPendu(tentative)
		if tentative == tentativemax:
			Pendu = True
			print('PENDU!!!\nLe mot cherché était : ' + chaine)
		
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")