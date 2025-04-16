cidade = input('Digite uma cidade: ')
santo = cidade[:6]

print("Cidade: ", cidade.title())

if santo.capitalize().startswith("Santo"):
    print("Sua cidade começa com Santo!")
else:
    print("Sua cidade não começa com Santo!")
