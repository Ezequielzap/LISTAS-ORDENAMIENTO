from listapersonas2 import *

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



mostrar_datos_mexico_ordenados()



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


mostrar_datos_de_menores()


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

ordenar_lista_codigo_postal()
