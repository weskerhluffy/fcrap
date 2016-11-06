def cumbia_poder2_encuentra_factores_primos(num):
    i = 2
    factores = []

    while i * i <= num:
        while not (num % i) :
            num = num / i
            factores.append(i)
            
        i = i + 1
    if(num != 1):
        factores.append(num)
    return factores

# http://www.lawebdelprogramador.com/codigo/Python/3152-Calcular-el-maximo-comun-divisor-de-dos-numeros.html
def mcd(a, b):
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    return a

def cumbia_poder2_tiene_base_entera(factores):
    mcd_actual = 0
    conteo_factores = {}
    
        
    for factor_mierda in factores:
        if(factor_mierda not in conteo_factores):
            conteo_factores[factor_mierda] = 0
        conteo_factores[factor_mierda] += 1
    
    if(len(factores) == 1):
        return False
    
    if(sum(conteo_factores.values()) == sum(conteo_factores.keys()) // len(factores)):
        return True
    
    for idx_factor, factor_mierda in enumerate(factores):
        ocurrencia_1 = conteo_factores[factor_mierda]
        if(not mcd_actual):
            factor_mierda_sig = factores[idx_factor + 1]
            ocurrencia_2 = conteo_factores[factor_mierda_sig]
            mcd_actual = mcd(ocurrencia_1, ocurrencia_2)
        else:
            mcd_actual = mcd(mcd_actual, ocurrencia_1)
            
#    print("mcd caca %u" % mcd_actual)
    return mcd_actual > 1
    

class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if(A==1):
            return True
        luna=cumbia_poder2_encuentra_factores_primos(A)
        llena=cumbia_poder2_tiene_base_entera(luna)
        return llena
