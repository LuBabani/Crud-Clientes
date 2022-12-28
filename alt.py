from bancoDados import *

def altNome():
    codigo = int(input('Informe o codigo do cliente'))
    print(f'Nome: {cliente[codigo][0]}')

    alterar = input('Alterar o Nome? S - SIM / N - Não')
    if alterar == 'S':
        novoNome = input('Informe o novo Nome')
        cliente[codigo][0] = novoNome

    else:
        print('Opção Inválida')

def altEndereco():
    codigo = int(input('Informe o codigo do cliente'))

    print(f'nome: {cliente[codigo][0]}')
    print(f'Endereço Atual{cliente[codigo][1]}')

    alterar = input('Alterar o Endereço? S - SIM / N - Não')
    if alterar == 'S':
        novoEnd = input('Informe o novo endereço')
        cliente[codigo][1] = novoEnd

    else:
        print('Opção Inválida')

def altEmail():
    codigo = int(input('Informe o codigo do cliente'))
    print(f'Nome: {cliente[codigo][0]}')
    print(f'E-mail Atual{cliente[codigo][2]}')

    alterar = input('Alterar o E-Mail? S - SIM / N - Não')
    if alterar == 'S':
        novoEmail = input('Informe o novo E-Mail')
        cliente[codigo][2] = novoEmail

    else:
        print('Opção Inválida')

def altTelefone():
    codigo = int(input('Informe o codigo do cliente'))
    print(f'Nome: {cliente[codigo][0]}')
    print(f'Telefone Atual{cliente[codigo][3]}')

    alterar = input('Alterar o Telefone? S - SIM / N - Não')
    if alterar == 'S':
        novoTel = input('Informe o novo Telefone')
        cliente[codigo][3] = novoTel
    
    else:
        print('Opção Inválida')


def altDesconto():
    codigo = int(input('Informe o codigo do cliente'))
    print(f'Nome: {cliente[codigo][0]}')
    print(f'Desconto Atual{cliente[codigo][4]}')

    alterar = input('Alterar o desconto? S - SIM / N - Não')
    if alterar == 'S':
        novoDesconto = input('Informe o novo desconto')
        cliente[codigo][4] = novoDesconto

def altcompras():
    codigo = int(input('Informe o codigo do cliente'))
    print(f'Nome: {cliente[codigo][0]}')
    print(f'Valor total de compras Atual{cliente[codigo][5]}')

    alterar = input('Alterar o Valor? S - SIM / N - Não')
    if alterar == 'S':
        novoCompras = input('Informe o novo valor')
        cliente[codigo][5] = novoCompras