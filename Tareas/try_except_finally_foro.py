
#Este ejemplo repite la solicitud hasta que se ingrese un numero
#En este caso no usamos finally, ya que este se ejecuta haya o no haya error
while True:
    try:
        x = int(input("ingresa un numero:"))
        break
    except ValueError:
        print("No ingresaste un numero, por favor ", end="")
print("has ingresado:", x)

#en este otro caso, solo nos avisa del error y sigue hasta el final
try:
    x = int(input("ingresa un numero:"))
except ValueError:
    print("ERROR, No ingresaste un numero ")
finally:
    print("has ingresado:", x)


