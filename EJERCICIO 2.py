#Desarrollar una función que realice el ordenamiento de las listas 
# por nombre de manera ascendente
# si el nombre es el mismo, debe ordenar por puntos de manera descendente


def ordenamiento_nombres_y_puntos(lista1:list,lista2:list):
    for i in range(len(lista2)-1):
            for j in range(i+1,len(lista2)):

                if (lista2[i] > lista2[j]): 

                    aux = lista2[i]
                    lista2[i] = lista2[j]
                    lista2[j] = aux

                    aux2 = lista1[i]
                    lista1[i] = lista1[j]
                    lista1[j] = aux2

                elif lista1[i] == lista1[j]:
                      if lista2[i] < lista2[j]:
                            
                            aux2 = lista2[i]
                            lista2[i] = lista2[j]
                            lista2[j] = aux2

                            aux2 = lista1[i]
                            lista1[i] = lista1[j]
                            lista1[j] = aux2



Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","CienciasSociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57]

ordenamiento_nombres_y_puntos(Nombres,Puntos)

for i in range(len(Nombres)):
        print(f"{Nombres[i]}, con {Puntos[i]} puntos ")

