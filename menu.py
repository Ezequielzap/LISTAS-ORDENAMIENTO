from listapersonas2 import nombres,telefonos,mails,address,postalZip,region,country,edades


#1
def importar_listas()->list:
    from listapersonas2 import nombres,telefonos,mails,address,postalZip,region,country,edades
    for i in range(len(nombres)):
        print(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i])
#2
def iniciar_lista_datos_mexico()->list:
    for i in range(len(country)):
        if country[i] == "Mexico":
            print(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i])

#3
def iniciar_lista_datos_brazil()->list:
    for i in range(len(country)):
            if country[i] == "Brazil":
                print(nombres[i], mails[i], telefonos[i], edades[i])
#4
def iniciar_lista_jovenes()->list:
    edad_menor = edades[0]
    for i in range(len(edades)):
        if edades[i] <= edad_menor:
            edad_menor = edades[i]
            print(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i])
#5
def calcular_promedio_edad()->list:
    suma = 0 
    for i in range(len(edades)):
        suma += edades[i]
    promedio_edad = suma / len(edades)
    print(f"el promedio de edad de los usuarios es de {promedio_edad}")
#6 
def iniciar_lista_usuario_mayor()->list:
    edad_mayor = 0
    nombre_mayor = ""
    for i in range(len(country)):
        if country[i] == "Brazil":
           if edades[i] > edad_mayor:
                    edad_mayor = edades[i]
                    nombre_mayor = nombres[i]
    print(nombre_mayor, edad_mayor)
#7
def iniciar_lista_codigo_postal()->list:
    for i in range(len(country)):
        if country[i] == "Brazil" or country[i] == "Mexico":
            if postalZip[i] > 8000:
                print(nombres[i])
#8
def iniciar_lista_italianos()->list:
    for i in range(len(country)):
        if country[i] == "Italy" and edades[i] > 40:
            print(nombres[i], mails[i], telefonos[i])

#9
def mostrar_datos_mexico_ordenados()->list:
    lista_datos_mexicanos = []
    for i in range(len(country)):
        if country[i] == "Mexico":
            lista_datos_mexicanos.append((nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i],country[i],edades[i]))

    for i in range(len(lista_datos_mexicanos)- 1):
        for j in range(i+1,len(lista_datos_mexicanos)):
                if (lista_datos_mexicanos[i] > lista_datos_mexicanos[j]):

                    aux_nombre = lista_datos_mexicanos[i]
                    lista_datos_mexicanos[i] = lista_datos_mexicanos[j]
                    lista_datos_mexicanos[j] = aux_nombre


    for i in range(len(lista_datos_mexicanos)):
        print(lista_datos_mexicanos[i])

#10
def mostrar_datos_de_menores()->list:
    edad_menor = edades[0]
    lista_datos_menores = []
    
    for i in range(len(edades)):
        if edades[i] <= edad_menor:
            edad_menor = edades[i]
    
    for i in range(len(edades)):
        if edades[i] == edad_menor:
            lista_datos_menores.append((nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i],country[i],edades[i]))

    for i in range(len(lista_datos_menores)- 1):
        for j in range(i + 1,len(lista_datos_menores)):
                if (lista_datos_menores[i] > lista_datos_menores[j]):

                    aux_edad = lista_datos_menores[i]
                    lista_datos_menores[i] = lista_datos_menores[j]
                    lista_datos_menores[j] = aux_edad

                elif (lista_datos_menores[i] == lista_datos_menores[j]):
                        
                        aux_nombre = lista_datos_menores[i]
                        lista_datos_menores[i] = lista_datos_menores[j]
                        lista_datos_menores[j] = aux_nombre

    for i in range(len(lista_datos_menores)):
         print(lista_datos_menores[i])


#11
def ordenar_lista_codigo_postal()->list:
    lista_de_codigo_postal = []
    for i in range(len(country)):
        if country[i] == "Brazil" or country[i] == "Mexico":
            if postalZip[i] > 8000:
                lista_de_codigo_postal.append((nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i],country[i],edades[i]))

    for i in range(len(lista_de_codigo_postal)):
        for j in range(i + 1,len(lista_de_codigo_postal)):
                if (lista_de_codigo_postal[i] > lista_de_codigo_postal[j]): 

                    aux_nombre = lista_de_codigo_postal[i]
                    lista_de_codigo_postal[i] = lista_de_codigo_postal[j]
                    lista_de_codigo_postal[j] = aux_nombre
            

    for i in range(len(lista_de_codigo_postal)):
         print(lista_de_codigo_postal[i])






def entrar_a_menu():
    print("opciones: \n1-Importar listas\n2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años")
    opcion = int(input("seleccione opcion: "))
    match opcion:
        case 1:
            importar_listas()
        case 2:
            iniciar_lista_datos_mexico()
        case 3:
            iniciar_lista_datos_brazil
        case 4:
            iniciar_lista_jovenes()
        case 5:
            calcular_promedio_edad()
        case 6:
            iniciar_lista_usuario_mayor()
        case 7:
            iniciar_lista_codigo_postal()
        case 8:
            iniciar_lista_italianos()
        case 9:
            mostrar_datos_mexico_ordenados()
        case 10:
            mostrar_datos_de_menores()
        case 11:
            ordenar_lista_codigo_postal()




entrar_a_menu()