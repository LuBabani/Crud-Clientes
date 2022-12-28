from list import *
from bancoDados import *

def listar():
    repeticao = 35
    print ('*' * repeticao)
    print ('1 - Listar clientes por Nome')
    print ('2 - Listar E-Endereçoes')
    print ('3 - Listar E-Mail')
    print ('4 - Listar Telefone')
    print ('5 - Listar Desconto')
    print ('-' * repeticao)
    print ('S - Volta ao menu principal')
    

    opcao = input('')

    if opcao == '1':
        listNome()
    elif opcao == '2':
        listEndereco()
    elif opcao == '3':
        listTelefone()
    elif opcao == '4':
        listEmail()
    elif opcao == '5':
        listDesconto()
    elif opcao.upper == 'S':
        return True
    else:
        print ('Opção inválida, tente novamente')
