
#Ejemplo 1

class planeta:
    def __init__(self, nombre, diametro, gravedad):
        self.nombre = nombre
        self.diametro = diametro
        self.gravedad = gravedad

    def obtenerInformacion(self):
        return f"{self.nombre}: Diametro {self.diametro} km, Gravedad {self.gravedad} m/s^2"

# Ejemplo de uso
tierra = planeta("Tierra", 12742, 9.8)
print(tierra.obtenerInformacion())







# Ejemplo 2

class sateliteNatural(planeta):
    def __init__(self, nombre, diametro, gravedad, orbita):
        super().__init__(nombre, diametro, gravedad)
        self.orbita = orbita

    def obtenerInformacion(self):
        return f"{self.nombre}: Diametro {self.diametro} km, Gravedad {self.gravedad} m/s^2, Orbita: {self.orbita}"

# Ejemplo de uso
luna = sateliteNatural("Luna", 3475, 1.625, "Alrededor de la Tierra")
print(luna.obtenerInformacion())







# Ejemplo 3

def mostrarInformacion(astro):
    print(astro.obtenerInformacion())

# Ejemplo de uso de polimorfismo
marte = planeta("Marte", 6779, 3.7)
mostrarInformacion(marte)

phobos = sateliteNatural("Phobos", 22, 0.0057, "Alrededor de Marte")
mostrarInformacion(phobos)
