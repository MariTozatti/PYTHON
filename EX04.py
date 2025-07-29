#Faça um programa que leia um n inteiro e mostre na tela seu sucessor e antecessor.

numero = int(input('Qual seu número?'))
antecessor = numero - 1
sucessor = numero + 1
print ('O Antecessor é {}, e o sucessor é {}'.format(antecessor, sucessor))

#ou

numero = int(input('Qual seu número?'))
print ('O Antecessor é {}, e o sucessor é {}'.format((numero - 1), (numero + 1)))


#Crie um algoritimo que leia um numero e mostre seu dobro, triplo e raíz quadrada

numero = int(input('Qual seu número?'))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print ('O dobro é {} o triplo é {} a raiz é {}'.format(dobro, triplo, raiz))

# A raiz tbem pode ser calculada com a fução .pow(numero, (1/2)), ai ela ficaria no print, dentro do format(quando o calculo é feito dentro do format)

# no pytohn, podemos multiplicar simbulos no print, como '=' * 10 -> ==========
