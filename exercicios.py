print("vamos calcular seus custos com o carro")
opcoes = input("digite uma das opções: 1-carro popular 2-carro de luxo: ")
km = float(input("digite quantos km você percorreu? "))
dias = int(input("quantos dias você andou com o carro? "))

contadias = dias * 90
contadial = dias * 150

if opcoes == "1":
    if km >= 100:
        custo = km * 0.10
        print(f"Você percorreu mais de 100km. O custo total é: R${custo:.2f}")
    else:
        custo = km * 0.20
        print(f"Você percorreu menos de 100km. O custo total é: R${custo:.2f}")
    final = custo + contadias
    print(f"você tem que pagar R${final:.2f}")

elif opcoes == "2":
    if km >= 200:
        custo = km * 0.25
        print(f"Você percorreu mais de 200km. O custo total é: R${custo:.2f}")
    else:
        custo = km * 0.30
        print(f"Você percorreu menos de 200km. O custo total é: R${custo:.2f}")
    final = custo + contadial
    print(f"você tem que pagar R${final:.2f}")
    
else:
    print("opção inválida. Por favor, escolha 1 para carro popular ou 2 para carro de luxo.")   