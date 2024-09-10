print("intoduccion a clases")
class Animal:
    edad=3
    raza="chihuas"
    comida="croquetas"
    def come(self):
        print(f"el perro come "+self.comida)
print(Animal)
print("creando el objeto de la clase Animal ")
perro=Animal()

print(f"edad del perro{perro.edad}")
print(f"raza del perro{perro.raza}")

perro.come