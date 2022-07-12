""" import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()

 """

from hashlib import new
import pandas as pd
import xlsxwriter


"""
|Sum all the hours of the Pilot and pass it to "horas"
"""
def calculo_horas(df):
    horas=0
    for i in df:
        horas=horas+i
    return horas
"""
|Find in a colum if the pilot name is found, ans if it does, 
|it take the values of hours to sum those

"""
def horas_alumno(columna, alumno, df):
    
    horas= df[df[columna].str.lower()==alumno]['Horas']
    horas=calculo_horas(horas)
    
    return horas

"""
|Load a EXCEL file using the path file, and search for information from
|a given Pilot name.
"""    
def archivo(path_file,nombre_alumno):
    #take each value and it is modify to be able to interpret
    nombre_alumno=nombre_alumno.strip()
    nombre_alumno=nombre_alumno.lower()
    
    hoja= "Entrenamientos" #Sheet name
    col_types ={'Instructor':str,'Piloto':str, "Co-piloto":str,"Horas":float}
    #Open a excel file, and search in the sheet name "hoja"
    try:
        df=pd.read_excel(path_file, sheet_name=hoja, dtype=col_types)
    except FileNotFoundError:
        print("File could not be found")

    #create a dict to storage each hour
    horas={'Instructor':0,'Piloto':0,'Co-Piloto':0,'Observador':0,'Total':0}
    #Save each hour of the Pilot in a dict    
    horas['Instructor']= round(horas_alumno('Instructor',nombre_alumno,df),2)
    horas['Piloto']=     round(horas_alumno('Piloto',nombre_alumno,df),2)
    horas['Co-Piloto']=  round(horas_alumno('Co-Piloto',nombre_alumno,df),2)
    horas['Observador']= round(horas_alumno('Observador',nombre_alumno,df),2)
    horas['Total']=horas['Instructor']+horas['Piloto']+horas['Co-Piloto']+horas['Observador'] #Suma el total de las horas voladas por el piloto
    
    return horas


"""
|Create a report with the Hours flying for each Pilot
"""    
def crear_informe(pilotos, nombre_alumno):
    
    #Crea un nuevo archivo de excel llamdo Reporte
    reporte= "Reporte.xlsx"
    writer =pd.ExcelWriter(reporte, engine="xlsxwriter")
    col=0
    #Iter for each object o Pilot
    for i in nombre_alumno:
        
        #Retrived the name of the Pilot 'i' and the hours 'pilotos[i]'
        info={ 
            i:pd.Series(pilotos[i], index=['Instructor','Piloto','Co-Piloto','Observador','Total'])
        
        }
        #Save the information in a dataframe
        info=pd.DataFrame(info)
        #Write in the excel file in the sheename='Horas', and moves 3 colums to the right to write the next information
        info.to_excel(writer, sheet_name='Horas', startcol=col)
        col=col+3
    writer.save()


    
    


def main(nombre_alumno,excel_archivo):
    
    path_file=excel_archivo #File name and Path
    pilotos={}
    for i, value in enumerate(nombre_alumno):
        
        horas=archivo(path_file, value)
        pilotos[value]=horas
    
    crear_informe(pilotos, nombre_alumno)
    return pilotos
    
  
       

