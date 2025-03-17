# faça um programa para ler a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintar, cada litro de tinta pinta uma área de 2m^2

# Leitura da largura e altura da parede
paredeLargura = float(input('Digite a largura da parede em metros: '))
paredeAltura = float(input('Digite a altura da parede em metros: '))

# Exibição das dimensões da parede
print('\nA sua parede tem: {}m de largura, por {}m de altura. \n'.format(paredeLargura, paredeAltura))

# Cálculo da área da parede
areaParede = paredeLargura * paredeAltura

# Cálculo da quantidade de tinta necessária (cada litro pinta 2m²)
quantidadeDeTinta = areaParede / 2

# Exibição do resultado
print(f'Você vai precisar de {quantidadeDeTinta:.2f}l de tinta, para pintar a parede que tem uma área de {areaParede:.2f}m^2.')
