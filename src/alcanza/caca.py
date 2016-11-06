'''
Created on 05/11/2016

@author: ernesto
https://codelab.interviewbit.com/problems/reach/
'''

# 2 -7 -13 
# 2 1 -5

def alcanza_caca_calcula_y(x1, y1, x2, y2, x):
    x_tmp = x + 0.5
    y = ((y2 - y1) * (x_tmp - x1)) / (x2 - x1) + y1
    return y

def alcanza_caca_calcula_movimientos(x1, y1, x2, y2):
    tam_x = abs(x2 - x1)
    tam_y = abs(y2 - y1)
    return max(tam_x, tam_y)
        


class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        contador_caca = 0
        for i in range(len(X[:-1])):
            x1 = X[i]
            y1 = Y[i]
            x2 = X[i + 1]
            y2 = Y[i + 1]
            contador_caca += alcanza_caca_calcula_movimientos(x1, y1, x2, y2)
            
        return contador_caca
            
if __name__ == '__main__':
    ass = Solution()
    a=ass.coverPoints([-7,-13],[1,-5])
    print(a)
