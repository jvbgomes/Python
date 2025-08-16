def decodificar_verao(mensagem):
    resultado = ""
    for letra in mensagem:
        if letra.lower() in "aeiou":
            resultado += "*"
        else:
            resultado += letra
    return resultado

def decodificar_inverno(mensagem):
    resultado = ""
    for letra in mensagem:
        if letra.lower() in "bcdfghjklmnpqrstvwxyz":
            resultado += "-"
        else:
            resultado += letra
    return resultado

chave = input("Digite a chave (verão ou inverno): ").strip().lower()
mensagem = input("Digite a mensagem secreta: ")

if chave == "verão":
    mensagem_decodificada = decodificar_verao(mensagem)
    print("Mensagem decodificada:")
    print(mensagem_decodificada)
elif chave == "inverno":
    mensagem_decodificada = decodificar_inverno(mensagem)
    print("Mensagem decodificada:")
    print(mensagem_decodificada)
else:
    print("Chave inválida!")