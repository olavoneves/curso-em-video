frase = input('Digite uma frase sobre algo que você gosta de fazer: ').lower()

frase.strip()
print('Sua frase possui a letra a ', frase.count('a'), 'vezes')
print('A letra a aparece primeiro na posição: ', frase.find('a')+1)
print('A letra a aparece na ultima vez na posição: ', frase.rfind('a')+1)
