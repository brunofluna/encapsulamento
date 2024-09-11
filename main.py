from classe import *

if __name__ == '__main__':
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    email = input('Digite o e-mail: ')

    # instancia da classe
    usuario = Pessoa(nome, idade, email)

    # saida de dados
    print(f'\nNome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'E-mail: {usuario.email}.')




# saida de dados "forma errada"
#    print(f'\nNome: {usuario.nome}.')
#   print(f'Idade: {usuario.get_idade()}.')
#    print(f'E-mail: {usuario.get_email()}.')