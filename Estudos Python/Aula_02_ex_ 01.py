#Crie um programa que leia um núimero Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
n = float(input("Digite um valor:"))
print("O valor digitado foi {} e a sua porção interia é {}".format(n, math.trunc(n)))
