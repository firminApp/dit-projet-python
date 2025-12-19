#  liste initiale
etudiants=[
{
"nom": "DIOP",
"prenom": "Aminata",
"matricule": "DIT3657825",
"notes": {
"Python": 14,
"Anglais": 1,
"Data Collection": 2,
"Machine Learning": 8
}
},
{
"nom": "SOW",
"prenom": "Mamadou",
"matricule": "DIT3657925",
"notes": { 
"Python": 10,
"Anglais": 9,
"Data Collection": 11,
"Machine Learning": 13
}
},
{
"nom": "NDIAYE",
"prenom": "Fatou",
"matricule": "DIT3651025",
"notes": {
"Python": 18,
"Anglais": 17,
"Data Collection": 19,
"Machine Learning": 16
}
}
]
def list_etudiants(etudiants):
    return etudiants
def afficher_etudiants():
    for etudiant in etudiants:
        print(f"Nom: {etudiant['nom']}, Prénom: {etudiant['prenom']}, Matricule: {etudiant['matricule']}")
        for matiere, note in etudiant['notes'].items():
            print(f"  {matiere}: {note}")
        print()
# DIT+ 4 chiffres + 2 dernières lettre de l’année d’inscription
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
    sauvegarder_etudiants()
    print("Étudiant ajouté avec succès.")

def modifier_note(matricule):
    for etudiant in etudiants:
        if etudiant['matricule']==matricule:
            matieres=["Python", "Anglais", "Data Collection", "Machine Learning"]
            for matiere in matieres:
                note=float(input(f"Entrez la note en {matiere}: "))
                notes=etudiant['notes']
                notes[matiere]=note
            etudiant={
                "nom": etudiant['nom'], 
                "prenom": etudiant['prenom'],
                "matricule": matricule,
                "notes": notes
                }
            etudiants.append(etudiant)
            print("Étudiant modifié avec succès.")
            return
        else:
            print("Matière non trouvée.")
            return
    sauvegarder_etudiants()
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
    largeur_totale = 70
    largeur_matiere = 45
    largeur_note = largeur_totale - largeur_matiere - 3  # 3 pour les bordures
    
    with open(f"bulletins/{etudiant['matricule']}.txt", "w") as f:
        # En-tête
        f.write("╔" + "═" * (largeur_totale - 2) + "╗\n")
        f.write("║" + "BULLETIN SCOLAIRE".center(largeur_totale - 2) + "║\n")
        f.write("╠" + "═" * (largeur_totale - 2) + "╣\n")
        f.write("║" + " " * (largeur_totale - 2) + "║\n")
        
        # Informations étudiant
        nom_line = f"  Nom: {etudiant['nom']}"
        f.write("║" + nom_line.ljust(largeur_totale - 2) + "║\n")
        prenom_line = f"  Prénom: {etudiant['prenom']}"
        f.write("║" + prenom_line.ljust(largeur_totale - 2) + "║\n")
        matricule_line = f"  Matricule: {etudiant['matricule']}"
        f.write("║" + matricule_line.ljust(largeur_totale - 2) + "║\n")
        f.write("║" + " " * (largeur_totale - 2) + "║\n")
        
        # Tableau des notes
        f.write("╠" + "═" * (largeur_totale - 2) + "╣\n")
        header_line = "MATIÈRE".center(largeur_matiere) + "│" + "NOTE".center(largeur_note)
        f.write("║" + header_line + "║\n")
        f.write("╠" + "═" * largeur_matiere + "╪" + "═" * largeur_note + "╣\n")
        
        for matiere, note in etudiant['notes'].items():
            matiere_cell = f"  {matiere}".ljust(largeur_matiere)
            note_cell = f"{note:.2f}".center(largeur_note)
            f.write("║" + matiere_cell + "│" + note_cell + "║\n")
        
        # Résultats
        f.write("╠" + "═" * (largeur_totale - 2) + "╣\n")
        f.write("║" + " " * (largeur_totale - 2) + "║\n")
        
        moyenne_line = f"  Moyenne Générale: {moyenne:.2f}"
        f.write("║" + moyenne_line.ljust(largeur_totale - 2) + "║\n")
        mention_line = f"  Mention: {mention}"
        f.write("║" + mention_line.ljust(largeur_totale - 2) + "║\n")
        f.write("║" + " " * (largeur_totale - 2) + "║\n")
        f.write("╚" + "═" * (largeur_totale - 2) + "╝\n")
    print(f"Bulletin généré pour {etudiant['prenom']} {etudiant['nom']}.")

# Sauvegarder tous les étudiants dans etudiants.txt
def generate_bulletins_classe():
    for etudiant in etudiants:
        generer_bulletin(etudiant)
    print("Bulletins de toute la classe générés.")

def afficher_etudiant(etudiant):
    print(f"Nom: {etudiant['nom']}, Prénom: {etudiant['prenom']}, Matricule: {etudiant['matricule']}")
    for matiere, note in etudiant['notes'].items():
        print(f"  {matiere}: {note}")
    moyenne=calculer_moyenne(etudiant)
    mention=determiner_mention(moyenne)
    print(f"Moyenne Générale: {moyenne:.2f}")
    print(f"Mention: {mention}")   

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
            i=0
            while i<len(lignes):
                if lignes[i].strip()=="":
                    i+=1
                    continue
                nom, prenom, matricule=lignes[i].strip().split(",")
                i+=1
                if i<len(lignes):
                    notes_parties=lignes[i].strip().split(",")[:-1]
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
                i+=1
        print("Étudiants chargés depuis etudiants.txt.")
        global etudiants
        etudiants=etudiants_charges
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
