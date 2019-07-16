ing_pan = ["harina", "levadura","sal", "azucar", "agua"]

def imprimir_lista(ingredientes, nombre_producto):

    print("lista de compras de", nombre_producto)
    print("______________")
    for producto in ingredientes:
         print(producto)

imprimir_lista(ing_pan, "pan")


ing_salsa = ["tomate", "zucar", "sal", "cebolla"]
imprimir_lista(ing_salsa, "salsa de pizza")
#ejercicio anterior
list_nros = [1,2,3,4,]

def suma_cuadrados(lista_n):
    suma = 0
    for p in lista_n:
        suma = suma + (p*p)
    return suma 

print(suma_cuadrados(list_nros))


################ CONDICIONAL ###############

# == igual
# >  mayor que
# <  menor que
# >= mayor o igual que
# <= menor o igual que
# != distinto o no igual 

a = 3 
# pregunta1
if a > 3:
    print("si, a es mayor a 3")
    print("chau")
else:
    print("no, a no es mayor a 3")
# pregunta 2
if a == 3:
    print("a es igual a 3")

nota = 60
# pregunta 3
if nota >= 60:
    print("pasasteeeee!!!!!")
else:
    print("hule ya :(")


# Ej. Crear una funcion que reciba como parametro una
# nota del 1 al 100 e imprima si pasaste o te aplazaste (se aprueba con 61)

nota = 65 

def tp (nota, nombre):
    if nota > 61:
        print("si, lo has logrado!!", nombre)
    else:
        print("no,no has logrado", nombre)
    
tp(65, "laura")

# ejemplos
a = 6
if a < 5 and a >10:
    print("a es mayor a  y menor que 10")
else:
    print("a no esta en el rango, alguna de las 2 condiciones no se cumplieron ")

if a > 5 or a < 10:
    print("a es mayor que 5 o menor que 10")
else:
    print("a no es mayor que 5 ni menor que 10")

print(5>3)# verifica si es el falso o verdadero
print(5==3) 

edad = 7
if edad > 18:
    print("deberia estar en la univeridad")
elif edad  > 13:
    print("deberia estar en secundaria")
elif edad > 6:
    print("deberia estar en primaria")
else:
    print("deberia estar en su casa ")

# anidado
if edad > 18:
    print("universidad")
else:
    if edad >13:
        print("secundaria ")
    else:
        if edad > 6:
            print("primaria")
        else:
            print("bbdlc")


# Ej. Crear una funcion puntaje que reciba como parametro una nota 
# del 1 al 100 e imprima que nota sacaste
# nota < 60 ---->1
# nota entre 60 y 70 ---> 2
# nota entre 71 y 75 ---> 3
# nota entre 76 y 85 ---> 4
# nota mayor que 85 ---> 5



def puntos(nota):
    if nota > 60 and nota < 70:
        print("tu nota es 2")
    elif nota > 71 and nota < 75:
        print("tu nota es 3")
    elif nota > 76 and nota < 85:
        print("tu nota es 4")
    elif nota > 85:
        print("tu nota es 5")
    else: 
        print("no has aprobado")
    

puntos(88)
nombre = input("ingresa tu nombre")
# ej. pedir al usuario que ingrese tres numeros y mulplicarlos 
# entre si, imprimir el resultado.
#int("22") + 3 # ----> 25 

datos1 = input("ingresa el primer nro: ")
datos2 = input("ingresa el segundo nro: ")
datos3 = input ("ingresa el tercer nro: ")
operacion  = int(datos1)*int(datos2)*int(datos3)
print(operacion)

# ej2. pedir al usuario un numero del 1 al 100 y llamar a la
# funcion que retornaba la nota que creamos hace un rato 
# utilizando el valor ingresando por el usuario

########### bucle while == mientras ########
x = 3
 while x != 5: # mientras x sea distinto de 5 hacer lo siguiente 
     print("hola esto es un bucle while, se va ejecutar mientras  sea distintas ")
     x = int(input("ingresa un numero:", )) # ingresamos un valor para x
     print("el valor de  ahora es", x)
print("termino !!!")

# contador inverso
contador = 10
while contador > 0:
    print("sigo en el bucle while ")
    contador = contador - 1
    print("te quedan", contador, "oportunidades")
print("termino")
# contador 
contador = 0
while contador <10:
    print("sigo en el bucle while")
    contador = contador + 1

# usando while pedir al usuario 5 ingredientes para hacer una pizza 
# y agregar  a una lista, al final la lista
#contador = 0 
 #while contador 

 ##################
#conta = 0
#ing_lista = []
#while conta<5:
    #print("hola")
    #ingre = input("ingrese un ingrediente: ")
    #ing_lista .append(ingre)
   # print = conta + 1 
#print("los ingredientes de la pizza son: ", ing_lista)

# Ej. crea un juego de adivinar el numero como el de arriba y 
#darle pistas al usuario si el numero que ingreso es myor o menor
#pista usar elif 























































    



        
































































