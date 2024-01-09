def menu():
    print("1. Fazer uma ligação")
    print("2. Cadastrar um contato")  #Função para mostrar o menu principal
    print("3. Remover um contato")
    print("4. Sair")


def fazer_ligacao(contatos):
    nome = input("Digite o nome do contato para ligar: ")
    try:
        telefone = contatos[nome]
        print(f"Ligando para {nome} no número {telefone}")            #Função para fazer uma ligação
    except KeyError:
        print(f"Contato {nome} não encontrado na lista.")


def cadastrar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")           #Função para cadastrar um contato
    contatos[nome] = telefone
    print(f"Contato {nome} cadastrado com sucesso.")


def remover_contato(contatos):
    nome = input("Digite o nome do contato para remover: ")                #Função para remover um contato
    try:
        del contatos[nome]
        print(f"Contato {nome} removido da lista.")
    except KeyError:
        print(f"Contato {nome} não encontrado na lista.")


def main():     #Função principal
    contatos = {}  #Dicionário para armazenar os contatos
    while True:
        menu()
        opcao = input("Escolha uma opção (1/2/3/4): ")
        try:
            opcao = int(opcao)
            if opcao == 1:
                fazer_ligacao(contatos)
            elif opcao == 2:
                cadastrar_contato(contatos)
            elif opcao == 3:
                remover_contato(contatos)
            elif opcao == 4:
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
