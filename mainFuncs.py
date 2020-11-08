"""
TriTout
Logiciel de tri de fichiers : Photos, Vidéos, Musiques, etc.

Début 26.04.20

Pour générer le script py à partir du fichier de Qt Creator
	pyuic5 gui.ui -x -o gui.py

WIP : Nouvelle GUI, filtres de recherche
		- Fonctions de connect
		- Lier les filtres aux utilisations réelles:
			- modifDate
			- fileSize

ToDo:
x Récursivité de la recherche des dossiers

x Trouver les doublons
	x Minimiser la liste des doublons (vérifier qu'un nouveau doublon
		n'était pas déjà dans la liste des doublons précédents)
	x Vérifier taille fichier pour ceux qui ont le même nom
	x Liste compréhensive des doublons
	- Filtrer les doublons à chercher:
		x Extension
		- Taille de fichier
		- Date

- Supprimer les doublons choisis
	x Mode simple : choisir pour chaque fichier (checkable listview)
	x Dossier fixé où seront supprimés des doublons (cas où il n'y a qu'un dossier dans la liste)
	x Désactiver les éléments supprimés dans la liste
	- Ordre des dossiers de suppression

- Implémenter la GUI
	x Choix des dossiers à inclure dans la recherche de doublons
	x Choix de recursivité
	x Dans quel dossier supprimer les doublons
	x Progress Bar
		x Pendant la recherche
		x Pendant la suppression
	x Rendre la liste des éléments en double cliquable (pour l'ouvrir par win)
	x Boites de dialogue:
		x Selectionner au moins un dossier
		x n double trouvé
		x n doubles ont été supprimés
	- Pouvoir supprimer un dossier de la liste des dossiers de recherche (tab 1)
	x Message d'alerte de suppression de la dernière copie
	- Dérouler un mode avancé:
		- Recherche doublons par filtres (date, ext, etc.)
		- Suppression doublons par dossiers etc.

- Pouvoir recommencer (reset toutes les listes etc)
x Mettre tout les chemins sous la même forme (os.path.abspath)

- Internationalisation des strings (qt + python)

"""

import os
from pathlib import Path

# Petit Failsafe
ENABLE_REAL_DEL = True
if ENABLE_REAL_DEL:
	print("REAL DELETE ENABLED WARNING !")

"""
Etablit la liste des fichiers dans les dossiers choisi et ajoute
des dossiers si la récursivité est activée

Args:
folderList: Liste des dossiers à parcourir
recursive: Booléen pour la recherche récursive
extList: Liste des extensions
inclExt: Si True, inclut seulement les extensions spécifiées
		Si False, exclut les extensions spécifiées

Retour:
Liste de liste de fichiers correspondant à chaque dossier de
folderList
"""
def mapFiles(folderList, recursive, extList=[], inclExt=None):
	# Nom des fichiers uniquement (la correspondance du dossier se fait avec l'indice)
	fileList = []

	for f in folderList:
		fileList.append([])

		# Liste des dossiers + fichiers du chemin f
		fullList = os.listdir(f)

		if len(fullList):
			for cf in fullList:
				fPath = os.path.join(f, cf)

				if os.path.isfile(fPath):  # Si fichier
					# Contrôle des extensions
					if inclExt is not None:
						splitted = cf.split(".") # Pour gérer les fichiers sans extension
						ext = splitted[-1] if len(splitted) else ""

						# Fichier accepté par le filtre des extensions
						if (inclExt and ext in extList) or (not inclExt and ext not in extList):
							fileList[-1].append(cf)
						"""
						else:
							print("Debug: Extension non désirée ", ext)
						"""

				elif recursive and fPath not in folderList:  # Si nv dossier + récursivité activée
					#print("Debug: Nouveau dossier trouvé: ", fPath)
					folderList.append(fPath)

	return fileList

"""
Nouvelle fonction pour maper les fichiers (en prenant en compte les tailles
et date de dernière modification)

Args:
folderList: Liste des dossiers à parcourir
recursive: Booléen pour la recherche récursive
extList: Liste des extensions
inclExt: Si True, inclut seulement les extensions spécifiées
		Si False, exclut les extensions spécifiées

Retour:
Liste de triplets : (fichier, taille, date dernière modif)
"""
def mapFiles2(folderList, recursive, extList=[], inclExt=None):
	# Nom des fichiers, taille et dernière modif
	fileList = []

	for f in folderList:
		fileList.append([])

		# Liste des dossiers + fichiers du chemin f
		fullList = os.listdir(f)

		if len(fullList):
			for cf in fullList:
				fPath = os.path.join(f, cf)

				if os.path.isfile(fPath):  # Si fichier
					# Contrôle des extensions activé ?
					if inclExt is not None:
						splitted = cf.split(".")  # Pour gérer les fichiers sans extension
						ext = splitted[-1] if len(splitted) else ""

						# Fichier accepté par le filtre des extensions
						if (inclExt and ext in extList) or (not inclExt and ext not in extList):
							fileList[-1].append((cf, os.path.getsize(fPath), os.path.getmtime(fPath)))

				elif recursive and fPath not in folderList:  # Si nv dossier + récursivité activée
					#print("Debug: Nouveau dossier trouvé: ", fPath)
					folderList.append(fPath)

	return fileList

