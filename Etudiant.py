class Etudiant:
    
    def __init__(self, coords, partie):
        self.coords = coords
        self.point_passage = 0
        self.partie = partie


    def avancer(self):
        
        prochain_point_passage = self.partie.carte.chemin[self.point_passage + 1]
        
        
        self.coords = [nouv_x, nouv_y]