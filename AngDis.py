# This code calculates angular diameter distances in a flat universe.

import numpy,scipy
import scipy.integrate 



class Distance:
    def __init__(self,Omega_M=0.3,Omega_L=0.7,h=0.7,H0=100.):
        self.Omega_L = Omega_L
        self.Omega_M = Omega_M
        self.h = h
        self.H0=H0
        self.coverh0=3000/h
        

    def friedmann(self,a):
        """ Returns (H/H_0)^2 evaluated for a definite value of a """
        return (self.Omega_M/a**3 + self.Omega_L)

    def ang_dis_int(self,a):
    
        return (self.coverh0/(a*a*numpy.sqrt(self.friedmann(a))))

    def ang_dis(self,z1,z2):
        #print z1,z2
        #assert(z1<z2)
        if ((z1>z2) or (z1==z2)): 
            return 0
        else:
            a1=1/(1+z2)
            a2=1/(1+z1)
        return (scipy.integrate.quad(self.ang_dis_int,a1,a2)[0])
