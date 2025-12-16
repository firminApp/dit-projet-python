# importer le module gestion_etudiants
import gestion_etudiants as ge
'''
 Menu principal à implémenter
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
'''
def main():
    etudiants=[]
    while True:
        print("========= SYSTEME DE GESTION SCOLAIRE =========")
        print("1. Ajouter un étudiant")
        print("2. Saisir / Modifier les notes d'un étudiant")
        print("3. Afficher tous les étudiants")
        print("4. Rechercher un étudiant par matricule")
        print("5. Afficher les étudiants admis")
        print("6. Sauvegarder les données")
        print("7. Charger les données")
        print("8. Générer le bulletin d’un étudiant")
        print("9. Générer les bulletins de toute la classe")
        print("10. Lire le bulletin d’un étudiant")
        print("0. Quitter")
        choix=input("Choisissez une option: ")
        
        if choix=="0":
            print("Au revoir!")
            break
        elif choix=="1":
            etudiant=ge.ajouter_etudiant()
            etudiants.append(etudiant)
        elif choix=="2":
            matricule=input("Entrez le matricule de l'étudiant: ")
            etudiant=ge.rechercher_etudiant(matricule)
            if etudiant:
                ge.saisir_notes(etudiant)
            else:
                print("Étudiant non trouvé.")
        elif choix=="3":
            ge.afficher_etudiants()
        elif choix=="4":
            matricule=input("Entrez le matricule de l'étudiant: ")
            etudiant=ge.rechercher_etudiant(matricule)
            if etudiant:
                ge.afficher_etudiant(etudiant)
            else:
                print("Étudiant non trouvé.")
        elif choix=="5":
            ge.afficher_admis()
        elif choix=="6":
            ge.sauvegarder_etudiants()
        elif choix=="7":
            etudiants=ge.charger_etudiants()
        elif choix=="8":
            matricule=input("Entrez le matricule de l'étudiant: ")
            etudiant=ge.rechercher_etudiant(matricule)
            if etudiant:
                ge.generer_bulletin(etudiant)
            else:
                print("Étudiant non trouvé.")
        elif choix=="9":
            for etudiant in etudiants:
                ge.generer_bulletin(etudiant)
        elif choix=="10":
            matricule=input("Entrez le matricule de l'étudiant: ")
            try:
                with open(f"{matricule}.txt", "r") as f:
                    contenu=f.read()
                    print(contenu)
            except FileNotFoundError:
                print("Bulletin non trouvé.")
        else:
            print("Option invalide. Veuillez réessayer.")
if __name__=="__main__":
    main()
