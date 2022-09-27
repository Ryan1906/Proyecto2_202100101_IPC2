from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
from nodo import Paciente 
from Lista import listasimple
import numpy as np
from nodo import DoublyLinkedList
from nodo import listadetableros


    
print("Predicción de Enfermedades")
lista = listasimple()
a=input("¿Desea abrir un Archivo? SI/NO")
if a == "SI":
    filename = fd.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Text files", ".xml"), ("Todos los archivos",".*")))
    docxml = minidom.parse(filename)
    paciente = docxml.getElementsByTagName('paciente')
    for i in paciente:
        nombre = i.getElementsByTagName('nombre')
        edad = i.getElementsByTagName('edad')
        periodo = i.getElementsByTagName('periodos')
        m = i.getElementsByTagName('m')
        rejilla = i.getElementsByTagName('rejilla')
        celda = i.getElementsByTagName('celda') 

        dimensiones = int(m[0].firstChild.data) 
        a = np.zeros((dimensiones, dimensiones))
        for j in rejilla:
            n=0
            for k in celda:
                a[(int(celda[n].attributes['f'].value)-1)][(int(celda[n].attributes['c'].value)-1)]=1
                n+=1
            coord = np.zeros((n, 2))
            p=0
            for l in celda:            
                coord[p][0]=(int(celda[p].attributes['f'].value))
                coord[p][1]=(int(celda[p].attributes['c'].value))
                p+=1

            enfermas=0    
         
           

        lista.insertlast( nombre[0].firstChild.data, edad[0].firstChild.data, periodo[0].firstChild.data, m[0].firstChild.data, coord, a )
    

print("PACIENTE:")
    
 
print("Ingrese Nombre de Paciente: ")
name=input()


paciente1=lista.getpacientes(nombre=name)
a3=lista.gettabla0(nombre=name)
dll = DoublyLinkedList()
rows=len(a3)
cols=len(a3)
dll.insertData(a3, rows, cols)
dll.dibujargrafica(name, "Período Inicial")
nodotablero = listadetableros()
nodotablero.tablero=dll
paciente1.settableros(nodotablero)
nodotab2=paciente1.tableros
for i in range(int(paciente1.periodos)):
    dll2=DoublyLinkedList()
    dll2.insertData(nodotab2.tablero.siguientediag(), rows, cols)
    tablero2=listadetableros()
    tablero2.tablero=dll2
    dll2.dibujargrafica(name,str(i+1))
    nodotab2.siguiente=tablero2
    nodotab2=None
    nodotab2=tablero2

nodotab2=None
nodotab2=paciente1.tableros
nodotab3=paciente1.tableros
encontrado=False
global estadopaciente
estadopaciente=""
repeticion=0
for i in range(int(paciente1.periodos)):
    if encontrado:break
    for j in range(int(paciente1.periodos)):
        if ((nodotab2.tablero.siguientediag())==(nodotab3.tablero.siguientediag())) and (i!=j):
            print("Se ha encontrado el patrón en: ", j )
            repeticion=0
            repeticion=abs(i-j)
            print("El patrón se repite cada: ", repeticion)
            curado=[True for z in nodotab2.tablero.siguientediag() if 1 in z]
            if not curado:
                print("El paciente se ha curado")
                estadopaciente="curado"
                repeticion=0
            elif repeticion==1:
                print("El paciente tiene una enfermedad mortal Q.E.P.D")
                estadopaciente="muerto"
                
            else:
                print("El paciente tiene una enfermedad grave")
                estadopaciente="grave"
                # repeticion=0
            encontrado=True
            break
        
        nodotab3=nodotab3.siguiente
    nodotab2=nodotab2.siguiente
    nodotab3=paciente1.tableros
    print("estado: ",estadopaciente)


root= ET.Element("?xml version=1.0 encoding=UTF-8?")
doc = ET.SubElement(root, "doc")
nodo1=ET.SubElement(doc, "pacientes\n")

nodo2 = ET.SubElement(doc, "paciente\n" )

nodo3 = ET.SubElement(doc, "datos personales\n")
nodo4 = ET.SubElement(doc, "nombre\n")
nodo4.text=name
nodo5 = ET.SubElement(doc, "edad\n")
nodo5.text=edad[0].firstChild.data
nodo6 = ET.SubElement(doc, "periodos\n")
nodo6.text=str(periodo[0].firstChild.data)
nodo7 = ET.SubElement(doc, "m\n")
nodo7.text=str(m[0].firstChild.data)
nodo8 = ET.SubElement(doc, "resultado\n")
nodo8.text=estadopaciente
nodo9 = ET.SubElement(doc, "n\n")
nodo9.text=str(repeticion)
arbol = ET.ElementTree(root)
tree = ET.ElementTree(root)
with open ("pacientes.xml", "wb") as files :
    tree.write(files)
            
lista.getpacientes(nombre=name)