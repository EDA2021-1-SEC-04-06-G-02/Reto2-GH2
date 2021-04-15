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
from DISClib.Algorithms.Sorting import mergesort as ms
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
        'categories':None, 
        'ids'   : None, }
    
    catalog['videos']=lt.newList('SINGLE_LINKED')
    catalog['ids']=mp.newMap(maptype='PROBING', loadfactor=0.5)
    catalog['categories']=mp.newMap(maptype='CHAINING', loadfactor=4.0)

    catalog['tags']=mp.newMap(maptype='CHAINING', loadfactor=4.0)

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    cv=catalog['videos']
    vid=esacosa(video)
    lt.addFirst(cv, vid)
    insertCat(catalog['categories'], vid['category_id'], vid)
    insertTag(catalog['tags'], vid['tags'], vid)

def addId(catalog, row)->None:
    row=row[0].split('\t')
    i=row[0]
    n=row[1]
    n=n.lower().strip()
    ci=catalog['ids']
    
    if mp.contains(ci, n)==False:
        mp.put(ci,n,i)
    

# Funciones para creacion de datos
def esacosa(video):
     data=('title','channel_title','country','publish_time','trending_date','category_id','views','likes','dislikes', 'tags')
     sub={}

     for i in data:
         value=video[i]
         sub[i]=value

     return sub

def insertCat(cc, i, e):
    if mp.contains(cc, i)==False:
        a=lt.newList('ARRAY_LIST')
        lt.addFirst(a,e)
        mp.put(cc,i, a)
    
    else: 
        a=mp.get(cc,i)
        a=me.getValue(a)
        lt.addFirst(a,e)
        mp.put(cc,i,a)

def insertTag(ct, t, e):
    tags=t.split('|')

    for tag in tags:
        mt=tag.lower().strip()
        if mp.contains(ct, mt)==False:
            a=lt.newList('ARRAY_LIST')
            lt.addFirst(a,e)
            mp.put(ct,mt, a)
    
        else: 
            a=mp.get(ct,mt)
            a=me.getValue(a)
            lt.addFirst(a,e)
            mp.put(ct,mt,a)



# Funciones de consulta

def reque1(catalog, cat, n, p):
    main=catalog['categories']
    cat=cat.lower().strip()
    id=Nit(catalog, cat)
    mini=mp.get(main,cat)

    main=me.getvalue(mini)
    mini=Cut_C(main, p)
    main=ms.sort(mini, cmpVideosByViews)
    le=min(n, lt.size(main))
    ans=lt.sublist(main, 1, le)
    return ans

def reque2(catalog, countri):
    main=catalog['country']
    countri=countri.lower().strip()

    mini=mp.get(main, id)
    main=me.getValue(mini)
    ans=Ct_alg(main)
    dans=ms.sort(ans, cmpVideosByTrend)

    ans=lt.firstElement(dans)
    return ans



def reque3(catalog, cat):
    main=catalog['categories']
    cat=cat.lower().strip()
    id=Nit(catalog, cat)
    
    mini=mp.get(main, id)
    main=me.getValue(mini)
    ans=Ct_alg(main)
    dans=ms.sort(ans, cmpVideosByTrend)

    ans=lt.firstElement(dans)
    return ans

def reque4(catalog, tag, n, p):
    main=catalog['tags']
    t=tag.lower().strip()
    mini=mp.get(main, t)

    main=me.getValue(mini)
    mini=Cut_C(main , p)
    main=ms.sort(mini, cmpVideosByLikes)
    k=min(n, lt.size(main))
    ans=lt.subList(main, 1 , k)

    return ans



# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2)->bool:
    return (float(video1['views']) > float(video2['views']))

def cmpVideosByTrend(video1, video2)->bool:
    return (float(video1['trending_days']) > float(video2['trending_days']))

def cmpVideosByLikes(video1, video2)->bool:
    return (float(video1['likes']) > float(video2['likes']))

# Funciones de ordenamiento
def Nit(catalog, cat):
    main=catalog['ids']
    mini=mp.get(main, cat)
    ans=me.getValue(mini)

    return ans

def Ct_alg(main):
    y=1
    titles=lt.newList('ARRAY_LIST')
    lt.addFirst(titles, '1')
    ans=lt.newList('ARRAY_LIST')

    while y<=lt.size(main):
        e=lt.getElement(main, y)
        t=e['title']
        se=dict(title=e['title'], channel_title=e['channel_title'], category_id=e['category_id'], trending_days=1)

        if lt.isPresent(titles, t)==0:
            lt.addFirst(titles, t)
            lt.addFirst(ans, se)
        
        elif lt.isPresent(titles, t)>0:
            k=get_tp(ans, t)
            se=lt.getElement(ans, k)
            se['trending_days']+=1
            lt.changeInfo(ans, k, se)
        
        y+=1
    return ans


def get_tp(main, t):
    y=1

    while y<=lt.size(main):
        e=lt.getElement(main, y)
        ct=e['title']

        if t==ct:
            k=y

        y+=1
    return k

def Cut_C(main, p):
    y=1
    ans=lt.newList('ARRAY_LIST')

    while y<=lt.size(main):
        e=lt.getElement(main, y)
        c=e['country']

        if c.strip().lower() == p.strip().lower():
            lt.addFirst(ans, e)

        y+=1
    return ans
