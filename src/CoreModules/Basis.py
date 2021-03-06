import numpy as np
import matplotlib.pyplot as plt
#import BasisFunction as bf

class basis:
    # It's a constructor, innit! #
    def __init__(self, basis_functions, min_size = 10):
        self.basis_functions = basis_functions
        self.basis_size = [min_size for i in range (len(basis_functions))]
        
    #def add_basis_function(basis_function)
    
    def set_basis_size(self, ns):
        self.basis_size = ns
        
    def evaluate_basis(self, k, x, y):
        result = []
        sz = len(self.basis_size)
        for i in range(sz):
            n = self.basis_size[i]
            bf = self.basis_functions[i]
            #A =  np.array([bf.f(j,k,x,y,n = n) for j in range(n)])/np.sqrt(n)
            js = [j for j in range(n)]
            A = np.array(list(map(lambda j: bf.f(j,k,x,y,n = n), js)))/np.sqrt(n)
            result.append(A)
    
        return np.concatenate(result)
    
    def evaluate_u(self, k, x, y, nx, ny):
        result = []
        sz = len(self.basis_size)
        for i in range(sz):
            n = self.basis_size[i]
            bf = self.basis_functions[i]
            #A =  np.array([bf.u_f(j,k,x,y,nx,ny,n = n) for j in range(n)])/np.sqrt(n)
            js = [j for j in range(n)]
            A = np.array(list(map(lambda j: bf.u_f(j,k,x,y,nx,ny,n = n), js)))/np.sqrt(n)
            result.append(A)
    
        return np.concatenate(result)

    def evaluate_df_dk(self, k, x, y):
        result = []
        sz = len(self.basis_size)
        for i in range(sz):
            n = self.basis_size[i]
            bf = self.basis_functions[i]
            #A =  np.array([bf.df_dk(j,k,x,y, n = n) for j in range(n)])/np.sqrt(n)
            js = [j for j in range(n)]
            A = np.array(list(map(lambda j: bf.df_dk(j,k,x,y, n = n), js)))/np.sqrt(n)
            result.append(A)
    
        return np.concatenate(result)
    
    def plot_basis_function(self,i,j,k):
        self.basis_functions[i].plot_fun(j,k)

    def plot_basis(self, k):
        dim = len(self.basis_functions)    
        for j in range(dim):
            bf = self.basis_functions[j]
            bs = self.basis_size[j]
            sz = int(np.min([9, bs]))
            
            #fig = plt.figure(figsize=figsize)
            for i in range(sz):
                plt.subplot(3,3,i+1)
                bf.plot_fun(i, k, n = bs)
            plt.tight_layout()
    
    def add_basis_function(self, basis_fun, min_size = 10):
        self.basis_functions.append(basis_fun)
        self.basis_size.append(min_size)

def combine_basis(basis1, basis2):
    bf1 = basis1.basis_functions
    #print(bf1)
    bs1 = basis1.basis_size

    bf2 = basis2.basis_functions
    #print(bf2)
    bs2 = basis2.basis_size
    
    bf = bf1.copy()
    bs = bs1.copy()
    for i in range(len(bf2)):
        bf.append(bf2[i])
        bs.append(bs2[i])
    #print(bf1)
    bas = basis(bf)
    bas.set_basis_size(bs)
    return bas