values = [1, 14, 9, 7, 2, 11, 0]
target = int(input("Digite o valor do orçamento: "))

def two_values(values, target):
    for i in range(len(values)):
        memoria = {}
        resto = target - values[i]
        memoria[values[i]] = i
