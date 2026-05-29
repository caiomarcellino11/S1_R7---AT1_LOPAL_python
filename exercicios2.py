print("vamos fazer um reajuste de salário")

salario = float(input("Digite o salário atual: "))

sexo = input("Digite o sexo (M/F): ").upper()

anos_empresa = int(input("Digite quantos anos esse funcionário trabalha na empresa: "))

if sexo == "F":
    if anos_empresa < 5:
        reajuste = salario * 0.04
    elif anos_empresa >= 5 and anos_empresa <= 10:
        reajuste = salario * 0.07   
    elif anos_empresa >= 15 and anos_empresa <= 20:
        reajuste = salario * 0.12
    else:
        reajuste = salario * 0.23


elif sexo == "M":
    if anos_empresa < 5:
        reajuste = salario * 0.03
    elif anos_empresa >= 5 and anos_empresa <= 15:
        reajuste = salario * 0.08
    elif anos_empresa >= 20 and anos_empresa <= 30:
        reajuste = salario * 0.14
    else:        reajuste = salario * 0.25

print(f"O reajuste salarial é: R${reajuste:.2f}")
salario_final = salario + reajuste
print(f"O salário final é: R${salario_final:.2f}")