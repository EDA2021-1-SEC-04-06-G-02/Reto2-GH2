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
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    return controller.loadData(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- (R1) Conocer los N videos con más views por categoría y país ")
    print("3- (R2) Video más viral por país")
    print("4- (R3) Video más viral por categoría")
    print("5- (R4) Conocer los N videos con más likes por tag")


# Para imprimir la info
def p_fv(e):
    print()

def p_rq1(ans):
    k=lt.size(ans)
    y=1

    while y<=k:
        e=lt.getElement(ans, y)

        print('Titulo: {0} || Canal: {1} || Fecha {2} || Tiempo de publicación {3} || Vistas {4} || Likes {5} || Dislikes {6} '
             .format(e['title'], e['channel_title'], e['trending_date'], e['publish_time'], e['views'], e['likes'], e['dislikes']))

        y+=1

def p_rq2(ans):
    print('Titulo: {0} || Canal: {1} || País{2} || Cantidad de días en tendencia {3}'
             .format(ans['title'], ans['channel_title'], ans['country'], ans['trending_days']))

def p_rq3(ans):
    print('Titulo: {0} || Canal: {1} || Número de categoría: {2} || Cantidad de días en tendencia: {3} '
             .format(ans['title'], ans['channel_title'], ans['category_id'], ans['trending_days']))

def p_rq4(ans):
    k=lt.size(ans)
    y=1
    
    while y<=k:
        e=lt.getElement(ans, y)

        print('Puesto: {0} || Titulo: {1} || Canal: {2} || Tiempo de publicación: {3} || Vistas: {4} || Likes: {5} || Dislikes: {6} || Tags: {7} '
             .format(y, e['title'], e['channel_title'], e['publish_time'], e['views'], e['likes'], e['dislikes'], e['tags']))

        y+=1



catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        loadData(catalog)

        print('Registros de videos cargados: ' + str(catalog['videos']))
        print('Registros de categorías cargados: ' + str(mp.size(catalog['categories'])))

    elif int(inputs[0]) == 2:
        cat=str(input('Escriba la categoría que le interesa: '))
        p=str(input('Escriba el país: '))
        n=int(input('Escriba cuantos videos quiere saber: '))

        ans=controller.reque1(catalog, cat, p, n)
        p_rq1(ans)

    elif int(inputs[0]) == 3:
        p=str(input('Escriba el país: '))

        ans=controller.reque2(catalog, p)
        p_rq2(ans)

    elif int(inputs[0]) == 4:
        cat=str(input('Escriba la categoría que le interesa: '))
        
        ans=controller.reque3(catalog, cat)
        p_rq3(ans)


    elif int(inputs[0]) == 5:
        tag=str(input('Escriba el tag: '))
        p=str(input('Escriba el país: '))
        n=int(input('Escriba cuantos videos quiere saber: '))

        ans=controller.reque4(catalog, tag, n, p)
        p_rq4(ans)

    else:
        sys.exit(0)
sys.exit(0)
