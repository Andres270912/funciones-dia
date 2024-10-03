#Ejemplo para calcular el area de un triangulo
#variables de la cadena

base = int(input("ingrese la base: "))
altura = int(input("Ingrese la altura: "))

#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

#invovar la funcion
resultado = calcularAreaTriangulo(base,altura)
#salida
print(f"El area del triangulo cuya {base} y altura {altura} es: {resultado}")

#Funcion con argumentos predeterminados
def my_fuction(country = "colombia"):
     print("I am from "+country)

# invocar la funcion
my_fuction()
my_fuction("Swenden")


def mostrarEstudiantes (*args):
    print("El estudiante: "+ args[2])
mostrarEstudiantes ("Emil", "Tobias", "Linus")

def mostrarCarros (carrol, carro2, carro3):
    print("El carro es:" +carro2)

mostrarCarros (carro1 = "BMW", carro3 = "Ferrari", carro2 = "Ford")

def mostrarCliente (**kwargs):
    print("Su apellido es: "+ kwargs["apellido"])
mostrarCliente (nombre = "Tobias", apellido = "Refsnes")

def miFuncion():
    pass

#Modulo de matematicas
import math
num3= math.ceil(7.8)
num4= math.floor(7.8)

print(num3)
print(num4)
