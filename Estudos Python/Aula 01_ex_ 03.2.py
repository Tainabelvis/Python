Variavel

a = input('Digite algo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um numero?', a.isnumeric())
print('É uma letra?', a.isalpha())
print('É uma alfanumero', a.isalnum())
print('Estão em maiúsculas?', a.isupper())
print('Estão em minúsculas?', a.islower())
print('Estão em maiúsculas e minúsculas?', a.istitle())
