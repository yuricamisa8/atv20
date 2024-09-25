# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.
n = 0 
for n1 in range(1,101):
    if n1 % 2 == 0:
        n += n1
print(n)
