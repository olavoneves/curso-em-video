# faça um algoritmo para ler um preço do produto e o novo preço com 5% de desconto

# Variavel para saber o produto que o usuário vai comprar
produto = input('Digite o produto que você gostaria de comprar (Arroz, Feijão, Carne, Macarrão, Frango, Peixe, Ovo, Legumes): ')

# Mostrar o produto do usuário e falar que tem desconto
print(f'O(A) {produto} está R$35.00 e tem desconto de 5%')

# Aplicando o desconto no produto
valorInicial = 35.00
descontoProduto = (valorInicial * 5) / 100
valorFinal = valorInicial - descontoProduto

# Exibir o novo preço para o usuário
print(f'O preço que o senhor(a) precisa pagar é de: R${valorFinal:.2f}')

