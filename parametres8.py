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

def suma_lista(argv):        

    i = 0
    while i != len(sys.argv): 
        try:
            if len(sys.argv) > 1:    # Si hay parámetros aparte del nombre del archivo continua con el programa
                total = int(sys.argv[1])         #   guardo el primer parámetro numérico
            
                for i in range(2,len(sys.argv),2): # recorro únicamente los operadores de la lista,
            # En función del operador realiza una u otra operación con el siguiente elemento.
            # Si encuentra un operador no válido, emite una excepción propia (raise) y pasa al 
            # siguiente operador, el número que sigue al operador no válido, no se tiene en cuenta
            # puesto que no sabe que operación ha de realizar con él.
                
                    if sys.argv[i] == '+':         
                        total += int(sys.argv[i+1])
                    elif sys.argv[i] == '-':
                        total -= int(sys.argv[i+1])
                    elif sys.argv[i] == '*':
                        total *= int(sys.argv[i+1])
                    elif sys.argv[i] == '/':
                        total /= int(sys.argv[i+1])
                    else:
                        raise(MyError(sys.argv[i],"El operador no es válido"))  
                # fuerzo la salida del while cuando ha recorrido todo el buble for
                i = len(sys.argv)          
            else:
                raise(MyError(len(sys.argv)-1,"No hay parámetros..."))    

        except ValueError:
            print("Hay un elemento de la lista que no es un número")
        except MyError as error: 
            print('Operador no valido: ',error.value, '\nMensaje: ', error.msg)  
        else:                
            print("El total de la lista es: ",total)
    

suma_lista(sys.argv)    # Llamo a la función para que sume la lista de parámetros

