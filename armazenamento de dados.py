cliente = []
idade = []

while True:
    try:   
        nome  = input('Digite o nome: ')
        cliente.append(nome)
        anos_vida = int(input('igite sua idade: '))
        idade.append(anos_vida)
        sair = input('Deseja inserir mais um Nº? (S/N)').upper().strip()
        if sair == 'N':
            break
    except:
        print('Digite um Nº Válido')

'''for i,e in cliente, idade:
    print(f'O cliente {i} tem {e} anos')'''


for i in range(len(cliente)):
    nome = cliente[i]
    anos = idade[i]
    print(f'O cliente {nome} tem {anos} anos')

#print('1\n2\n3\n4')


'''while True:
    try:
        opcao = int(input('opcao: '))
        if opcao in [1,2,3,4]:
            print('opcao ok')
            break
        else:
            print('opção inválida')
    except:
        print('Digite um Nº válido')'''
