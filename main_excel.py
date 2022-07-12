import tkinter
from tkinter import *
import horas_alumnos_excel as excel
from tkinter import filedialog
import pandas



#Comprueba que los valores no sean numeros, ni tanpoco este vacio
def obtener_datos(Nombre, Apellido):
    
    if len(Nombre)<1 or Nombre.isdigit():
    
        text_accion=' Por favor entre un Nombre valido'
        good_value=False
    elif len(Apellido)<1 or Apellido.isdigit():
        text_accion=' Por favor entre un Apellido valido'
        good_value=False

    else:    
        text_accion=f' Agregado el Piloto {Nombre} {Apellido}                         '  
        good_value=True
    if good_value:
        alumno.append(Apellido.strip()+" "+Nombre.strip())
        print(alumno)    

    return text_accion, good_value


#Agrega mas Pilotos a la lista
def guardar_alumnos_boton():

    
    text_accion, good_value=obtener_datos(Nombre.get(),Apellido.get())
    
    
    #Si es un valor valido
    
      
    mylabel=Label(root, text= text_accion)
    mylabel.grid(row=9,column=1, columnspan=3)
    
#Busca informacion sobre los Pilotos
def buscar_info():
    pilotos={}
     
    pilotos=excel.main(alumno,filename)
    #Mensaje de resultados
    mylabel=Label(root, text= 'Horas Voladas por Pilotos:                 ')
    mylabel.grid(row=10,column=0)
    
    for i, value in enumerate(alumno):
        #Made message
        
        text_accion1=f'Piloto {value}: como instructor {pilotos[value]["Instructor"]}'
        text_accion2=f'                como Piloto {pilotos[value]["Piloto"]}'
        text_accion3=f'                como Co-Piloto {pilotos[value]["Co-Piloto"]}'
        text_accion4=f'                como Observador {pilotos[value]["Observador"]}'
        text_accion5=f'                Total {pilotos[value]["Total"]}'                   
        #Position of message

        mylabel1=Label(root, text= text_accion1)
        mylabel1.grid(row=(11+i),column=(0))
        mylabel2=Label(root, text= text_accion2)
        mylabel2.grid(row=(11+i),column=(1))
        mylabel3=Label(root, text= text_accion3)
        mylabel3.grid(row=(11+i),column=(2))
        mylabel4=Label(root, text= text_accion4)
        mylabel4.grid(row=(11+i),column=(3))
        mylabel5=Label(root, text= text_accion5)
        mylabel5.grid(row=(11+i),column=(4))
        

   
    
if __name__=='__main__':
    alumno=[]
    #Busca el archivo excel
    filename=filedialog.askopenfilename(initialdir="",title="Select a file",filetypes=(("Excel files","*.xlsx"),("all files","*.*")))
    root= Tk()
    
    #Labels
    titulo= Label(root, text="Hola, yo creo un informe con las horas entrenadas de varios Pilotos en excel, solo escribe su nombre y apellido, pulsa agregar")
    titulo.grid(row=0, column=0,columnspan=6)
    titulo2= Label(root, text="  a cuantos pilotos necesites y por terminar pulsa crear informe, este creara un informe en un archivo excel llamado 'Reporte' ")
    titulo2.grid(row=1, column=0,columnspan=6)
    titulo2= Label(root, text=" Nombre: ")
    titulo2.grid(row=2, column=0)
    titulo2= Label(root, text=" Apellido: ")
    titulo2.grid(row=5, column=0)
    #variables input
    Nombre=Entry(root, width=50, bg="White", fg="Black", borderwidth=5) 
    Nombre.grid(row=4, column=1, padx=10,pady=12)
    Apellido=Entry(root, width=50, bg="White", fg="Black", borderwidth=5) 
    Apellido.grid(row=6, column=1, padx=10,pady=12)
    #Add the buttons
    boton_crear_reporte=Button(root, text="Crear Reporte"  , padx=10,pady=12, command=buscar_info, fg="Black", bg="White")
    boton_agregar=Button(root, text="Agregar", padx=10,pady=12, command=guardar_alumnos_boton, fg="Black", bg="White")
    

    #Place the buttons in the aplication
    boton_crear_reporte.grid(row=7, column=1 )
    boton_agregar.grid(row=7, column=0)
    
    
    root.mainloop()



    
    
    

    
