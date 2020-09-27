from projection import Projection
import numpy as np

class Lots_Of_Dots():
    def __init__(self, pole):
        self.__pole = pole
        self.dot_create()
    
    def __repr__(self):
        return f'Lots_Of_Dots({self.__pole})'
    
    @property
    def pole(self):
        return self.__pole
    
    @property
    def dsphere(self):
        return self.__dotsonsphere
    
    @property
    def dots(self):
        return self.__dots
             
    
    def dot_create(self, nmax=3):
        """
        input pole in string type and the maximum index, 
        an array of dots on the pole circle be the property of self.dot
        """
        a = []
        for x in range(-nmax, nmax+1):
            for y in range(-nmax, nmax+1):
                for z in range(-nmax, nmax+1):
                    if np.dot(self.__pole, [x, y, z]) == 0:
                        a.append([x, y, z])
        v = a.copy()
        for element in a:
            for bv in range (2, nmax+1):
                if list(np.array(element)/bv) in v:
                    v.remove(element)
                    break
        self.__dots = np.array(v)
        self.__dotsonsphere = np.array([Projection(n).p100() for n in self.dots])

    def dot100(self):
        bln = np.dot(self.__dotsonsphere, [1,0,0]) >= 0
        self.ts = self.dsphere[bln]
        self.td = self.dots[bln]
        return np.array([Projection(n).apt100() for n in self.ts])
    
    def dot110(self):
        bln = np.dot(self.dots, [1,1,0]) >= 0
        self.ts = self.dsphere[bln]
        self.td = self.dots[bln]
        return np.array([Projection(n).apt110() for n in self.ts])
    
    def dot111(self):
        bln = np.dot(self.dots, [1,1,1]) >= 0
        self.ts = self.dsphere[bln]
        self.td = self.dots[bln]
        return np.array([Projection(n).apt111() for n in self.ts])