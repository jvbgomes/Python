livros = []

def cadastrar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor: ")
    ano = int(input("Ano de publicação: "))
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    livros.append(livro)
    print("Livro cadastrado com sucesso!\n")
    
def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.\n")
    else:
        print("Lista de livros:")
        for livro in livros:
            print(f"- {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")
        print(' ')
        
def buscar_por_autor():
    nome_autor = input("Digite o nome do autor: ")
    encontrados = [livro for livro in livros if livro['autor'].lower() == nome_autor.lower()]
    if encontrados:
        print("Livros encontrados:")
        for livro in encontrados:
            print(f"- {livro['titulo']} ({livro['ano']})")
    else:
        print("Nenhum livro encontrado desse autor.")
    print(' ')
    
def buscar_por_intervalo_ano():
    inicio = int(input("Ano inicial: "))
    fim = int(input("Ano final: "))
    encontrados = [livro for livro in livros if inicio <= livro['ano'] <= fim]
    if encontrados:
        print("Livros encontrados:")
        for livro in encontrados:
            print(f"- {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")
    else:
        print("Nenhum livro encontrado nesse intervalo de anos.")
    print(' ')

while True:
        print("=== Biblioteca Doméstica ===")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar por autor")
        print("4. Buscar por intervalo de anos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_por_autor()
        elif opcao == "4":
            buscar_por_intervalo_ano()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.\n")