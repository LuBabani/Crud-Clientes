from bancoDados import *

def excluir():
    codigo = int(input('Informe o codigo do cliente: '))
    if codigo in list (cliente.keys()):
        print(f'Nome: {cliente[codigo][0]}')

        excluir = input('Deseja excluir o cliente? S - SIM / N - Não').upper()
        if excluir == 'S':
            del cliente[codigo]
            print('O cadastro foi excluido')
        
    else:
        print('Invalido')
    input('Deseja voltar ao menu principal?')

