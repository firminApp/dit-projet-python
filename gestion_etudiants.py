# etudiants=[
#     {
# "nom": "DIOP",
# "prenom": "Aminata",
# "matricule": "DIT3657825",
# "notes": {
# "Python": 14,
# "Anglais": 16,
# "Data Collection": 12,
# "Machine Learning": 18
# }
# },
# {
# "nom": "SOW",
# "prenom": "Mamadou",
# "matricule": "DIT3657825",
# "notes": { 
# "Python": 10,
# "Anglais": 9,
# "Data Collection": 11,
# "Machine Learning": 13
# }
# },
# {
# "nom": "NDIAYE",
# "prenom": "Fatou",
# "matricule": "DIT3657825",
# "notes": {
# "Python": 18,
# "Anglais": 17,
# "Data Collection": 19,
# "Machine Learning": 16
# }
# }
# ]
# DIT+ 4 chiffres + 2 dernières lettre de l’année d’inscription
def list_etudiants(etudiants):
    return etudiants
def afficher_etudiants():
    for etudiant in etudiants:
        print(f"Nom: {etudiant['nom']}, Prénom: {etudiant['prenom']}, Matricule: {etudiant['matricule']}")
        for matiere, note in etudiant['notes'].items():
            print(f"  {matiere}: {note}")
        print()
def generer_matricule(annee_inscription=2025):
    prefixe="DIT"
    numero=len(etudiants)+1
    numero_str=str(numero).zfill(4)
    annee_str=str(annee_inscription)[-2:]
    matricule=f"{prefixe}{numero_str}{annee_str}"
    return matricule

def ajouter_etudiant():
    nom=input("Entrez le nom de l'étudiant: ")
    prenom=input("Entrez le prénom de l'étudiant: ")
    matricule=generer_matricule(2024)
    notes={}
    matieres=["Python", "Anglais", "Data Collection", "Machine Learning"]
    for matiere in matieres:
        note=float(input(f"Entrez la note en {matiere}: "))
        notes[matiere]=note
    etudiant={
        "nom": nom, 
        "prenom": prenom,
        "matricule": matricule,
        "notes": notes
    }
    etudiants.append(etudiant)
    print("Étudiant ajouté avec succès.")

def modifier_note(matricule, nouvelle_note):
    for etudiant in etudiants:
        if etudiant['matricule']==matricule:
            matieres=["Python", "Anglais", "Data Collection", "Machine Learning"]
            for matiere in matieres:
                note=float(input(f"Entrez la note en {matiere}: "))
                notes[matiere]=note
            etudiant={
                "nom": nom, 
                "prenom": prenom,
                "matricule": matricule,
                "notes": notes
                }
            etudiants.append(etudiant)
            print("Étudiant modifié avec succès.")
            return
        else:
            print("Matière non trouvée.")
            return
    print("Étudiant non trouvé.")


def calculer_moyenne(etudiant):
    total=0
    for note in etudiant['notes'].values():
        total+=note
    moyenne=total/len(etudiant['notes'])
    return moyenne
def determiner_mention(moyenne):
    if moyenne>=16:
        return "Très Bien"
    elif moyenne>=14:
        return "Bien"
    elif moyenne>=12:
        return "Assez Bien"
    elif moyenne>=10:
        return "Passable"
    else:
        return "Échec"  
# Générer un bulletin individuel en fichier texte (.txt)
def generer_bulletin(etudiant):
    moyenne=calculer_moyenne(etudiant)
    mention=determiner_mention(moyenne)
    with open(f"bulletins/{etudiant['matricule']}.txt", "w") as f:
        f.write(f"Bulletin de {etudiant['prenom']} {etudiant['nom']}\n")
        f.write(f"Matricule: {etudiant['matricule']}\n\n")
        f.write("Notes:\n")
        for matiere, note in etudiant['notes'].items():
            f.write(f"  {matiere}: {note}\n")
        f.write(f"\nMoyenne Générale: {moyenne:.2f}\n")
        f.write(f"Mention: {mention}\n")
    print(f"Bulletin généré pour {etudiant['prenom']} {etudiant['nom']}.")

# Sauvegarder tous les étudiants dans etudiants.txt
def sauvegarder_etudiants():
    with open("etudiants.txt", "w") as f:
        for etudiant in etudiants:
            f.write(f"{etudiant['nom']},{etudiant['prenom']},{etudiant['matricule']}\n")
            for matiere, note in etudiant['notes'].items():
                f.write(f"{matiere}:{note},")
            f.write("\n")
    print("Étudiants sauvegardés dans etudiants.txt.")  
# Charger à nouveau les données depuis ce fichier
def charger_etudiants():
    etudiants_charges=[]
    try:
        with open("etudiants.txt", "r") as f:
            lignes=f.readlines()
            for ligne in lignes:
                parties=ligne.strip().split("\n")
                nom, prenom, matricule=parties[0].split(",")
                notes_parties=parties[1].split(",")[:-1]
                notes={}
                for note_partie in notes_parties:
                    matiere, note=note_partie.split(":")
                    notes[matiere]=float(note)
                etudiant={
                    "nom": nom,
                    "prenom": prenom,
                    "matricule": matricule,
                    "notes": notes
                }
                etudiants_charges.append(etudiant)
        print("Étudiants chargés depuis etudiants.txt.")
    except FileNotFoundError:
        print("Fichier etudiants.txt non trouvé.")
    return etudiants_charges

# Rechercher un étudiant par matricule
def rechercher_etudiant(matricule):
    for etudiant in etudiants:
        if etudiant['matricule']==matricule:
            return etudiant
    return None
#  afficher les etudiants admis (moyenne >=10)
def afficher_admis():
    for etudiant in etudiants:
        moyenne=calculer_moyenne(etudiant)
        if moyenne>=10:
            print(f"Nom: {etudiant['nom']}, Prénom: {etudiant['prenom']}, Matricule: {etudiant['matricule']}, Moyenne: {moyenne:.2f}")  
