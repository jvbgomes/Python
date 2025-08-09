def calcular_media_idade():
    qtd_pessoas = []

    qtd_pessoas = int(input("Digite a quantidade de pessoas entrevistadas: "))

    if qtd_pessoas <= 0:
     print("O número de pessoas deve ser maior que zero.")
     return  
    soma_idades = 0   

    for i in range(qtd_pessoas):
          idade = int(input(f"Digite a idade da pessoa {i+1}: "))
          soma_idades += idade
          media_idade = soma_idades / qtd_pessoas
    print(f"A média de idade do grupo é: {media_idade:.2f} anos")