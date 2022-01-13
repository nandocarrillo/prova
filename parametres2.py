#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def suma_lista(argv): # paso como argumento la lista de parámetros
    total = 0
    i = 1   # inicializo a 1 para no coger el primer elemento de la lista que es el parámetro cero, osea el nombre del script
    while i <= len(sys.argv)-1:
        try:

            total += int(sys.argv[i]) # convierto el elemento de la lista a entero
            i +=1  # incremento el contador
        except ValueError:
            print("Hay un elemento de la lista que no es un número")
	    i +=1
        else:
            print("La suma de la lista es: ",total)    

if len(sys.argv)-1 == 2:   # compruebo el número de parámetros, sin contar argv[0] que es el nombre del script
        print("Has introducido 2 parámetros, es correcto!")
        suma_lista(sys.argv)    # llamo a la funcion que suma los parámetros
else:
        print("Número de parámetros incorrecto, han de ser 2...") 
