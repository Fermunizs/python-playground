# Challenge #001 — Encontrando Dois Valores que Formam uma Soma

<p align="left">
    <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Difficulty-Easy-28a745?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Algorithm-HashMap%20%7C%20Brute%20Force-blue?style=for-the-badge" />
</p>

## Descrição

Durante uma auditoria financeira, é necessário localizar rapidamente dois valores dentro de uma lista cuja soma seja exatamente igual ao valor esperado.

O objetivo deste desafio é desenvolver um algoritmo que encontre os dois elementos responsáveis por formar o valor alvo (**target**).

Foram implementadas duas abordagens:

- Força Bruta (Brute Force)
- HashMap (Dicionário)

---

## Problema

Dado um vetor de números inteiros e um valor alvo (`target`), encontre dois números cuja soma seja igual ao valor informado.

Considere que:

- Existe apenas uma solução válida.
- Um mesmo elemento não pode ser utilizado duas vezes.
- A ordem dos elementos não importa.

---

## Entrada

```python
values = [1, 14, 9, 7, 2, 11, 0]
target = 16
```

---

## Saída Esperada

```text
14 + 2 = 16
```

---

## Regras

- Utilizar Python.
- Não utilizar bibliotecas externas.
- Existe apenas uma resposta correta.
- O mesmo elemento não pode ser utilizado duas vezes.
- Desenvolver duas soluções com diferentes complexidades.

---

## Soluções Implementadas

### Solução 1 — Força Bruta

Arquivo:

```text
main.py
```

A primeira solução percorre toda a lista utilizando dois laços de repetição.

Para cada elemento, todos os demais elementos à frente são verificados até encontrar um par cuja soma seja igual ao valor informado.

Essa abordagem é simples e fácil de compreender, porém possui custo computacional elevado para listas grandes.

---

### Solução 2 — HashMap (Dicionário)

Arquivo:

```text
dict.py
```

A segunda solução utiliza um dicionário como estrutura auxiliar para armazenar os valores já percorridos.

Para cada número da lista é calculado o complemento necessário para atingir o valor alvo.

Caso esse complemento já exista no dicionário, a resposta é encontrada imediatamente.

Essa abordagem elimina a necessidade de percorrer a lista duas vezes, reduzindo significativamente o tempo de execução.

---

## Complexidade

| Solução | Tempo | Memória |
|---------|-------|----------|
| Força Bruta | O(n²) | O(1) |
| HashMap | O(n) | O(n) |

---

## Objetivos de Aprendizado

Durante este desafio foram praticados os seguintes conceitos:

- Estruturas de dados
- Listas
- Dicionários (HashMap)
- Loops
- Funções
- Busca eficiente
- Complexidade de algoritmos
- Otimização de código

---

## Estrutura do Projeto

```text
challenge-001-two-values
│
├── main.py
├── dict.py
└── README.md
```

---

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/Fermunizs/python-playground.git
```

Acesse a pasta do desafio:

```bash
cd challenges/two-sum
```

Execute uma das soluções:

```bash
python main.py
```

ou

```bash
python dict.py
```

Informe o valor desejado quando solicitado.

---

## Resultado Esperado

Entrada

```text
Digite o valor do orçamento: 16
```

Saída (Força Bruta)

```text
Encontrado! 14 + 2 soma 16.
```

Saída (HashMap)

```text
Valores encontrados! 2 + 14 = 16.
```

---

## Comparação das Soluções

| Característica | Força Bruta | HashMap |
|---------------|------------|----------|
| Facilidade de implementação | Alta | Média |
| Performance | Baixa | Alta |
| Escalabilidade | Baixa | Alta |
| Complexidade | O(n²) | O(n) |

A solução utilizando HashMap é a abordagem mais indicada para aplicações reais devido à sua eficiência, enquanto a solução por força bruta é importante para compreender a lógica inicial do problema.

---

## Licença

Este projeto foi desenvolvido para fins de estudo e prática de lógica de programação.