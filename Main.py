from tkinter import filedialog as fd
from xml.dom import minidom

from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET

cont =0
filename = fd.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Text files", ".xml"), ("Todos los archivos",".*")))
docxml = minidom.parse(filename)

Cliente = docxml.getElementsByTagName('empresa')
print(Cliente)
for i in Cliente:
    cont+=1
    ID = Cliente[cont-1].attributes['id'].value
    nombre = i.getElementsByTagName('nombre')[0]
    abreviacion = i.getElementsByTagName('abreviatura')[0]
    nombre1 = i.getElementsByTagName('nombre')[1]
    direccion = i.getElementsByTagName('direccion')[0]
    escritorio = i.getElementsByTagName('escritorio')[0]
    
    print(ID)
    print(f"nombre ={nombre.firstChild.data}")
    print(f"Abreviatura ={abreviacion.firstChild.data}")
    print(f"Nombre Punto ={nombre1.firstChild.data}")
    print(f"Dirección ={direccion.firstChild.data}")

    #Escritorio1 = docxml.getElementsByTagName('listaEscritorios')
    #for i in Escritorio1:
       # escritorio = i.getElementsByTagName('escritorio')[0]
        #print(f"Escritorio ={escritorio.firstChild.data}")


    puntoAtencion = docxml.getElementsByTagName('puntoAtencion')

    
    





