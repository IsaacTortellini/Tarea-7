print("Calculadora de numeros ENTEROS")
print("1-Suma")
print("2-Resta")
print("3-Multiplicacion")
print("4-Division")
print("5-Salir")

opcion = int (input ("Seleccione una operacion: "))
if opcion == 1:
    print("Selecciono: Suma")
    nu1=int(input("Primer Numero: "))
    nu2=int(input("Segundo Numero: "))
    nu3=nu1+nu2
    print("Resultado: ",nu3)

elif opcion == 2:
    print("Selecciono: Resta")
    nu1=int(input("Primer Numero: "))
    nu2=int(input("Segundo Numero: "))
    nu3=nu1-nu2
    print("Resultado: ",nu3)
elif opcion == 3:
    print("Selecciono: Multiplicacion")
    nu1=int(input("Primer Numero: "))
    nu2=int(input("Segundo Numero: "))
    nu3=nu1*nu2
    print("Resultado: ",nu3)
elif opcion == 4:
    print("Selecciono: Division")
    nu1=int(input("Primer Numero: "))
    nu2=int(input("Segundo Numero: "))
    if nu2==0:
     print("ERROR")
    else:
     nu3=nu1/nu2
     print ("Resultado",nu3)
elif opcion == 5:
     print ("Adios!")
     sys.exit()