import numpy as np

class Projection():
    tmatrix111 = np.array([[ 2/3, -1/3, -1/3],
                           [-1/3,  2/3, -1/3],
                           [-1/3, -1/3,  2/3]])
    
    tmatrix110 = np.array([[1/2, -1/2, 0],
                           [-1/2, 1/2, 0],
                           [   0,   0, 1]])
    
    def __init__(self,vector):
        self.__x = vector[0]
        self.__y = vector[1]
        self.__z = vector[2]
        self.__pos = np.array(vector)
        self.__length = sum(self.pos**2)**0.5
    
    @property
    def pos(self):
        return self.__pos
    
    def p100(self):
        cor = self.__pos / self.__length
        return cor
    
    def pt100(self):
        sph_cor = self.p100()
        sph_cor[0] += 1 
        #projection from(-1 0 0), vector
        fraction = 1/ sph_cor[0] 
        #expand to x = 1 plane
        return(sph_cor * fraction)
    
    def pt111(self):
        sph_cor = self.p100()
        sph_cor += 1
        return np.dot(sph_cor, Projection.tmatrix111)
    
    def pt110(self):
        sph_cor = self.p100()
        sph_cor[:2] += 1
        return np.dot(sph_cor, Projection.tmatrix110)

    def apt100(self):
        sph_cor = self.__pos
        sph_cor[0] += 1 
        #projection from(-1 0 0), vector
        fraction = 1/ sph_cor[0] 
        #expand to x = 1 plane
        return(sph_cor * fraction)
    
    def apt110(self):
        sph_cor = self.__pos
        sph_cor[:2] += 1
        return np.dot(sph_cor, Projection.tmatrix110)
    
    def apt111(self):
        sph_cor = self.__pos
        sph_cor += 1
        return np.dot(sph_cor, Projection.tmatrix111)