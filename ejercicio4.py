#leer un numero entero de dos digitos y calcular la suma de ellos
'''
varibles
entero numero digito1 digito2 sumadigitos
Inicio 
    Escriba"digite un numero entero: "
    Lea numero
    si numero < 0 entonces
        numero = numero * -1
    fin si
    si numero >= 10 and numero <= 99 entonces
        digito1 = numero/10
        digito2 = numero modulo 10
        sumadigitos = digito1 + digito2
        Escriba"la suma de los digitos es: sumadigitos"
    si no
        Escriba"El numero no es de dos digitos"
    fin si
Fin
'''


