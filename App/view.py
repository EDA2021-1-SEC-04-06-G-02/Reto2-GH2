"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import time
import tracemalloc
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def initCatalog(kind, lf):
    return controller.initCatalog(kind, lf)

def loadData(catalog):
    return controller.loadData(catalog)

def usage_memory(md):
    am=0
    for st in md:
        am= am + st.size_diff    
    
    am=am/1024.0
    return am

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        kind= input('Seleccione el tipo de mapa: ')
        lf= float(input('Seleccione el factor de carga: '))

        t1=time.perf_counter()
        tracemalloc.start()
        m1=tracemalloc.take_snapshot()

        catalog=initCatalog(kind, lf)
        loadData(catalog)
        
        m2=tracemalloc.take_snapshot()
        tracemalloc.stop()
        t2=time.perf_counter()
        tt=(t2-t1)*1000
        md=m2.compare_to(m1,'filename')
        mm=usage_memory(md)
 
        print('Tiempo[ms]: {0} || Memoria[kb]: {1}'.format(tt, mm))
        print('Registros de videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Primer video: ' + str(lt.firstElement(catalog['videos'])))
        print('Categorias: ' + str(catalog['ids']))


    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
