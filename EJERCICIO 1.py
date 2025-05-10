#Desarrollar una función que realice el ordenamiento de las listas por nombre 
# de manera ascendente.




def ordenamiento_nombres(nombres:list,edades:list):
    for i in range(len(nombres)-1):
            for j in range(i+1,len(nombres)):
                if (nombres[i] > nombres[j]):

                    aux_nombre = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = aux_nombre


                    aux_edad = edades[i]
                    edades[i] = edades[j]
                    edades[j] = aux_edad



Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


ordenamiento_nombres(Nombres,Edades)

for i in range(len(Nombres)):
        print(f"{Nombres[i]}, con la edad de {Edades[i]}")