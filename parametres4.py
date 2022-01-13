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
        except ValueError: # los parámetros han sido convertidos a enteros, int(sys.argv[i]), por tanto la excepción ha de ser de tipo ValueError y no de TypeError
            print("Hay un elemento de la lista que no es un número")
            i += 1  # fuerzo la salida 
        else:
            print("La suma de la lista es: ",total) 

suma_lista(sys.argv)
