def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass

    Nombre= input('ingrese su nombre: ')
    apellido= input('ingrese su apellido: ')

    nombre_completo = Nombre + " " + apellido

    print((nombre_completo).lower())
    print((nombre_completo).title())
    print((nombre_completo).upper())
    print("\t" + nombre_completo.lower())