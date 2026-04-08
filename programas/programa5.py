# -*- coding: utf-8 -*-
import re
import sys

from programa2 import programa2
from programa4 import programa4
def programa5(RutaPdf,RutaXML):
    fecha , monto = programa2(RutaPdf) 
    texto = programa4(RutaXML)
    patron = r'<BanTeng:Movimiento[^>]* \bImporte="' + monto + r'"[^>]* \bFecha="' + fecha + r'"[^>]* />'
    res = re.search(patron, texto)
    return res is not None
 
    
    

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa5(entrada_pdf,entrada_xml)      # ejecutar 
    if (ret):
        ret = "Encontrado"
    else:
        ret = "No encontrado"
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
