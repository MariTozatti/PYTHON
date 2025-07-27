# o print sozinho, estar declarado o tipo da variavel, le o que recebe em string, então ele não soma ele concatena
# Tipos primitivos:
# Int - números inteiros
# Float - números reais
# Bool - True ou False
# Str - tipo letra(usa '' ou "")

#mostra o tipo da variavel - retorna str
n1 = input('Qaul seu número?')
print(type(n1))
#mostra o tipo da variavel - retorna int
n1 = int(input('Qaul seu número?'))
print(type(n1))

#ex 02
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
print('A soma dos números', n1, 'e', n2, 'é:',s)
#isso pode ser substituido por uma mascara que deixa mais facil a escrita
print('A soma dos números {} e {} é: {}'.format(n1,n2,s))

#tem vários métodos .isnumeric, .isupper, .isalpha, cada uma mostra uma informação diferente sobre a variavel, funciona com o input sem tipo declarado.