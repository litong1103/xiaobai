"""
Created on Fri Apr 9 2021

@author: Juan Cervino
"""

import numpy as np

class GFT:
    def __init__(self,S):
        self.S=S
        [self.eigs,self.V]=np.linalg.eig(S)
        self.V=self.V[:,np.argsort(self.eigs)]
        self.eigs=np.sort(self.eigs)
        self.Lambda=np.diag(self.eigs)

    def computeGFT(self,x,k=None):
        xt=np.conj(self.V.T) @ x
        if k==None:
            return xt
        else:
            xtk = np.zeros_like(xt)
            xtk[np.argsort(np.abs(xt[:, 0]))[-k:], 0] = xt[np.argsort(np.abs(xt[:, 0]))[-k:], 0]
            return xtk

    def computeiGFT(self,xt, k=None):
        if k==None:
            return self.V@xt
        else:
            return self.V[:,np.argsort(np.abs(xt[:,0]))[-k:]]@xt[np.argsort(np.abs(xt[:,0]))[-k:],0]

    def computeTotalVariation(self,x):
        #x.T转置
        return x.T@(self.S)@x
