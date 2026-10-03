def converter_minutos(horas):
    return horas * 60

horas = int(input("Digite a quantidade de horas: "))
resultado = converter_minutos(horas)

print("O total em minutos é:", resultado)