def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def mostrar_menu():
    print("CALCULADORA")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")

def main():
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))

    if opcion == '1':
        print(sumar(num1, num2))
    
    if opcion == '2':
        print(restar(num1, num2))

    if opcion == '3':
        print(multiplicar(num1, num2))

    if opcion == '4':
        print(dividir(num1, num2))

if __name__ == "__main__":
    main()

    