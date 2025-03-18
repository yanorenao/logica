#Leer un numero nentero y determinar si termina en 4
#algoritmo termina en 4
#Variables
#   Entero: numero
#Inicio
#   Escriba "Por favor, digite un numero entero"
#   Lea Numero
#   Si Numero Modulo de 10 = 4 entonces
#             Escriba"El numero termina en 4"
#   Sino
#             Escriba"El numero no termina en 4""
#   finsi
#Fin
numero = 0
numero = input("Por favor, digite un numero entero: ")
print("El tipo para la varible numero es: ", type(numero))
numero = int(numero)
print("El tipo para la varible numero despues de int es : ", type(numero))

if (numero % 10) == 4:
    print("El numero termina en 4")
else:
    print("El numero no termina en 4")
    