import os
from colorama import Fore, init
init(autoreset=True)  
from cidades import *
def limpar_tela():
    os.system('cls' if os.name == "nt" else 'clear')
def pausar():
    input(f"{Fore.BLUE}Digite ENTER para continuar...")

def exibir_menu():
    print(f"{Fore.LIGHTBLUE_EX}=====MENU=====")
    print(f"{Fore.BLUE}1. Listar Cidades")    
    print(f"{Fore.BLUE}2. Adicionar Cidades")    
    print(f"{Fore.BLUE}3. Buscar Cidades")    
    print(f"{Fore.BLUE}4. Atualizar Cidades")    
    print(f"{Fore.BLUE}5. Excluir Cidades")    
    print(f"{Fore.BLUE}0. Sair ")

def processar_opcao(opcao):
    if opcao == "1":
        cidades = ler_cidades()
        for cidade in cidades:
            print(f" -> {Fore.LIGHTBLUE_EX}{cidade} \n")

    elif opcao == "2":
        nome_cidade = input("Digite o nome da cidade: ")
        adicionar_cidade(nome_cidade)
        print("CIDADE CADASTRADA COM SUCESSO!")

    elif opcao == "3":
          nome_cidade = input("Digite o nome da cidade a ser buscada: ")
          cidades_encontradas = buscar_cidades(nome_cidade)
          print("CIDADES ENCONTRADAS: ")
          for cidade in cidades_encontradas:
              print(cidade)
    elif opcao == "4":
          nome_antigo = input("Digite o nome da cidade a ser atualizada: ")
          nome_novo = input("Digite o novo nome da cidade: ")
          if atualizar_cidade(nome_antigo, nome_novo):
              print("CIDADE ATUALIZADA...")
          else:
              print("CIDADE NAO ENCONTRADA")

    elif opcao == "5":
        nome_cidade = input("Digite o nome da cidade a ser excluida: ")
        if excluir_cidade(nome_cidade):
              print("CIDADE EXCLUIDA...")
        else:
              print("CIDADE NAO ENCONTRADA")

    elif opcao == "0":
         print("Saindo do sistema...")
         exit(0)
    else:
         print(f"{Fore.RED}Opcao invalida!")


        

def executar_sistema():
    exibir_menu()
    opcao = input("Digite a opção desejada:")
    limpar_tela()
    processar_opcao(opcao)
    pausar()
    executar_sistema()


executar_sistema()  