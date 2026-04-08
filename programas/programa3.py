# -*- coding: utf-8 -*-
import re
import sys

from programa1 import programa1
def programa3(RutaFactura):
    
    '''
    SU CÓDIGO
    
    
    '''
    text = programa1(RutaFactura)
    res=f""
    
    result = re.findall(
        r"(\d+)\s+(.*)\s+(\d+,\d{2})\s+(\d+,\d{2})",text
    )
    for i in result:
        res+= f"Cant: {i[0].strip()} |Desc: {i[1].strip()} | {i[2].strip()} c/u |Total:  {i[3].strip()}"
        res+= "\n"

    print(res)
    return res

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)    
 
    ret = programa3(entrada)      # ejecutar 
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
