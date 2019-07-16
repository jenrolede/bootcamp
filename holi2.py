# Tipo de dato STRING/str de texto
"esto es un string"
#tipo de dato integerentero/int
105
#Listas
# [] #lista vacia
lista_corta = ["Jenny", 33, "estudiante "] #LISTA DE 3 ELEMENTOS

#variables
nombre = "Jenny"
edad = 18+2
edad_mal = "18+2"
variable_lista = ["hola", nombre, 30]
#acceder a un elemento de la lista

print(variable_lista[0], edad, variable_lista[2])

#acciones/operaciones sobre lista
variable_lista.append("viajar") #agregar elemento a la lista al final
variable_lista.pop#eliminar el ultimo elemeto
variable_lista[2] = 50
print(variable_lista)

#bucles/loop/ciclos
#imprimir cada elemeto
for infos in variable_lista:
    print(infos) 
print(len(variable_lista))
#imprimir los numeros de 1 al 10
#ej1
for lacosa in range (10):
    print(lacosa)
#ej2
for lacosa in range (10):
    print(lacosa + 1)
#ej3
for lacosa in range (1,11):
    print(lacosa)
#ej4 el primer nro es el indice y el otro el final

#imprimir el ultimo elemeto de una lista de una lista sin saber cuantos
#elementos tiene, solucion general
otra_lista = [2, "holi","lechuga",10]
otra_lista.append("aaaaaaaa")
print(otra_lista)
print(otra_lista[len(otra_lista)-1])#formula para imprimir el ultimo elemeto

#solucion paso por paso
dimension_de_lista = len(otra_lista) - 1
print("la dimension de otra_lista es", dimension_de_lista)
indice_el_ult = dimension_de_lista - 1
print("el indice del ultimo elemento es", indice_el_ult)
otra_lista[indice_el_ult]
print(otra_lista[indice_el_ult])

#solucion una linea
print(otra_lista[len(otra_lista) - 1])
#formula de la operacion print(nombre_lista[len(nombre_lista) - 1])

#for nombredevariable in range (valor numerico):

for valores in range(1, 11):
    print(valores)

#imprimir hola 10 veces
for valores in [1,2,3,4,5,6,7,8,9,10]:
    print("hola", valores) #imprimir valores es opcional

#imprimir el resultado del 1 al 10 = 55

#solucion1
#nombre_de_lista=[1,2,3,4,5,7,8,9,10] #se crea una lista
prueba=[1,2,3,4,5,6,7,8,9,10]#se crea una lista
a=0#se crea una variable base
for x in prueba:#sea crea un ciclo que va correr
    a=a+x#se va acumulando las sumas parciales
print(a)

#solucion2
sumatoria=0
for valor in range(1,11):
    sumatoria= sumatoria + valor 
print(sumatoria)

######   funciones  ######
#def nombre_de_la_funcion(argumento):
def saludo(quien):
    print("hola", quien)
saludo("jenny")

def suma(numb1, numb2):
    resultado = numb1+numb2
    return resultado
suma(1,5)
suma(2,6)
print(suma(5,10))
result = suma(5,8)
print(result)

#crear una funcion resta, que reciba como parametro dos numeros
#y retorno la resta de esos numeros
#luego llamar a la uncion a imprimir el resultado 

def resta(nro1, nro2):
    resultado = nro1-nro2
    return resultado #retornar del resultado 

resta(10,2) #pasamos los nros
resta(8,4)
print(resta(10,2)) # mostramos el resultado 
result = resta (8,4)
print(result)

# mismo ejercicio  con ej de multiplicacion 

def multiplicacion(nro1, nro2):
    resultado = nro1*nro2 # especiicamos la operacion con simbolos y argumetos
    return resultado


print(multiplicacion(2,2))
result = multiplicacion (2,3)
print(result)

#formula
#def nombre_funcion(argumento) _codigo_

#crear una funcion saludo que reciba como parametro nombre y edad
#imprima "hola soy "___ y tengo ____ anos 
#llamar varias veces a la funcion con distintos valores 
#nota:retornar algo es opcional 




def datos (nombre, edad):
    print("hola soy", nombre,"y tengo", edad, "anos") # con la funcion print agregue el texto con los parametros, 
#obs con la funcion print solo funciona si esta dentro de la funcion        

datos("jenny", 20)# llamada de la funcion y di  el valor 

#ej. crear la funcion suma_lista que reciba como argumento una lista de numero
#y retorne la suma de sus elementos
#pista: usar for y una variable acumulador 

lista_nro = [1,2,3,4,5] #1+2+3+4+5= 15
#pista2, la llamada deberia ser:
#suma_lista(listit
#pista3
 #def suma_lista(una_lista)
#suma = 0
#codigo
#codigo
listita = [1,2,3,4,5]

def sumatoria (listita):
    suma = 0
    for x in sumatoria:
        suma = suma + x
 #return suma 

sumatoria(listita)
result = sumatoria(listita)
print(resul)


def lista_cuadrado(listajeyma):
    a = [] #lista vacia
    for jeyma in listajeyma:
        a.append(jeyma*jeyma)
    return a

otravez = [1,4,9,16,25]     
resultado_cuad = lista_cuadrado(otravez)  
print(resultado_cuad)

###############
#ej eliminar todos los elementos de una lista utizando for

grupo5 = ["n","f1","f2", "a"] 
print("antes", grupo5)
for j in range (len (grupo5)):
    grupo5.pop()
print("despues", grupo5)


#crear una funcion suma_cuadrado que reciba una lista de numeros
#retorna el valor de la suma de cada numero al cuadrado
#[1,2,3,4] --> 1+4+9+16 -> 30

ingr_pan = ["harina", "levadura", "sal", "aucar", "agua"]

def imprimir_lista(ingredientes):
    for producto in ingredientes:
        print(producto)
imprimir_lista(ingr_pan)

































