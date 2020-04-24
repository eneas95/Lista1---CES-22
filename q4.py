c_list = [2, 3, 4, 5, 6, 8]
b_list = [2,2,2,2,2,2]
d_list = [3,5,7,2]
e_list = [3,3, 3, 3]
f_list = [3, 4, 5, 6, 8]

def questao4 (a_list):
 #achar o primeiro impar e
 #somar a lista até ele
 tam = len(a_list)
 sum = 0
 for i in range(tam):
    if a_list[i]%2 != 0:
        sum = sum + a_list[i]
    else:
        break
 return sum

#TESTE DE UNIDADE

def test(passou):
    if passou:
        print("Teste ok")
    else:
        print("Teste FAILED")

def test_suite():
    test(questao4(c_list)==0)
    test(questao4(b_list)==0)
    test(questao4(d_list)==15)
    test(questao4(e_list)==12)
    test(questao4(f_list)==3)
    

test_suite()