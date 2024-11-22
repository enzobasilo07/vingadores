from registro.herois import Heroi
import os

class Interface:

    @staticmethod
    def imprimir_titulo_app():
        print('''
    
█▀█ █▀▀ █▀▀ █ █▀ ▀█▀ █▀█ █▀█   █░█ █▀▀ █▀█ █▀█ █ █▀
█▀▄ ██▄ █▄█ █ ▄█ ░█░ █▀▄ █▄█   █▀█ ██▄ █▀▄ █▄█ █ ▄█
        ''')

    @staticmethod
    def apresentar_menu_principal():
        os.system('cls')
        Interface.imprimir_titulo_app()
        print('Menu principal\n')
        print('1. Cadastrar Vingador')
        print('2. Listar herois cadastradros')
        print('3. Listar detalhes de um vingador específico')
        print()
        Interface.ler_opcao_usuario()

    
    @staticmethod
    def imprime_titulo_tela(titulo):
        os.system('cls')
        Interface.imprimir_titulo_app
        print(f'{str(titulo).upper()}')
        print('-' * 20)
        print()

    @staticmethod
    def cadastrar_herois():
        Interface.imprime_titulo_tela('Cadastrando novo carro')
        nome_heroi = input('Nome de Herói:')
        nome_real = input('Nome verdadeiro:')
        raca = input('Informe qual sua raça:')
        poderes = input('Informe seus poderes:')
        poder_principal = input('Informe seu poder principal:')
        fraquezas = input('Informe suas fraquezas:')
        nivel_forca = input('Informa qual o seu nível de força:')

        heroi = Heroi(nome_heroi, nome_real, raca, poderes, poder_principal, fraquezas, nivel_forca)

        return f'O heroi cadastrado: \n{heroi}'

    @staticmethod
    def ler_opcao_usuario():
        opcao = int(input('Digite sua opção: '))

        if opcao == 1:
            print()
            Interface.cadastrar_herois()
            Heroi.listar_herois()
            Interface.voltar_ao_menu_principal()
        elif opcao == 2:
            Interface.imprime_titulo_tela('listando carros')
            Heroi.listar_herois()
            Interface.voltar_ao_menu_principal
        elif opcao == 3:
            print('Encerrando o programa')
            exit()
        else:
            print('Erro')

    @staticmethod
    def voltar_ao_menu_principal():
        input('Pressione ENTER para voltar ao menu')
        print()
        os.system('cls')
        Interface.apresentar_menu_principal()