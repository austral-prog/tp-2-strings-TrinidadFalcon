def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto=float(input("Ingresar gasto:"))
    dinero=int(input( "Dinero recibido"))

    print("Ingresar gasto:"+'\n'+ f"{gasto}")
    print("Dinero recibido" + '\n' + f"{dinero}")

    Vuelto=dinero-gasto
    Pesos= int(Vuelto)
    Centavos= (Vuelto-Pesos)*100


    print("\nVuelto\n")
    print("Pesos:")
    print (Pesos)
    print("Centavos:")
    print(int(round(Centavos)))

