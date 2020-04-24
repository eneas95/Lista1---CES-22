def contarPalavras(msg):
    temp = msg.split()
    contador = 0
    for i in temp:
        contador = contador + 1
        if i == "sam":
            break
    return contador

msg1 = "balabla blelel ola zetsu sam goiaba chaves"
msg2 = "Palmeiras é o Real Madrid das Américas e todo mundo sabe disso"
msg3 = "O maior vilão do jogo é o sam mas não sei porque"
msg4 = "Desejo uma feliz pasamcoa a todos voces"


def test(passou):
    if passou:
        print("Teste ok")
    else:
        print("Teste FAILED")

def test_suite():
    test(contarPalavras(msg1)==5)
    test(contarPalavras(msg2)==12)
    test(contarPalavras(msg3)==8)
    test(contarPalavras(msg4)==7)
    
test_suite()