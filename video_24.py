saldo=1000

print("\tMenu, elija un numero\n")
print("1. Ingresar dinero")
print("2. Retirar dinero")
print("3. Mostrar saldo")
print("4. salir\n")

opcion = int(input(f"Pone un numero: "))

if opcion == 1:
    plata=float(input("Cuanto dinero desea ingresar: "))
    saldo=saldo+plata
    print(f"El saldo es: {saldo}")
elif opcion == 2:
    plata=float(input("Cuanto dinero desea retirar: "))
    saldo=saldo-plata
    print(f"El saldo es: {saldo}")
elif opcion == 3:
    print(f"El saldo es: {saldo}")
elif opcion == 4:
    print("Saliendo del menu")
else:
    print("La opcion no es correcta")
