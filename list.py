from bancoDados import *  


def listNome():
    for codigo in cliente:
        print(f'{cliente[codigo][0]} - {cliente[codigo][0]}')  
    input('Pressione uma tecla para continuar')   

def listEndereco():
    for codigo in cliente:
        print(f'{cliente[codigo][0]} - {cliente[codigo][1]}')
    input('Pressione uma tecla para continuar')

def listEmail():
    for codigo in cliente:
        print(f'{cliente[codigo][0]} - {cliente[codigo][2]}')   
    input('Pressione uma tecla para continuar')

def listTelefone():
    for codigo in cliente:
        print(f'{cliente[codigo][0]} - {cliente[codigo][3]}')
    input('Pressione uma tecla para continuar')

def listDesconto():
    for codigo in cliente:
        print(f'{cliente[codigo][0]} - {cliente[codigo][4]}')   
    input('Pressione uma tecla para continuar')