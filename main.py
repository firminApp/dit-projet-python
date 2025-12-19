# importer le module gestion_etudiants
import gestion_etudiants as ge

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
                ge.modifier_note(matricule)
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
            ge.generate_bulletins_classe()
        elif choix=="10":
            matricule=input("Entrez le matricule de l'étudiant: ")
            try:
                with open(f"bulletins/{matricule}.txt", "r") as f:
                    contenu=f.read()
                    print(contenu)
            except FileNotFoundError:
                print("Bulletin non trouvé.")
        else:
            print("Option invalide. Veuillez réessayer.")
if __name__=="__main__":
    main()
