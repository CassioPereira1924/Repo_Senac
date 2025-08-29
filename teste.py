'''num1 = int(input('Digite o primeiro Nº: ')) #int é para dizer que os tipo de dado é in inteiro
num2 = int(input('Digite o segundo Nº:  ')) 
resultado = num1 + num2

print(f'A resultado da soma de {num1} + {num2} é {resultado}')'''

while True:
    try:
        idade = int(input('Digite sua idade: '))
        break
    except:
        print('Digite um nº válido')


if idade < 16:
    print('Não vota')
elif idade >= 16 and idade < 18:
    print('voto opcional')
elif idade >= 18 and idade <= 65:
    print('voto obrigatório')
else:
    print('Voto opcional de idoso')


