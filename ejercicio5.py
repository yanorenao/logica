#leer un numero entero de dos digitos y decir si ambos son pares
'''
varibles
entero numero digito1 digito2 
Inicio 
    Escriba"digite un numero entero: "
    Lea numero
    si numero < 0 entonces
        numero = numero * -1
    fin si
    si numero >= 10 and numero <= 99 entonces
        digito1 = numero/10
        digito2 = numero modulo 10
        si digito1 modulo 2 = 0 and digito2 modulo 2 = 0 entonces
            Escriba"los digitos son pares"
        si no
            Escriba"los digitos no son pares"
        fin si
    sino
            Escriba"El numero no es de dos digitos"
    fin si
Fin
'''