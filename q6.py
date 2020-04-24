def valor_absoluto(x):
    if x < 0:
        return -x
    return x


def is_prime(n):
    #verificar para todos os possíveis divisores 
    #deste número inteiro se alguns deles é realmente divisor
    #se existir algum divisor entre 2 e N/2
    #entao não é primo
    N = valor_absoluto(n)
    stop = N//2    
    if N > 1:
        for i in range(2, stop):
            if N%i == 0:
                #não é primo
                return False
        return True
    else:
        #n é -1, 0 ou 1
        return False

#TESTE DE UNIDADE

def test(passou):
    if passou:
        print("Teste ok")
    else:
        print("Teste FAILED")

def test_suite():
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(is_prime(19950807))
    
test_suite()

