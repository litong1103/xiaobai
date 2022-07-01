"""
Created on Fri Apr 9 2021

@author: Juan Cervino
"""
#生成一个有向循环图，表示为Adc。编写一个类，以节点数N作为输入，以输出无权有向循环图的邻接矩阵作为输出。代码可以实现如下：
import numpy as np
import cmath


class matrix:
    def __init__(self,N):
        self.N=N

class directCycle(matrix):
    def __init__(self,N):
        super().__init__(N)
        #用例:numpy.tril(m, k=0) 功能:返回数组的下三角部分。将其第k条对角线上方的元素全部置零。
        self.A=np.tril(np.ones((self.N,self.N)),-1)-np.tril(np.ones((self.N,self.N)),-2)
        self.A[0,self.N-1] = 1

class fourier(matrix):
    def __init__(self,N):
        #调用父类(超类)的一个方法
        super().__init__(N)
        #numpy.outer(a, b) 求外积
        self.F=np.outer(np.arange(self.N),np.arange(self.N))
        self.F=(1/np.sqrt(N))*np.exp(2j*cmath.pi*self.F / self.N)
