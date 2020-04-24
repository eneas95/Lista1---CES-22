#Representando complexos como Tuplas

#3 + 2i
x1 = (3,2)
#1 + 0i
x2 = (1,0)
#12 + 5i
x3 = (12,5)
#2i
x4 = (0,2)
#2 + 2i
x5 = (2,2)
#4 + 3i
x6= (4,3)

#Agora definir a soma de complexos
def SomaComplexos(z1, z2):
    a = z1[0] + z2[0]
    b = z1[1] + z2[1]
    z3 = (a,b)
    return z3

def test(passou):
    if passou:
        print("Teste ok")
    else:
        print("Teste FAILED")

def test_suite():
    test(SomaComplexos(x1,x2)==(4,2))
    test(SomaComplexos(x3,x4)==(12,7))
    test(SomaComplexos(x5,x6)==(6,5))
    
test_suite()