"""
Trouve les doublons parmi la liste des fichiers

incrFunc: Fonction pour le suivi (progressbar)

Renvoie un dictionnaire où les keys sont les noms des fichiers en double
et les éléments associés sont les dossiers contenant le doublon
"""
def findDuplicates(folderList, fileList, incrFunc):
	dupFiles = dict()
	currIncr = 0

	# Pour la progressbar
	incr = 100 / len(fileList)

	for i in range(len(fileList)):
		f1 = set(fileList[i])

		for j in range(i+1, len(fileList)):
			f2 = set(fileList[j])

			# Intersection des ensembles : doublons
			for e in f1 & f2:
				# 1ère fois qu'on identifie ce doublon
				if e not in dupFiles:
					dupFiles[e] = [folderList[i], folderList[j]]

				# Ce doublon est déjà dans la liste : dossier déjà listé ?
				else:
					if folderList[i] not in dupFiles[e]:
						dupFiles[e].append(folderList[i])

					if folderList[j] not in dupFiles[e]:
						dupFiles[e].append(folderList[j])
		
				# Progressbar : pour gérer les incréments à virgule
				currIncr += incr
				if currIncr >= 1:
					incrFunc(int(currIncr))
					currIncr -= int(currIncr)

	return dupFiles

"""
Nouvelle fonction de détection des doubles
Utilise le nom du fichier, la taille et la date de dernière modification
pour trouver les doublons

Args:
folderList: Liste des dossiers
fileList: Liste des fichiers correspondant a folderList
incrFunc: Fonction d'incrément (pour progressbar)

Retourne une liste contenant une liste pour chaque fichier au format
[(nom_fichier, taille, date), [dossiers où ce fichier est présent]]
"""
def findDuplicates2(folderList, fileList, incrFunc):
	dupFiles = []
	currIncr = 0

	# Pour la progressbar
	incr = 100 / len(fileList)

	for i in range(len(fileList)):
		f1 = set(fileList[i])

		for j in range(i+1, len(fileList)):
			f2 = set(fileList[j])

			# Intersection des ensembles : doublons
			for e in f1 & f2:
				# 1ère fois qu'on identifie ce doublon
				if e not in dupFiles:
					dupFiles.append([e, [folderList[i], folderList[j]]])

				# Ce doublon est déjà dans la liste : dossier déjà listé ?
				else:
					ind = dupFiles.index(e)
					if folderList[i] not in dupFiles[ind][1]:
						dupFiles[ind][1].append(folderList[i])

					if folderList[j] not in dupFiles[ind][1]:
						dupFiles[ind][1].append(folderList[j])

				# Progressbar : pour gérer les incréments à virgule
				currIncr += incr
				if currIncr >= 1:
					incrFunc(int(currIncr))
					currIncr -= int(currIncr)

	return dupFiles

def beautifyDict(dictio):
	beau = []
	
	for key, elem in dictio.items():
		beau += [key] + ["\t"+e for e in elem]
	
	return beau

"""
Supprime la liste des fichiers spécifiés dans la liste
"""
def delFiles(delPathList, incrFunc):
	delCpt = 0
	currIncr = 0
	incr = 100 / len(delPathList)

	deletedList = []

	permError = False

	for i in range(len(delPathList)):
		#print("Removing ", p)
		if ENABLE_REAL_DEL:
			try:
				os.remove(delPathList[i])
			# On préviendra alors l'utilisateur qu'on a pas pu supprimer car un fichier est ouvert
			except PermissionError as e:
				permError = True
			else:
				deletedList.append(delPathList[i])
				delCpt += 1

		# Progressbar : pour gérer les incréments à virgule
		currIncr += incr
		if currIncr >= 1:
			incrFunc(int(currIncr))
			currIncr -= int(currIncr)
	
	return deletedList, delCpt, permError

"""

PARTIE DE CODE DESTINEE AU DEBUG DU CODE SANS GUI

"""
"""
# Liste des dossiers à inclure dans la recherche de doublons (à récup GUI)
folders = ["C:/Users/Flyknit/Desktop/tri_tout_test"]

folders = [os.path.normpath(e) for e in folders]

print("Folder list: ", folders)

# Récursivité de la recherche (récup gui)
recSearch = True

fileList = mapFiles(folders, recSearch, lambda x: 1, ["txt"], 0)
print(fileList, "\n", folders, "\n")

dups = findDuplicates(folders, fileList)

print("Fichiers en double: ", list(dups.keys()))
print(dups)

print(delDuplicate(folders, dups, 1))
"""
