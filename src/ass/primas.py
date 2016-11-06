'''
Created on 04/11/2016

@author: ernesto
https://codelab.interviewbit.com/problems/primesum/
'''

import math


def primas_genera_primos(limite):
    primos = set()
    compuestos = [False for _ in range(limite+1)]
    limite_crap = int(round(math.sqrt(limite)))
    
    for m in range(2, limite_crap + 1):
        if(not compuestos[m]):
            primos.add(m)
            for caca in range(m * m, limite + 1, m):
                compuestos[caca] = True
    
    for caca in range(limite_crap, limite + 1):
        if(not compuestos[caca]):
            primos.add(caca)
    
    return primos

def es_primo(num):
    compuesto = False
    for i in range(2, int(round(math.sqrt(num))) + 1):
        if(not (num % i)):
#            print("es compuesto por %u" % (num%i))
            compuesto = True
            break
    return not compuesto

#http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        caca = 0
        primos = sorted(list(primes(9781)))
        for caca in primos:
            complemento = A - caca
#        print("asshit %u %u" % (caca, complemento))
            if(complemento in primos):
                break
            if es_primo(complemento):
                break
        return [caca, A - caca]








