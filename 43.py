l = float(input("Digite quantos litros você quer abastecer: "))
c = input("Digite A para álcool ou G para gasolina: ")
pç= 0
if c == "A" or c == "a":
    pç = l * 1.9
    if litros <= 20:
        pç -= 1.9 * l * 3 / 100
    else:
        pç-= 1.9 * l * 5 / 100
elif c == "G" or c == "g":
    pç = l * 2.5
    if l<= 20:
        pç-= 2.5 * l* 4 / 100
    else:
        pç-= 2.5 * l * 6 / 100
print(f"O preço a pagar é R${preco:.2f}")
