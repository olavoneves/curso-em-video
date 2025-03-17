# programa para ver se o usuário alugou um carro, e depois calcular quanto ele vai precisar pagar

#Perguntar para o usuário se ele alugou um carro
alugouCarro = input('Você alugou um carro? (s/n): ')

# Converter a resposta para um valor boolean
if alugouCarro.lower() == 's':
    sim = True
else:
    nao = False

#Verificar se foi alugado
if sim:
    quantDias = int(input('Quantos dias você alugou esse carro? '))
    quantKm = float(input('Quantos Km você rodou com esse carro? '))
    precoDias = quantDias * 60.00
    precoKm = quantKm * 0.15
    precoTotal = precoDias + precoKm
    print(f'Então o sr(a), vai ter um valor total de R${precoTotal:.2f} a ser pago!')
else:
    print('Você não alugou um carro!')
