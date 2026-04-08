# -*- coding: utf-8 -*-
import sys


def programa4(RutaXML):

    with open(RutaXML, encoding="utf-8") as f:
        return f.read()
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa4(entrada)      # ejecutar 
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
