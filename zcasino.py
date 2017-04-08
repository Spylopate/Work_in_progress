#import os #pour windows
from random import randrange
from math import ceil
import functions.function

argent = 1000 # somme de départ du client
continuer_partie = True 

print("La partie commence, vous etes assis à une table avec ", argent, "$")

while continuer_partie:
	nb_mise = -1
	while nb_mise < 0 or nb_mise > 49:
		nb_mise = input("Entrez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
		try :
			nb_mise = int(nb_mise)
		except ValueError:
			print("Ceci n'est pas un nombre ! ")
			nb_mise = -1
			continue
		if nb_mise < 0 :
			print("trop petit !")
		if nb_mise > 49:
			print("chiffre trop grand")

#on demande combien le client veut miser :
	mise = 0
	while mise <= 0 or mise > argent:
		mise = input("Combien voulez vous miser")
		try:
			mise = int(mise)
		except ValueError:
			print("ce n'est pas un nombre")
			mise = 0
			continue
		if mise >= 0 or mise <= argent:
			print(" Vous ne pouvez pas miser ca !")
		else:
			print("vous misez :", mise)




	numero_win = randrange(50)
	print("La boule est tombée sur le numero : ",numero_win)

	if numero_win == nb_mise:
		print("Bravo tu as gagner :", mise * 3, "$ !")
		argent += mise * 3
	elif numero_win % 2 == nb_mise % 2:
		mise = ceil(mise * 0.5)
		print("Vous avez misé sur la bonne couleur, vous gagné : ", mise, " $")
		argent += mise
	else:
		print("Dommage vous avez perdu")	
		argent -= mise

	if argent <= 0:
		print("Vous etes ruiné !! aurevoir")
		continuer_partie = False
	else:
		print("vous avez actuellement ", argent, " $")
		quitter = input("Voulez vous quitter ? (o/n)")
		if quitter == "o" or quitter == "O":
			print(" A bientot !!")
			continuer_partie = False

















#os.system("pause") #pour windows
