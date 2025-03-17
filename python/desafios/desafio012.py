# programa que vai ler a temperatura que o usuário vai digitar em °C

celsius = float(input('Digite a temperatura em °C: '))
kelvin = celsius + 273
fahrenheit = (1.8 * celsius) + 32

print(f'A temperatura que você digitou, corresponde a {celsius:.1f}°C, {kelvin:.1f}K, {fahrenheit:.1f}°F')
