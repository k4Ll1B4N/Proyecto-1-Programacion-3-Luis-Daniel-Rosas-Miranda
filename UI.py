from tkinter import * # Se importa el módulo 'tkinter' para crear interfaces gráficas de usuario
import tkinter as tk # Se importa el módulo 'tkinter' bajo el alias 'tk'
from api_link import * #Del archivo de conexion con la API se importan todas las funciones necesarias para trabajar el apartado de consola

departamentos = crear_lista_departamentos() #Se asigna una lista de los departamentos disponibles dentro de la base de datos a una variable para realizar
                                            #la comprobacion del nombre ingresado por usuario en la funcion consulta_nombre

#--Funcion para consultar si el nombre ingresado existe----------------------------------------------------------------------------------------------------                                           
def consulta_nombre(texto):
    if (texto not in departamentos):
        print("Error, el nombre que busca no se encuentra en la base de datos, asegurese de buscar el nombre sin caracteres especiales y/o tildes.")
        return True
        exit()
    else: 
        return False

#--Funcion que comprueba que el limite ingresado se encuentre en el rango definido por el programa---------------------------------------------------------
def comprobacion_limite(numero):
    if ((numero <= 0) or (numero > 1000)):
        print("Error, el numero de registros que quiere buscar no es valido, asegurese de elegir un numero entre 1 y 1000.")
        return True
        exit()
    else: return False  

#--Funcion que actua como interfaz grafica para el usuario-------------------------------------------------------------------------------------------------
def ejecutable():

    print("BIENVENIDO AL PROGRAMA DE CONSULTA DE CASOS DE COVID 19 EN COLOMBIA")

    nombre = input("Ingrese el nombre del departamento el cualquiera buscar: ").upper()
    limite = input("Ingrese la cantidad de registros que quiera consultar (Por precaucion, el programa tiene un limite maximo de 1000 registros. Recomendamos buscar una cantidad inferior a la mencionada.): ")
    limite = int(limite)

    if ((consulta_nombre(nombre)== False)and(comprobacion_limite(limite)==False)):
        str(limite)
        api(nombre, limite)

