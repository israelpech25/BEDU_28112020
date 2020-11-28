numero = input('Que numero quieres multiplicar?\t')

numero = int(numero)

print(f'A continuacion se muestra la tabla del (numero)')

print('-------------------------------------')

for n in range (10):
    indice = n + 1
    resultado = numero * indice
    resultado_impreso=(f'{numero} * {indice} = {resultado}')
    print(resultado_impreso)