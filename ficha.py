def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombrecompleto = input('ingrese su nombre completo: ')
    email = input('ingrese su email: ')
    nota1 = input('ingrese su nota:')
    nota2 = input('ingrese su nota:')
    nota3 = input('ingrese su nota:')
    encabezado= """========================
    FICHA DEL ALUMNO
========================"""
    nombremayuscula = nombrecompleto.title()
    nombreminuscula = nombrecompleto.lower()
    nombrecodigo = nombrecompleto.strip().upper()
    nombrelimpio = nombremayuscula.strip()
    nombrelimpio1= nombreminuscula.strip()
    notanum1 = int(nota1)
    notanum2 = int(nota2)
    notanum3 = int(nota3)
    esp = nombrelimpio.find(" ")
    esp1= nombrelimpio1.find(" ")
    nombre = nombrelimpio1[:esp1]
    apellido = nombrelimpio1[esp1+1:]
    usuario= apellido + "." + nombre
    cierre= "="*24


    print (encabezado)
    print (f"Nombre: {nombremayuscula.strip()}")
    print (f"Email: {email.lower()}")
    print (f"Caracteres en nombre: {len(nombrecompleto.strip())}")
    print (f"Iniciales: {nombrelimpio[0] + nombrelimpio[esp +1]}")
    print (f"Usuario: {usuario}")
    print (f"Email valido: {'@' in email.lower()}")
    dominio= email.find("@")
    print (f"Dominio: {email[dominio+1:].lower()}")
    print (f"Nombre para archivo: {nombremayuscula.strip().replace(' ', '_')}")
    print (f"Cantidad de a: {nombreminuscula.count('a')}")
    print (f"Codigo secreto: {nombrecodigo[::-1]}")
    print (f"Nota 1: {nota1}")
    print (f"Nota 2: {nota2}")
    print (f"Nota 3: {nota3}")
    print (f"Suma: {notanum1 + notanum2 + notanum3}")
    print (f"Promedio: {(notanum1 + notanum2 + notanum3)/3}")
    print (f"Promedio entero: {(notanum1 + notanum2 + notanum3)//3}")
    print (cierre.strip())







