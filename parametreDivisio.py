#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class MyError(Exception): 
    # Constructor or Initializer 
    def __init__(self, value, mensaje): 
# se cargan los valores enviados en el error al propio a MyError 
# para poderlo utilizar en la sección except
        self.value = value
        self.msg=mensaje


def division(argv):

    try:
        if len(sys.argv)-1 == 2:   # compruebo el número de parámetros, sin contar argv[0] que es el nombre del script                print("Has introducido 2 parámetros, es correcto!")
            dividendo = float(sys.argv[1])
            divisor = float(sys.argv[2])
            resultado = dividendo/divisor
            print("El resultado de la división es: ",resultado)
        else:
            raise(MyError(len(sys.argv)-1,"Número de parámetros incorrecto, han de ser 2."))
                   
    except MyError as error: 
        print("Número de parámetros: ",error.value, "\nMensaje: ", error.msg)
        
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    except ValueError: # los parámetros han sido convertidos a enteros, float(sys.argv[i]), por tanto la excepción ha de ser de tipo ValueError y no de TypeError
        print("Hay un elemento de la lista que no es un número")
        # paso al siguiente parámetro     
    print("Sigue la ejecución del código...")


division(sys.argv)
