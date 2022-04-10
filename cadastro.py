from datetime import datetime


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


current_date = datetime.now()
current_date = current_date.strftime('%d/%m/%y - %H:%M') # define formato de data: DIA/MES/ANO - HORA/MINUTO


def register(): # para registrar um novo individuo
    global age
    while True: # cria um loop enquanto nao receber um nome valido
        try:
            name = input('Olá, digite seu nome inteiro:\n')
            if all(c.isalpha() or c.isspace() for c in name):
                break # quebra o loop
            else:
                raise InputError('O nome contém caracteres inválidos. Por favor tente novamente:\n')
        except InputError as ex:
            print(ex)
    name = name.title() # coloca o nome em maiusculo
    brk = name.split()
    first_name = brk[0] # pega o primeiro nome

    genders_tuple = ('masculino', 'feminino', 'outro') # generos aceitos
    gender = input('Qual o seu gênero?\n(masculino/feminino/outro)\n')
    while gender not in genders_tuple: # genero invalido
        gender = input('Gênero inválido. Por favor insira "masculino", "feminino" ou "outro":\n')
    if gender == 'masculino': # grava idade; tratamentos diferentes de acordo com o genero informado
        age = input('Bem-vindo {}, entre com sua idade:\n'.format(first_name))
    elif gender == 'feminino':
        age = input('Bem-vinda {}, entre com sua idade:\n'.format(first_name))
    elif gender == 'outro':
        age = input('Bem-vinde {}, entre com sua idade:\n'.format(first_name))
    while age.isnumeric() is False: # idade invalida
        age = input('A idade inserida é inválida. Por favor, digite sua idade em números:\n')

    age = int(age)
    while age < 1 or age > 125: # aceita idades entre 1 e 125 anos
        age = input('Idade inválida. Por favor, tente novamente.\n')
    
    if age >= 18: # separa adulto de jovem/crianca de acordo com a maioridade
        fullage = 'adulto'
    else:
        fullage = 'jovem/criança'

    occupation = input('Qual sua ocupação?\n') # grava ocupacao
    while any(x.isalpha() for x in occupation) == False or all(x.isalpha() or x.isspace() for x in occupation) == False:
        occupation = input('Ocupação inválida. Revise os dados e tente novamente: ')

    occupation = occupation.lower()

    register1 = 'Nome: {}\n' \
                   'Gênero: {}\n' \
                   'Idade: {} ({})\n' \
                   'Ocupação: {}'.format(name,
                                         gender,
                                         age, fullage,
                                         occupation) # organiza o cadastro

    print('\nCadastro completo. Aqui estão suas informações:\n'
          '{}'.format(register1)) # exibe ao usuario o cadastro

    if __name__ == '__main__':
        directory = 'C:/Users/Raul/Desktop/register.txt'
        file = open(directory, 'a')
        text = ('\n[{}]'
                '\n{}'.format(current_date,
                              register1))
        file.write(text)
        file.close() # grava o cadastro no arquivo de texto


def correct(): # para corrigir o ultimo cadastro
    directory = 'C:/Users/Raul/Desktop/register.txt'
    readfile = open(directory) # abre o arquivo
    lines = readfile.readlines()
    readfile.close()
    w = open(directory, 'w')
    w.writelines([item for item in lines[:-6]]) # apaga o ultimo cadastro
    w.close() # fecha o arquivo
    register() # cria um novo cadastro

action_tuple = ('corrigir', 'registrar') # acoes disponiveis
action = input('Qual a ação desejada?'
               '\n-> "corrigir" para corrigir o último registro;'
               '\n-> "registrar" para criar novo cadastro.\n')
while action not in action_tuple: # acao invalida
    action = input('Ação desconhecida.Favor inserir ação válida'
                   '\n(corrigir/registrar)\n')

if action == 'registrar':
    register()

elif action == 'corrigir':
    correct()
