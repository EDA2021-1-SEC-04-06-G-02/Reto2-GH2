"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog()->dict:
    catalog= {
        'videos': None,
        'tags'  : None,
        'ids'   : None, }
    
    catalog['videos']=lt.newList('LINKED_LIST')
    catalog['ids']={}
    catalog['categories']=mp.newMap(maptype='PROBING', loadfactor=0.5)

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    cv=catalog['videos']
    vid=esacosa(video)
    lt.addLast(cv, vid)
    insert(catalog['categories'], vid['category_id'], vid['title'])

def addId(catalog, row)->None:
    row=row[0].split('\t')
    i=row[0]
    n=row[1]
    n=n.lower().strip()
    ci=catalog['ids']
    
    ci[i]=n

# Funciones para creacion de datos
def esacosa(video):
     data=('title','channel_title','country','publish_time','trending_date','category_id','views','likes','dislikes', 'tags')
     sub={}

     for i in data:
         value=video[i]
         sub[i]=value

     return sub

def insert(cc, i, n):
    if mp.contains(cc, i)==False:
        a=lt.newList()
        lt.addLast(a,n)
        mp.put(cc,i, a)
    
    else: 
        a=mp.get(cc,i)
        a=a['value']
        lt.addLast(a,n)
        mp.put(cc,i,a)


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
