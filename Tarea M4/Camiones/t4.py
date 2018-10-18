# -*- coding: utf-8 -*-
from math import *
from matplotlib import pyplot
from numpy import *

def ciudades_csv():
    file_ciudades = open("ciudades.csv", "r")
    for a in file_ciudades:
        linea = a.strip('"').split(",")
        latitudes[linea[0]] = (float(linea[1].strip('"')),float(linea[2].strip().strip('"')))
    file_ciudades.close()

def adyacencia_csv():
    file_adyacencia = open("adyacencia.csv", "r")
    for a in file_adyacencia:
        linea = a.strip("\n").split(",")
        lista_adyacencia = []
        if linea[0] != "CIUDADES":
            for b in range(len(linea)-1):
                lista_adyacencia.append(int(linea[b+1]))
        adyacencia[linea[0]] = tuple(lista_adyacencia)
    file_adyacencia.close()

def rutas_txt():
    file_rutas = open("rutas.txt", "r")
    viajes_totales = 0
    litros_totales = []
    kilometros_totales = []
    for a in file_rutas:
        viajes_totales += 1
        ruta = []
        suma_distancia = 0
        pyplot.clf()
        ruta.extend(a.strip("\n").split(","))
        for b in range(len(ruta)-1):
            ciudad_1 = ruta[b]
            ciudad_2 = ruta[b+1]
            if plot_points(ciudad_1, ciudad_2) == False:
                break
            else:
                suma_distancia += distancia(latitudes[ciudad_1], latitudes[ciudad_2])
        pyplot.axis([-74,-68,-44,-18])
        pyplot.show()
        kilometros_totales.append(suma_distancia)
        litros_totales.append(int(suma_distancia/100*26.5))
        print(suma_distancia, "Km's recorridos")
        print(int(suma_distancia/100*26.5), "Lt's consumidos")
    print()
    histogramas(litros_totales, kilometros_totales, viajes_totales)
    file_rutas.close()

def plot_points(ciudad_1, ciudad_2):
    flag = False
    y1 = latitudes[ciudad_1][0]
    x1 = latitudes[ciudad_1][1]
    pyplot.text(x1, y1-1, ciudad_1, {})
    for c in range(18):
        if adyacencia[ciudad_1][c] == 1 and adyacencia[ciudad_2][c] == 1:
            flag = True
            break
    if flag == True:
        y1 = latitudes[ciudad_1][0]
        x1 = latitudes[ciudad_1][1]
        y2 = latitudes[ciudad_2][0]
        x2 = latitudes[ciudad_2][1]
        pyplot.arrow(x1,\
                     y1,\
                     x2-x1,\
                     y2-y1,\
                     head_width=0.2,\
                     head_length=0.2)
        pyplot.text(x2, y2-1, ciudad_2, {})
    elif flag == False:
        y1 = latitudes[ciudad_1][0]
        x1 = latitudes[ciudad_1][1]
        y2 = latitudes[ciudad_2][0]
        x2 = latitudes[ciudad_2][1]
        pyplot.arrow(x1,\
                     y1,\
                     0,\
                     0,\
                     head_width=0.2,\
                     head_length=0.2)
        pyplot.arrow(x2,\
                     y2,\
                     0,\
                     0,\
                     head_width=0.5,\
                     head_length=0.6)
        pyplot.text(x2, y2-1, ciudad_2, {})
        return False

def distancia(ciudad_1, ciudad_2):
    R = 6371.0
    lon1, lat1 = map(radians, ciudad_1)
    lon2, lat2 = map(radians, ciudad_2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2.0 * atan2(sqrt(a), sqrt(1.0 - a))
    return int(R * c)

def histogramas(litros_totales, kilometros_totales, viajes_totales):
    print("Litros totales")
    pyplot.clf()
    pyplot.hist(litros_totales)
    pyplot.show()
    print("Kilometros totales")
    pyplot.clf()
    pyplot.hist(kilometros_totales)
    pyplot.show()

latitudes = {}
adyacencia = {}

ciudades_csv()
adyacencia_csv()
rutas_txt()
