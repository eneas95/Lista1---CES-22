def sum_to(n):
    sum = 0
    vetor = range(n)
    for i in vetor:
        sum = sum + vetor[i]
    sum = sum + n
    return sum

result = sum_to(9)
print(result)