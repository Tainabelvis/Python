#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um numero:"))
d = n * 2
t = n * 3
r = n ** (1/2)
print("O dobro do numero digitado é: {} \nO triplo do numero digitado é: {} \nA raiz quadra do nunmero digitado é:{}" .format(d,t,r))
