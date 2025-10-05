def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Media Móvil Simple (MA) básico
def media_movil(lista, ventana):
    return [sum(lista[i:i+ventana])/ventana for i in range(len(lista)-ventana+1)]

def main():
    print("Calculadora básica")
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elige una opción (1/2/3/4): ")

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        print("Resultado:", suma(a, b))
    elif opcion == '2':
        print("Resultado:", resta(a, b))
    elif opcion == '3':
        print("Resultado:", multiplicacion(a, b))
    elif opcion == '4':
        print("Resultado:", division(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()