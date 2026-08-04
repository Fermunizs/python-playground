values = [1, 14, 9, 7, 2, 11, 0]
target = int(input("Digite o valor do orçamento: "))

def two_values(values, target):
    for i in range(len(values)):
        print(f"Verificando o valor {values[i]} na posição {i}")
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target:
                print(f"Encontrado! {values[i]} + {values[j]} soma {target}, o index deles são respectivamente {i} e {j}.")
                return (values[i], values[j])
            else:
                print(f"Valor ainda não encontrado")
        print(f"Valores não encontrados.")

two_values(values, target)