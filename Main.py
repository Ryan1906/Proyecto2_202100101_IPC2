from tkinter import filedialog as fd
from xml.dom import minidom

from lista import listaempresa
listaempresa = listaempresa()
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET

cont =0
filename = fd.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Text files", ".xml"), ("Todos los archivos",".*")))
docxml = ET.parse(filename)
root = docxml.getroot()


listaIDCliente=[]
listaempresas =[]

listaTransacciones =[]

for x in root.findall('empresa'): #Aqui se puede filtrar por ID './/empresa[@id="'+i+'"]'
     
    IDempresa = x.attrib.get('id')
    NombreEmpresa = x.find('nombre').text
    AbreviaturaEmpresa = x.find('abreviatura').text
    listaempresas.append([IDempresa,NombreEmpresa,AbreviaturaEmpresa])
        

    PuntosAtencion = x.find('listaPuntosAtencion')
    listaPuntosA = []
    listaEscritorio =[]

    for y in PuntosAtencion.findall('puntoAtencion'):
           
        IDPuntaAtencion = y.attrib.get('id')
        NombrePuntoAtencion =y.find('nombre').text
        DireccionPuntoAtencion =y.find('direccion').text
        listaPuntosA.append([IDPuntaAtencion,NombrePuntoAtencion,DireccionPuntoAtencion])

        ListEscritorios =  y.find('listaEscritorios')

        for z in ListEscritorios.findall('escritorio'):

            IDEscritorio =z.attrib.get('id')
            IdentificacionEscritorio = z.find('identificacion').text
            EncargadoEscritorio = z.find('encargado').text
            listaEscritorio.append([IDPuntaAtencion, IDEscritorio,IdentificacionEscritorio,EncargadoEscritorio])
            #transacciones = x.find('listaTransacciones')
    
        
        
    listaempresa.insertar_empresa(IDempresa,NombreEmpresa, AbreviaturaEmpresa, listaPuntosA,listaEscritorio)
listaempresa.mostrarempresa()


    
        # for y in transacciones.findall('transaccion'):

        #     IDTransaccion = y.attrib.get('id')
        #     NombreTransaccion = y.find('nombre').text
        #     TiempoAtencion =y.find('tiempoAtencion').text
        #     listaTransacciones.append([IDTransaccion,NombreTransaccion,TiempoAtencion])
       










