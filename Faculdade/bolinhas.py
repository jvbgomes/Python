def busca_solucoes(caixa, linhas, colunas, bolinhas):
    if len(bolinhas) == 0:
        return [caixa]
    solucoes = []
    for i in range(linhas):
        for j in range(colunas):
            if caixa[i][j] == 0:
                for k in range(bolinhas):
                    caixa[i][j] = 1
                    solucoes.extend(busca_solucoes(caixa, linhas, colunas, bolinhas - 1))
                    caixa[i][j] = 0
    return solucoes