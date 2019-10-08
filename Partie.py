class Partie:
    
    
    def __init__(self, carte):
        self.carte = carte
        self.etudiants = []


    def ajouterEtudiant(self, etudiant):
        self.etudiants += [etudiant]
    
    def retirerEtudiant(self, etudiant):
        self.etudiants.remove(etudiant)



    def rafraichir(self):
        
        for etudiant in self.etudiants:
            etudiant.avancer()