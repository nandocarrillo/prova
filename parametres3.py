#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def division(dividendo, divisor, argv):
    if len(sys.argv)-1 == 2:   # compruebo el número de parámetros, sin contar argv[0] que es el nombre del script
        print("Has introducido 2 parámetros, es correcto!")
       
        try:
            dividendo = float(sys.argv[1])
            divisor = float(sys.argv[2])
            resultado = division(dividendo, divisor)
            print("El resultado de la división es: ",resultado)
        except ZeroDivisionError:
            print("El divisor no puede ser 0")
        except ValueError: # los parámetros han sido convertidos a enteros, float(sys.argv[i]), por tanto la excepción ha de ser de tipo ValueError y no de TypeError
                    print("Hay un elemento de la lista que no es un número")
                    # paso al siguiente parámetro     
            
        print("Sigue la ejecución del código...")
    
    else:
        print("Número de parámetros incorrecto, han de ser 2...")


