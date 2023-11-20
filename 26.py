pç1 = float(input("Digite o preço do produto 1: "))
pç2 = float(input("Digite o preço do produto 2: "))
pç3 = float(input("Digite o preço do produto 3: "))
if pç1 < pç2 and pç1 < pç3:
    print(f"O produto com o menor preco é o 1, custando R${pç1:.2f}")
elif pç2 < pç1 and pç2 < pç3:
    print(f"O produto com o menor preco é o 2, custando R${pç2:.2f}")
else:
    print(f"O produto com o menor preco é o 3, custando R${pç3:.2f}")
