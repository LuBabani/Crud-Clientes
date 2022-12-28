from bancoDados import *


def incluir():
    repeticao = 35
    print('*' * repeticao)
    print('Cadastro de cliente')
    print('*' * repeticao)
    codigo = int(input('Informe o código do cliente: '))
    nome = input('Nome: ')
    endereco = input ('Endereço: ')
    email = input('E-Mail: ')
    telefone = input ('Telefone: ')
    desconto = float(input('Desconto: '))
    compras = float(input('Digite o total de compras: '))
    print('-' * repeticao)

    
    lista = [nome, endereco, email, telefone, desconto, compras] #Criar a lista
    cliente[codigo] = lista #preencher dicionário

 