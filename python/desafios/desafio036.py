num01 = int(input("Digite o valor 01: "))
num02 = int(input("Digite o valor 02: "))

if num01 > num02:
    print(num01, ">", num02)
elif num02 > num01:
    print(num02, ">", num01)
else:
    print(num01, "=", num02)