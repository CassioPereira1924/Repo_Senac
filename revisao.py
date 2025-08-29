print("Bem-vindo ao Konoha Hotel!\n")
print("Escolha o tipo de quarto:")
print("1 - Quarto Genin (R$ 120,00 por noite)\n2 - Quarto Jounin (R$ 180,00 por noite)\n3 - Suíte Hokage (R$ 250,00 por noite)")

# Entrada do tipo de quarto
while True:
    try:
        tipo_quarto = int(input("Digite o número correspondente ao tipo de quarto desejado: "))
        break
    except:
        print('Digite um nº válido')


nome = input("Informe seu nome: ")
noites = int(input("Informe o número de noites que deseja ficar: "))

# Definindo o preço por noite com base na escolha
if tipo_quarto == 1:
    preco_noite = 120
    nome_quarto = "Quarto Genin"
elif tipo_quarto == 2:
    preco_noite = 180
    nome_quarto = "Quarto Jounin"
elif tipo_quarto == 3:
    preco_noite = 250
    nome_quarto = "Suíte Hokage"
else:
    print("Opção inválida. Encerrando o sistema.")
    

# Cálculo do valor total
valor_total = preco_noite * noites

# Exibindo confirmação formatada
print("\n--- Confirmação de Reserva ---\n")
print(f"Nome do hóspede: {nome}")
print(f"Tipo de quarto: {nome_quarto}")
print(f"Número de noites: {noites}")
print(f"Valor total da estadia: R$ {round(valor_total, 2)}")
print("Obrigado por reservar com o Konoha Hotel!")
