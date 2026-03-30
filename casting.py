def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""


    precio=input()
    descuento=input()
    cantidad=input()

    preciodescuento=int(precio)-float(descuento)
    total=preciodescuento*int(cantidad)

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {preciodescuento}")
    print(f"Total: {total}")



