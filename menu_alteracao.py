
from alt import *


def alterar():
    repeticao = 35
    print ('*' * repeticao)
    print ('1 - Alterar Nome')
    print ('2 - Alterar endereço')
    print ('3 - Alterar E-Mail')
    print ('5 - Alterar telefone')
    print ('5 - Alterar Desconto')
    print ('-' * repeticao)
    print ('S - Voltar ao menu principal')
 

    opcao = input('')
    
    if opcao == '1':
        altNome()
    elif opcao == '2':
        altEndereco()
    elif opcao == '3':
        altEmail()
    elif opcao == '4':
        altTelefone()
    elif opcao == '5':
        altDesconto()
    elif opcao.upper == 'S':
        return True
    else:
        print ('Opção inválida, tente novamente')
