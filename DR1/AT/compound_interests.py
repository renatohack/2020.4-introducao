#Este programa calcula o montante acumulado a partir de juros compostos

import matplotlib.pyplot as graphic


def capitalAcumulado():
    x = []
    y = []

    inicial = float(input("Valor inicial: "))
    rendimento = float(input("Rendimento por período (%): ")) / 100
    aporte = float(input("Aporte a cada período: "))
    periodo = int(input("Total de períodos: "))
    print()

    montante = inicial
    for i in range(1, periodo + 1):
        montante = montante * (1 + rendimento) + aporte

        print("Após", i, "períodos(s), o montante será de R$",
              round(montante, 2))

        x.append(i)
        y.append(montante)

    graphic.plot(x, y)
    graphic.show()


#MAIN
capitalAcumulado()
