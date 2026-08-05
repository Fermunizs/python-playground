values = [1, 14, 9, 7, 2, 11, 0]
target = int(input("Digite o valor do orçamento: "))

def two_values(values, target):
    memoria = {}
    for i in range(len(values)):
        if target - values[i] in memoria:
            complemento = target - values[i]
            print(f"Valores encontrados! {values[i]} + {complemento} = {target}, os index deles são respectivamente {i} e {complemento}.")
            return (i , complemento) 
        else:
            memoria[values[i]] = i
            print(f"{values[i]} foi adicionado à memória.")
    print("Valores não encontrados.")

two_values(values, target)
