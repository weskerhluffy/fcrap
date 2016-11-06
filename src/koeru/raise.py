'''
Created on 02/11/2016

@author: ernesto
https://codelab.interviewbit.com/problems/equal/
'''

import operator
def caca_ordena_dick_valor(dick):
    return sorted(dick.items(), key=lambda cosa: cosa[1])

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        mapa={}
        mapa2={}
        mapa_mezclado={}
        max_suma=None
        par_elegido=[]
        cacas=[]
        
        for idx_a in xrange(len(A)):
            for idx_b in xrange(idx_a+1,len(A)):
                resu_suma=A[idx_a]+A[idx_b]
                if(resu_suma in mapa2):
                    continue
                if(resu_suma not in mapa):
                    mapa[resu_suma]=(idx_a,idx_b)
                else:
                    idx_a1,idx_b1=mapa[resu_suma]
 #                   print("comparando %s con %u %u"%(mapa[resu_suma],idx_a,idx_b))
                    if(idx_b1!=idx_a and idx_b1!=idx_b and idx_a1<idx_a):
                        mapa2[resu_suma]=[idx_a,idx_b]
        
        for llave_act in mapa2:
            idx_a,idx_b=mapa[llave_act]
            idx_a1,idx_b1=mapa2[llave_act]
            mapa_mezclado[llave_act]=[idx_a,idx_b,idx_a1,idx_b1]
        
        cacas=caca_ordena_dick_valor(mapa_mezclado)
#        print("ordenados %s"%cacas)
        
        if(cacas):
            llave_elegida=cacas[0][0]
            par_elegido=cacas[0][1]
        
        return par_elegido
                