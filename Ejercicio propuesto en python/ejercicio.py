#Se debe desarrollar una aplicación en Python que permita llevar el control de novedades de los equipos que se encuentran en los diferentes ambientes.La aplicacion debe permitir:
# -Agregar los equipos de cómputo con su ID y dispositivos (cargador y mouse)utilizando un diccionario para almacenar la informacion de cada equipo.
# -Agregar novedades sobre los equipos de computo, fecha y descripcion.
# -Buscar un equipo de computo utilizando su ID y mostrar su informacion.
# -Mostrar un reporte de equipos que presentan novedades utilizando una función que recorra la lista de novedades y muestre solo las que correspondan a equipos que presentan novedades.
# -Se deben crear funciones para agregar, modificar y eliminar equipos, asi como para mostrar la lista completa de equipos y su estado actual 

# Se crea un diccionario para almacenar informacion de equipos
equipos = {}
# Se crea una lista para almacenar las novedades
novedades = []
# el while es el bucle principal ya que se ejecutara indefinidamente hasta que el usuario indique salir
while True: 
    print("Opciones de la aplicacion: ")
    print("A. Agregar un equipo de computo")
    print("B. Agregar una novedad sobre un equipo")
    print("C. Buscar un equipo por ID")
    print("D. Mostrar reporte de equipos con novedades")
    print("S. Salir")
    
    opcion = input("Digite la opcion a realizar : ")

    if opcion.lower() == 'a':
        idEquipo = input("Ingrese el ID del equipo que desea agregar: ")
        cargador = input("Ingrese el estado del cargador (En buen estado/En mal estado): ")           
        mouse = input("Ingrese el estado del mouse (En buen estado/En mal estado): ")
        equipos[idEquipo] = {"Cargador": cargador, "Mouse": mouse} #es un diccionario anidado donde un diccionario esta dentro de otro diccionario como un valor asociado. 
    elif opcion.lower() == 'b':
        idEquipo = input("Ingrese el ID del equipo al que le va a registrar una novedad: ")
        fecha = input("Ingrese la fecha de la novedad: ")
        descripcion = input("Describa la novedad del equipo: ")
        novedades.append({"ID del equipo": idEquipo, "Fecha de la novedad": fecha, "Novedad": descripcion}) #El metodo append es para agregar en la lista de novedades
    elif opcion.lower() == 'c':
        idEquipo = input("Ingrese el ID del equipo que desea buscar: ")
        if idEquipo in equipos: #La condicion busca que el ID ingresado se encuentre en el diccionario 'equipos'
            print("Datos del equipo:")
            print(f"El ID del equipo es: {idEquipo}, El estado del cargador es {equipos[idEquipo]['Cargador']} y el mouse esta en {equipos[idEquipo]['Mouse']}") #Esta cadena de texto imprimira los datos del equipo
        else:
            #En caso de que no se encuentre el ID del equipo se imprima el mensaje.  
            print("El equipo no se encuentra en la base de datos") 
    elif opcion.lower() == 'd':
            # Nos falta realizar el reporte 

    elif opcion.lower() == 's': #Cuando la opcion ingresada sea = 's' se rompera el ciclo 
        break #termina el ciclo
    else:
        #En caso de que el usuario digite una opcion no valida, se imprimira este mensaje. 
        print("La opcion que ingreso no es valida, verifique las opciones e ingrese una correcta")

# Cuando se rompe el ciclo se imprimira este mensaje. 
print("El Programa a finalizado con exito :D ")