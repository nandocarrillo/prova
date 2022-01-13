#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class MyError(Exception): 
    # Constructor or Initializer 
    def __init__(self, value, mensaje): 
# se cargan los valores enviados en el error al propio a MyError 
# para poderlo utilizar en la sección except
        self.value = value
        self.msg=mensaje


def obrirFitxer(argv):

    try:
        if len(sys.argv) == 2:   # compruebo el número de parámetros, sin contar argv[0] que es el nombre del script       
            f = open('/home/nando/programacio/fitxers/'+sys.argv[1], 'r')    
        else:
            raise(MyError(len(sys.argv),"Falta el nom de l'arxiu."))

    except MyError as error: 
        print("Número de parámetros: ",error.value, "\nMensaje: ", error.msg)
    
    
    except FileNotFoundError:
        print("El fitxer no existeix!!")

    else:    
        contenido = f.read()
        print ("El contingut del fitxer es:")
        print ("=======================")
        print (contenido)
        print ("=======================")
        print ("Longitud", len(contenido), "bytes.")
        f.close()

obrirFitxer(sys.argv)


