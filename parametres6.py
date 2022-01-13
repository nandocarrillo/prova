#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class MyError(Exception): 
    # Constructor or Initializer 
    def __init__(self, value, mensaje): 
# se cargan los valores enviados en el error al propio a MyError 
# para poderlo utilizar en la sección except
        self.value = value
        self.msg=mensaje

def histograma(argv):

    try:
        if len(sys.argv)-1 > 0:   # si hay más de un parámetro sigo con el programa,       
                                  # no cuento el parámetro 0 que es el nombre del script 
            for i in range(1,len(sys.argv)):
                print("*" * int(sys.argv[i]))            
        
        else:
            raise(MyError(len(sys.argv)-1,"No has introducido parámetros."))

    except MyError as error: 
        print("Número de parámetros: ",error.value, "\nMensaje: ", error.msg)

    
    except ValueError: # los parámetros han sido convertidos a enteros, int(sys.argv[i]), por tanto la excepción ha de ser ValueError
        print("Hay un elemento de la lista que no es un número")
             
    

        

histograma(sys.argv)
