# -*- coding: utf-8 -*-
import re
import sys

from programa1 import programa1


def programa2(RutaFactura):
    
    '''
    SU CÓDIGO
    
    NOTA: El formato de la fecha debe ser AAAA-MM-DD 
    '''

    texto = programa1(RutaFactura)

    m_fecha = re.search(
        r"(\d{2})[-/](\d{2})[-/](\d{4})", texto
    )
    
    m_monto = re.search(r"BANCARIO\s+(\d+,\d{2})", texto)
    day = m_fecha.group(1)
    mes = m_fecha.group(2)
    anio = m_fecha.group(3)

    fecha =f"{anio}-{mes}-{day}"
    monto = m_monto.group(1)

    return fecha, monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
