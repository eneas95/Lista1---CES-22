
def neatMatriz(num):
    #FORMATAÇÃO

    #num: índice da matriz, ou seja, número de células por linha
    #Espaços utilizados por cada célula no total 
    cel = len(str(num**2)) + 1 #adicionar um espaço a mais
    #Espaços utilizados pelas células à esquerda (numeração das linhas)
    n_linha = len(str(num)) + 1 #adicionar um espaço a mais

    #LINHA PONTILHADA
    pontilhada = " " * n_linha + ":" + "-" * cel * num
    # (n-linha):--------------------------------------

    #CABEÇALHO
    stringAux1 = ""
    #evitar o zero
    for j in range(1, num + 1):
        #numeros em cada célula, nesse caso, são strings
        stringAux1 = "".join([stringAux1, str(j).rjust(cel)])
        #rjust(cel) faz a formatação à direita para cada célula
        #Ex: j=1 -> stringAux1 = "   1"
        #    j=2 -> stringAux1 = "   1   2"
    cabecalho = " " * n_linha + " " + stringAux1

    #LINHAS DA MATRIZ
    
    corpo = "\n".join([str(j).rjust(cel) + ":" + 
    "".join([str(j * k).rjust(cel) for k in range(1, num+1)]) for j in range(1, num + 1)])

    
    #FINALMENTE: JUNTAR AS STRINGS E PRINTAR A MATRIZ
    saida= "\n".join([cabecalho, pontilhada, corpo])
    print(saida)

neatMatriz(14)
