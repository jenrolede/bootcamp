print(2*5)
print(3+9)
print(4*4)#multplica
print("hola mundo")
print("Hello People")#emprime el texto
print("hola mundo" +"22")#une texto con numeros
print("hola mundo" * 20) #multplica el texto 20 veces 
print(2+2)#suma de enteros
################
a = 2*2# multiplicacion de la variable a
print(a)
a = 2#datos de la variable a
b = 5#datos de la variable b
print(a+b)#muestra de la suma de variables asignados mas arriba 
print(a,b)# la coma separa los valores en este caso las variables a y b
print("toy",4)#muestra de texto con espacio  es decir separar datos 
print(a,b,"holi")#imprimir variables con texto entre espacios


#ej.crear una variable nombre y una edad
#con sus nombres y edades e imprimir:
#hola, me llamo.... y tengo... anos 
nombre ="Jenny"
edad = 20
print( nombre , edad)
print("hola, me llamo", nombre, "y tengo", edad, "anos")#imprimir texto utilizando coma para separar la variables 

lista_vacia = []
listax = [1,2,6,8]
print(lista_vacia)
print(listax)
datos = ["jenny"]
print(datos)
alumnos = ["jose", "ramoncito", nombre,"martha"]
print(alumnos)
#nro_alumnos = 3
print(alumnos[2], alumnos[0])

#ej.crar una lista datos que en el primer lugar este tu nombre
#y en la segunda posicion este tu edad
#imprimir "hola me llamo___, y tengo ___ anos"


datos  = ["jenny", 20] # info de  lista 
print("hola me llamo",datos[0],"y tengo",datos[1],"anos")
datos[1] = 15
print("hola me llamo",datos[0],"y tengo",datos[1], "anos")#cambio de valor de la lista 

datos.append("estudiante")# .append se utiliza para agg datos a la lista, el punto indica accion 
print(datos)
print(datos[2])

#ej.Agregar una profesion y un hobby a la lista previa mente creada (usar append)
datos.append("estudiante")
datos.append("diy")
print(datos[4]) #info agg en una lista ya creada
print(datos)#imprimir una lista completa
datos.pop()# el pop saca una info de la lista,en este caso  el ultimo valor
print(datos)
datos.pop()


#funcion len() _dimension/longitud en ingles  
print(datos)
dimension_de_datos = len(datos) # en nombre de variables se utiliza guion bajo
print(dimension_de_datos)
datos.pop()
print(datos)
print(len(datos))# longitud de caracteres 
saludo = "hola,que tal"
print(saludo)
print(len(saludo)) #imprimimos la dimension de la lista datos 

#ej. obtener la dimension de la lista datos e imprimir:
#"la lista de datos tiene ____ elementos"
print("la lista de datos tiene", len(datos), "elementos") #texto, accion de dimension mas variable,texto

#ej.imprimir el ultimo elemento de una lista que no sabemos 
#cuantos elementos tiene, pista usar len ()
#no hacer lista_larga[27]
lista_larga = [2,3,3,3,3,3,3,3,3,4,5,5,6,6,6,6,6,6,6,66]
print(lista_larga)
print(len(lista_larga))#cantidad de elementos
print(len(lista_larga) - 1)#formula
print(lista_larga[len(lista_larga) -1])#formula general para hallar el ultimo elemento


###########bucles/loops/ciclos/iteraciones #####3
listas_temas = ["variables","listas","tipos de datos"]
#cuando se utiliza dos puntos siempre hay un bloco de codigos

for concepto in listas_temas:
    print("hoy aprendi", concepto)
    print("que gusto")
print("esto es lo que aprendi hoy") # salir de la orden de la tabulacion evita la repeticion 

#for variable in lista_o_rango:
    #bloque de codigo
   # print("esto se repite")
#print("esto no se repite")

#ej.recorrer una lista con for  e imprimir en cada ciclo 
#el valor del elemento con 3 signos de admiracion 
#variables !!!

listas_emociones = ["felicidad","amor","techagau","rabia","melancolia","conejo"]

for describo in listas_emociones:
    print("hoy siento",describo)
print("fin!!")#fuera del bucle significa fuera del orden

for x in range (10):#range se pone adentro del parentesis un valor repite las veces indicadas
    print("hola")
    print("hola", x)# cuando  aggs una variable   se enumera los elementos

#ej- imprimir los numeros del 1 al 100 usando fory range
for j in range (101):
    print ("n", j)

#ej2 imprimir el resultado de la suma de los numeros 
#del 1 al 10 - 1+2+3+4+5+6+7+8+9+10 = 55

sumas = (1+2+3+4+5+6+7+8+9+10)
print(sumas)
#range = (1+2+3+4+5+6+7+8+9+10)




