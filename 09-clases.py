class OperacionesBasicas:
    num1 = 0
    num2 = 0
    res = 0

    #se declara el this (en java) que es self
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    #se declara los metodos
    def suma(self, a):
        self.num1 = a
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))

    def resta(self):
        self.res = self.num1 - self.num2
        print("La resta es: {}".format(self.res))

#se hace la instancia fuera de la clase
def main():
    obj = OperacionesBasicas()
    obj.suma(10)
    obj.resta()

#controlar la manera de como se ejecuta el programa
if __name__ == "__main__":
    main() #Aqui inicia la aplicacion