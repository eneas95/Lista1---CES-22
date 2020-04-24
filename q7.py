def sum_of_squares(xs):
    aux = 0
    sum = 0
    for i in xs:
        aux = i**2
        sum = sum + aux
    return sum

#TESTE DE UNIDADE

def test(passou):
    if passou:
        print("Teste ok")
    else:
        print("Teste FAILED")

def test_suite():
    test(sum_of_squares([2,3,4])==29)
    test(sum_of_squares([ ])==0)
    test(sum_of_squares([2,-3,4])==29)
    
test_suite()