# -*- coding: utf-8 -*-
import re
import sys
from programa2 import programa2
from programa4 import programa4
from programa5 import programa5

def programa6(RutaPdf,RutaXML):
    fecha , monto = programa2(RutaPdf)
    texto = programa4(RutaXML)
    if programa5(RutaPdf,RutaXML):
            patron = r'<BanTeng:Movimiento[^>]* \bImporte="' + monto + r'"[^>]* \bFecha="' + fecha + r'"[^>]* />'
            res = re.sub(patron, "", texto)
            res = re.sub(r'\n\s*\n', '\n    ', res)

            total_movimientos = re.search(r'<BanTeng:TotalMovimientos>(\d+)</BanTeng:TotalMovimientos>', texto)
            total_nuevo = int(total_movimientos.group(1)) - 1
            res = re.sub(r'<BanTeng:TotalMovimientos>(\d+)</BanTeng:TotalMovimientos>', f'<BanTeng:TotalMovimientos>{total_nuevo}</BanTeng:TotalMovimientos>', res)
            return res
    else:
        return texto

   
 

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
