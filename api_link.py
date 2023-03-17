#Importacion de librerias para trabajar la API y el vinculo con la base de datos
import pandas as pd
from sodapy import Socrata

def crear_lista_departamentos():                        #Esta funcion es esencial para comprobar que el usuario ingrese el nombre de un departamento presente en la base de datos
    
    client = Socrata("www.datos.gov.co", None)          #Estas \
    results = client.get("gt2j-8ykr")                   #  3    >   Son la conexion con la API y la conversion de la base de datos a un dataframe de Pandas para emplear las funciones de esta libreria de forma sencilla
    results_df = pd.DataFrame.from_records(results)     #Lineas/
                                                        
    nombre_lista = list(results_df["departamento_nom"]) #Se hace uso de la funcion list() utilizando como parametro todos los elementos pertenecientes a la columna departamento_nom dentro de la base de datos
                                                        #para realizar la comprobacion en la funcion consulta_nombre del archivo de UI
    
    return nombre_lista                                 #Envia la lista


def api (nombre_departamento, limite_registros):                                                        #La funcion que envia el dataframe a mostrar en pantalla con el formato deseado
    
    client = Socrata("www.datos.gov.co", None)                                                          #Las      \ 
    results = client.get("gt2j-8ykr", departamento_nom = nombre_departamento, limit = limite_registros) #Mismas 3  > Lo que cambia respecto a la conexion presente en la funcion anterior son los parametros que definen el 
    results_df = pd.DataFrame.from_records(results)                                                     #Lineas   /  departamento que se desea buscar y la cantidad de registros
    
    results_df.rename(columns={"departamento_nom": "Departamento"}, inplace=True)                       #\
    results_df.rename(columns={"ciudad_municipio_nom": "Municipio"}, inplace=True)                      # \
    results_df.rename(columns={"edad": "Edad"}, inplace=True)                                           #  \ Se renombran las columnas a mostrar por fines meramente esteticos y para 
    results_df.rename(columns={"fuente_tipo_contagio": "Tipo de contagio"}, inplace=True)               #  / darle mas legibilidad al programa
    results_df.rename(columns={"estado": "Estado"}, inplace=True)                                       # /
    results_df.rename(columns={"tipo_recuperacion": "Tipo de recuperacion"}, inplace=True)              #/
    results_df.rename(columns={"pais_viajo_1_nom": "Pais"}, inplace=True)

    if 'pais_viajo_1_nom' not in results_df:                                                            #\
        results_df ['Pais'] = "NaN"                                                                     # \ La columna "pais_viajo_1_nom", al encontrarse "vacia" en algunos (bastantes) campos, puede dar problemas a la hora de imprimirse, 
    else:                                                                                               # / por ende, estas lineas permiten llenar esos "Vacios" para evitar errores en la ejecucion e impresion del programa 
        results_df.rename(columns={"'pais_viajo_1_nom'": "Pais"}, inplace=True)                         #/

    results_df = results_df[["Departamento", "Municipio", "Edad", "Tipo de contagio", "Estado", "Tipo de recuperacion", "Pais"]] # Se le da el formato al dataframe para que muestre las columnas que se requieren
    
    print(results_df.to_string(index = False)) #Imprime en la consola el dataframe


