precoProduto = float(input("Qual o preço do produto: "))
condicaoPagamento = int(input("Qual a condição do pagamento ? \n 1. Dinheiro/Cheque \n 2. Cartão Débito \n 3. 2x no Cartão \n 4. 3x ou mais com Juros \n\n Escolha a Condição: "))

if condicaoPagamento == 1:
    print("10% de desconto")
elif condicaoPagamento == 2:
    print("5% de desconto")
elif condicaoPagamento == 3:
    print("Preço normal")
else:
    print("20% de juros")
