velocidade = float(input("Qual a velocidade atual do carro? "))
if velocidade > 80 :
    multa = (velocidade - 80) * 7 
    print("MULTADO!! Você excedeu o limite permnitido que é de 80 km/h.\nVocê deve pagar uma multa de R${:.2f}!".format(multa))
print("Tenha um bom dia! Dirija com segurança!")