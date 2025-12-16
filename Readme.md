# Présentation générale du projet
Ce projet consiste à développer un système complet de gestion des étudiants en Python. Le
programme permettra d’enregistrer les étudiants, saisir leurs notes, calculer les moyennes,
attribuer des mentions et générer des bulletins individuels au format texte (.txt). Ce projet
couvre les notions essentielles du semestre : listes, dictionnaires, boucles, fonctions,
fichiers, map/filter/lambda et organisation modulaire.
## Structure des données attendue
Chaque étudiant doit être représenté sous forme de dictionnaire :

        {
        "nom": "DIOP",
        "prenom": "Aminata",
        "matricule": "DIT3657825",
        "notes": {
        "Python": 14,
        "Anglais": 16,
        "Data Collection": 12,
        "Machine Learning": 18
        }
        }
## Fonctionnalités obligatoires
Le système devra obligatoirement permettre :
• Ajouter un étudiant avec matricule automatique en gardant le format donner en exemple
DIT+ 4 chiffres + 2 dernières lettre de l’année d’inscription
• Modifier ou saisir ses notes
• Calculer la moyenne générale
• Déterminer la mention
• Générer un bulletin individuel en fichier texte (.txt)
• Sauvegarder tous les étudiants dans etudiants.txt
• Charger à nouveau les données depuis ce fichier
• Rechercher un étudiant par matricule
• Afficher les étudiants admis
## Menu principal à implémenter
Le programme doit afficher le menu suivant :
========= SYSTEME DE GESTION SCOLAIRE =========
1. Ajouter un étudiant
2. Saisir / Modifier les notes d'un étudiant
3. Afficher tous les étudiants
4. Rechercher un étudiant par matricule
5. Afficher les étudiants admis
6. Sauvegarder les données
7. Charger les données
8. Générer le bulletin d’un étudiant
9. Générer les bulletins de toute la classe
10. Lire le bulletin d’un étudiant
0. Quitter
5. Format du bulletin à générer
Chaque bulletin devra être sauvegardé dans un dossier nommé bulletins/ sous la forme :
bulletins/MATRICULE.txt
NB : Vous êtes encouragés à concevoir un bulletin personnel et esthétique. Il peut être
sobre, artistique, encadré, structuré en tableau, ou organisé sous forme de certificat.
Donnez libre cours à votre créativité : l’objectif est de produire un document lisible et
agréable, tout en respectant le contenu obligatoire.
Exemple :
=====================================
BULLETIN DE NOTES
Nom : DIOP
Prénom : Aminata
Matricule : DIT3657825
--- Notes ---
Python : 14
Anglais : 16
Data Collection : 12
Machine Learning : 18
Moyenne générale : 15.0
Mention : Bien
=====================================
##  Contraintes techniques
• L’utilisation des dictionnaires est obligatoire.
• Un module Python (gestion_etudiants.py) doit contenir toutes les fonctions.
• Le fichier principal (main.py) doit importer ce module.
## Livrables attendus
Vous devez fournir :
-  Le dossier complet du projet
-  main.py
-  gestion_etudiants.py
-  etudiants.txt
-  Le dossier bulletins/ contenant les fichiers générés
-  Un fichier contenant les membres du groupe