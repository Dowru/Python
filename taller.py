# Punto 1 / Lo hice así porque me da pereza agregar uno por uno

# Creamos las listas vacias para los aprendices y las edades
aprendices = []
edades = []

# Aqui estan los nombres y edades de todos los aprendices de nuestra formación
datosC = [
    "DAHIANA RIVERA\t17",
    "JUAN MAHECHA\t17",
    "KEVIN HERNANDEZ\t17",
    "KEVIN HERNANDEZ\t17",
    "KEVIN LONDONO\t23",
    "LAURA BENAVIDEZ\t17",
    "LINA BARRIOS\t18",
    "MAICOL PRADA\t17",
    "MARIA ALAPE\t18",
    "MARIA FERNANDA\t18",
    "MARIA PEREZ\t17",
    "MARIA BUENAVENTURA\t17",
    "MARLON LOPEZ\t19",
    "MATHEW GUARNIZO\t17",
    "MATIAS GUZMAN\t17",
    "MIGUEL BERNAL\t17",
    "NATALY MONTAÑA\t17",
    "NEYLLIBER LOPEZ\t16",
    "NICOLAS FIERRO\t18",
    "NICOLAS PAULO\t17",
    "PAULA GARCIA\t20",
    "SANTIAGO GOMEZ\t18",
    "SEBASTIAN PINZON\t17",
    "SEBASTIAN TOVAR\t17",
    "STIVEN RAMIREZ\t18",
    "VANESA ALEXANDRA\t17",
    "WILFRANK FRANCISCO\t18"
]

# En un bucle for vamos a iterar a través de la lista datosC y vamos a separar los nombres y las edades para agregarlos a las listas creadas anteriormente
for elemento in datosC:
    nombre, edad = elemento.split("\t")
    aprendices.append(nombre)
    edades.append(int(edad))

# Punto 2 / Imprima las listas

print(aprendices)
print(edades)

# Punto 3 / Muestre el aprendiz con la mayor edad

mayor = max(edades)
iMayor = edades.index(mayor)
nMayor = aprendices[iMayor]

print(f"El aprendiz más viejo es {nMayor} con {mayor}")

# Punto 4 / Inserte el nombre de la instructora en la posición 1

instructora = "Adriana Rincon"
aprendices.insert(1, instructora) # o (0, instructora) no se muy bien a que se refiere con posición 1

# Punto 5 / Cuente cuantos aprendices tienen 18 años

mEdad = 18
totalA = 0
for edad in edades:
    if edad == mEdad: # O puede ser >= que significa mayor o igual a 18 años ya que no especifica la pregunta
        totalA += 1
print(f"Hay {totalA} aprendices con 18 años")

# Punto 6 / Agregue un aprendiz x al final de la lista

nAprendiz = "CRISTIAN PEÑA"
nEdad = 17
aprendices.append(nAprendiz)
edades.append(nEdad)

# Punto 7 / Borre el nombre de la instructora de la lista
if "Adriana Rincon" in aprendices:
    aprendices.remove(instructora)

# Punto 8-1 / Indique un dato a buscar en la lista de aprendices | como ejemplo, mi nombre SANTIAGO GOMEZ

if "SANTIAGO GOMEZ" in aprendices:
    print("Dato se encuentra en la lista")
else:
    print("Dato no se encuentra en la lista")

# Punto 8-2 / Indique un dato a buscar en la lista de aprendices | Lo mismo que el anterior pero con un input para que sea de selección autonoma el dato que quiera buscar

buscador = input("Ingrese un aprendiz que quiera buscar: ")
if buscador in aprendices:
    print(f"{buscador} si es un aprendiz de ADSO")
else:
    print(f"{buscador} no es un aprendiz de ADSO")

# Punto 9 / Muestre los primeros 10 aprendices de la lista

p10 = aprendices[:10]
print("Los 10 primeros aprendices ubicados en la lista son: ")
for primeros in p10:
    print(primeros)

# Punto 10 / Muestre los 10 últimos aprendices de la lista

u10 = aprendices[-10:]
print("Los 10 ultimos aprendices ubicados en la lista son: ")
for ultimos in u10:
    print(ultimos)

# Punto 11 / Muestre del elemento 10 al elemento 20

elementos1020 = aprendices[9:20]
print("Los aprendices ubicados del 10 al 20 en la lista son: ")
for mitad in elementos1020:
    print(mitad)

# En el punto 9, 10 y 11 se crea un print antes de cada bucle para que el mensaje no se repita con cada iteración


# Espero guste mi trabajo, no soy el mejor comentando codigo <3