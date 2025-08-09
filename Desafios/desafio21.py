def gerar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = min(i, j, n - 1 - i, n - 1 - j) + 1
            linha.append(valor)
        matriz.append(linha)
    return matriz

while True:
    entrada = input().strip()  
    if not entrada:
        continue 
    n = int(entrada) 
    if n == 0:
        break

    matriz = gerar_matriz(n)

    for i in range(n):
        for j in range(n):
            print (matriz)[i][j],
        print
    print
