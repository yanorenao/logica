#leer un numero entero de dos digitos y decir si los digitos son primos
'''
varibles
entero numero, digito1, digito2
Inicio 
    Escriba"digite un numero entero: "
    Lea numero
    si numero >= 10 and numero <= 99 entonces
        digito1 = numero / 10
        digito2 = numero modulo 10
        si digito1 = 2 or digito1 = 3 or digito1 = 5 or digito1 = 7 
           and
           digito2 = 2 or digito2 = 3 or digito2 = 5 or digito2 = 7 
            Escriba"los digitos son primos"
        si no
            Escriba"uno de los digitos o ninguno de los digitos son primos"
        fin si
Fin
'''