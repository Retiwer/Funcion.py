import Libreria  #Importar la libreria creada

"""
La Tabla de Excel fue copiada en una hoja diferente de la que originalmente se
presento, aun dentro del mismo documento, debido a que existian problemas de 
formatoen la hoja de excel, externos a los configurados o soportados por la
funcion de lectura.
los datos en la nueva hoja no fueron alterados en ningun otro aspecto mas que
la ubicacion y el orden de las columnas.  la informacion numerica se mantiene
identica a la original.
"""


################	   Excel	     ################
wb = openpyxl.load_workbook('/Test/Base.xlsx')  #Abrir el archivo Excel
sheet = wb.get_sheet_by_name('Hoja1')           #Identificar la hoja de Datos
#####################################################

Procesamiento(2, 4985, 5, 24, 4)  #Llamar la funcion principal con los
                                  #parametros correctos
