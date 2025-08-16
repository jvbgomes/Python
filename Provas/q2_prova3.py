receitas = []

def listar_receitas():
    if not receitas:
        print("Nenhuma receita cadastrada ainda.\n")
    else:
        print("Receitas cadastradas:")
        i = 1
        for receita in receitas:
            print(f"{i}. {receita['nome'].title()}")
            print("   Ingredientes:")
            for ing in receita['ingredientes']:
                print("   -", ing)
            i += 1
        print()

def adicionar_receita():
    nome = input("Nome da receita: ")
    ingredientes = []

    print("Digite até 3 ingredientes (pressione Enter para parar antes se quiser menos):")
    for i in range(3):
        ing = input(f"Ingrediente {i+1}: ")
        if ing == "":
            break
        ingredientes.append(ing)

    receita = {"nome": nome, "ingredientes": ingredientes}
    receitas.append(receita)
    print(f"Receita '{nome}' adicionada com sucesso!\n")
    
def buscar_por_ingrediente():
    ingrediente = input("Digite o ingrediente para buscar receitas: ").strip().lower()
    encontradas = []

    for receita in receitas:
        if ingrediente in receita['ingredientes']:
            encontradas.append(receita)

    if len(encontradas) > 0:
        print("Receitas encontradas com esse ingrediente:")
        for r in encontradas:
            print(f"- {r['nome'].title()}")
            print("  Ingredientes:")
            for ing in r['ingredientes']:
                print("  -", ing)
    else:
        print("Nenhuma receita contém esse ingrediente.")
    print()

while True:
        print("=== Gerenciador de Receitas ===")
        print("1. Adicionar nova receita")
        print("2. Listar todas as receitas")
        print("3. Buscar receitas por ingrediente")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_receita()
        elif opcao == "2":
            listar_receitas()
        elif opcao == "3":
            buscar_por_ingrediente()
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")