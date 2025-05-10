#Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente
# si el apellido es el mismo, debe ordenar por nombre de manera  ascendente
# si el nombre también es el mismo, debe ordenar por nota de manera descendente

def ordenamiento_apellidos(apellidos:list,nota:list,nombres:list):
    for i in range(len(apellidos)-1):
            for j in range(i+1,len(apellidos)):
                if (apellidos[i] > apellidos[j]):

                    tem_apellido = apellidos[i]
                    apellidos[i] = apellidos[j]
                    apellidos[j] = tem_apellido

                    tem_nota = nota[i]
                    nota[i] = nota[j]
                    nota[j] = tem_nota

                    tem_nombre = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = tem_nombre
                
                #si es igual el apellido ordena por nombre
                elif (apellidos[i] == apellidos[j]):
                    if (nombres[i] > nombres[j]):  

                        tem_nombre = nombres[i]
                        nombres[i] = nombres[j]
                        nombres[j] = tem_nombre
                        
                        tem_nota = nota[i]
                        nota[i] = nota[j]
                        nota[j] = tem_nota

                    elif (nombres[i] == nombres[j]):
                        if(nota[i] < nota[j]):

                            aux_nota = nota[i]
                            nota[i] = nota[j]
                            nota[j] = aux_nota   


Estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]


ordenamiento_apellidos(Apellidos,Nota,Estudiantes)

for i in range(len(Estudiantes)):
        print(f"{Estudiantes[i]} {Apellidos[i]} se saco un  {Nota[i]}")




