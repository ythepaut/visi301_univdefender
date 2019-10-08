class Etudiant:
    
    def __init__(self, coords, partie):
        self.coords = coords
        self.point_passage = 0
        self.partie = partie


    def avancer(self):



        if self.point_passage >= len(self.partie.carte.chemin) - 1: #Dernier point passage atteint ?

            self.partie.retirerEtudiant(self)

        else:

            prochain_point_passage = self.partie.carte.chemin[self.point_passage + 1]

            dir_x = prochain_point_passage[0] - self.coords[0]
            dir_y = prochain_point_passage[1] - self.coords[1]
            
            if (abs(dir_x) + abs(dir_y) <= 1):    #Point de passage atteint ?
                self.point_passage += 1
            

            deplacement_x = max(-1, min(1, dir_x))
            deplacement_y = max(-1, min(1, dir_y))

            self.coords = [self.coords[0] + deplacement_x * 2, self.coords[1] + deplacement_y * 2]
