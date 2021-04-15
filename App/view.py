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
from DISClib.ADT import map as mp
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
def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    return controller.loadData(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- (R1) Conocer los N videos con más views en un país por categoría: ")
    print("3- (R2) Video más viral en un país")
    print("4- (R3) Video más viral por categoría")
    print("5- (R4) Conocer los N videos con más likes por tag")


# Para imprimir la info
def p_fv(e):
    print()

def p_rq1(ans,n):
    le=min(n, lt.size(ans))
    c=1

    while c<=le:
        e=lt.getElement(ans,c)

        print('Puesto: {0} || Trending_date: {1} || Titulo: {2} || Canal: {3} || Tiempo de pulicación: {4} || Vistas: {5} || Likes: {6} || Dislikes: {7}'
             .format(c, le['trending_date'], le['title'], le['channel_title'], le['publish_time'], le['views'], le['likes'], le['dislikes']))

        c+=1

def p_rq2(ans):
    print('Titulo: {0} || Canal: {1} || País: {2} || Cantidad de días en tendecia: {3} '
             .format(ans['title'], ans['chaneel_title'], ans['country'], ans['trending_days']))

def p_rq3(ans):
    print('Titulo: {0} || Canal: {1} || Número de categoría: {2} || Cantidad de días en tendencia: {3} '
             .format(ans['title'], ans['channel_title'], ans['category_id'], ans['trending_days']))

def p_rq4(ans,n):
    k=min(n, lt.size(ans))
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

        print('Registros de videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Registros de categorías cargados: ' + str(mp.size(catalog['categories'])))

    elif int(inputs[0]) == 2:
        categories=str(input('Escriba la categoría que le interesa: '))
        n=str(input('Escriba cuantos videos quiere conocer: '))
        p=str(input('Escriba el país del que desea conocer: '))

        ans=controller.reque1(catalog, categories, n, p)
        p_rq1(ans)
        

    elif int(inputs[0]) == 3:
        countri=str(input('Escriba el pais que le interesa:'))
        
        ans=controller.reque2(catalog, countri)
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
        p_rq4(ans,n)

    else:
        sys.exit(0)
sys.exit(0)
