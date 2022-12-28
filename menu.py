
from inclusao import *
from exclusao import *
from menu_alteracao import *
from menu_listagem import *


def menu():
    while True:
        repeticao = 20
        print ('*' * repeticao)
        print ('Cadastro de Clientes: ')
        print ('*' * repeticao)
        print(' 1 - Incluir Cliente: ')
        print(' 2 - Alterar Cadastro: ')
        print(' 3 - Excluir Cadastro: ')
        print(' 4 - Listar Clientes')
        print ('-' * repeticao)
        print(' S - Sair')
    
        
        opcao = input('')
        
        if opcao == '1':
            incluir()
        elif opcao == '2':
            alterar()
        elif opcao == '3':
            excluir()
        elif opcao == '4':
            listar()
        elif opcao.upper == 's':
            pass
        else:
            print ('Opção não reconhecida. Tente Novamente!')
    #Fim do loop
            