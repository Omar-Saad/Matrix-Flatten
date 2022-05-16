from operator import le
import numpy as np
class Matrix:
    _INDEX_ERROR_MSG = "INDEX ERROR : Wrong indeces"

    def __init__(self,N,M,P):
        self.N = N
        self.M = M
        self.P= P
        self.matrix = self.generate_random_matrix(N,M,P)

    def generate_random_matrix(self,N, M, P):
        matrix = np.random.rand(N,M,P)
        return matrix


    def flatten_matrix(self):
        self.matrix_flattend = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                for k in range(len(self.matrix[i][j])):
                    self.matrix_flattend.append(self.matrix[i][j][k])

        self.matrix_flattend

    def get_item_from_flatten_by_index(self,index):
        return self.matrix_flattend[index]

    def get_item_from_3d_by_index(self,i,j,k):
        return self.matrix[i][j][k]
    
    def get_1D_index_from_3D(self,i,j,k):
        if i >= self.N or j >= self.M or k >= self.P:
            raise IndexError
             
        return i*self.M*self.P + j*self.P + k
     