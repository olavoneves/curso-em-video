name = input('Digite seu nome completo: ')
print("Maiusculo: " + name.upper())
print("Minusculo: " + name.lower())
print("Quantidade de letras: ", len(name.replace(" ", "")))

listaName = name.split()
print("Seu primeiro nome é: ", listaName[0], "\nEle tem ", len(listaName[0]), " letras.")