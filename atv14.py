print("Digite o valor do produto")
valorProd = float(input())
print("Digite a quantidade do produto que foi comprado")
qtdProd = int(input())
valorCompra = valorProd * qtdProd
desconto = valorCompra / 10.0
print("O valor total da compra desse produto foi de " , valorCompra, "Além disso, o valor dessa compra com o desconto de 10% foi de: " , valorCompra - desconto)
