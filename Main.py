from calendar import c
from telnetlib import SE
from tkinter import filedialog as fd
from xml.dom import minidom

from lista import listaempresa
from listaTransacciones import listatransacciones1
listaempresa = listaempresa()
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET


















def LimpiarSistema():
    print("Se Limpió Sistema")

    listaempresa.eliminardatos()

def actualizar():
 
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
        
        transacciones = x.find('listaTransacciones') #lista de transacciones
        listatransacciones=[]
        for a in transacciones.findall('transaccion'):

            Id_transaccion = a.attrib.get('id') #id transaccion
            Nombre_transaccion = a.find('nombre').text #nombre transaccion
            Tiempo = a.find('tiempoAtencion').text #tiempo transaccion
            listatransacciones.append([Id_transaccion,Nombre_transaccion,Tiempo])
        
            
            
        listaempresa.insertar_empresa(IDempresa,NombreEmpresa, AbreviaturaEmpresa, listaPuntosA,listaEscritorio,listatransacciones)
    listaempresa.mostrarempresa()   

def CargarArchivo():

    global filename
    global docxml
    global root
    global listaempresas
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
        
        transacciones = x.find('listaTransacciones') #lista de transacciones
        listatransacciones=[]
        for a in transacciones.findall('transaccion'):

            Id_transaccion = a.attrib.get('id') #id transaccion
            Nombre_transaccion = a.find('nombre').text #nombre transaccion
            Tiempo = a.find('tiempoAtencion').text #tiempo transaccion
            listatransacciones.append([Id_transaccion,Nombre_transaccion,Tiempo])
            
            
        listaempresa.insertar_empresa(IDempresa,NombreEmpresa, AbreviaturaEmpresa, listaPuntosA,listaEscritorio,listatransacciones)
    listaempresa.mostrarempresa()


def CrearNuevaE():
    print("Creando Nueva Empresa")


    IdNuevaEmpresa = input("Escriba el ID DE su nueva empresa: ")
    NombreNuevaEmpresa = input("Escriba el nombre de la Nueva Empresa: ")
    AbreviaturaNuevaEmpresa = input("Escriba la nueva Abreviatura: ")
    NumePuntosAtencion = input("¿Cuantos Puntos de Atención tiene su empresa")
    


    cadena=("\n")
    cadena += " <empresa id='"+IdNuevaEmpresa+"'>\n"
    cadena+=    "   <nombre> "+NombreNuevaEmpresa+" </nombre>\n"
    
    cadena+= "    <abreviatura>"+ AbreviaturaNuevaEmpresa +"</abreviatura>\n"
    cadena+=    "<listaPuntosAtencion>\n"
    cont =1
    listIdPA =[]
    listNomPA =[]
    listIdEsc=[]
    listDirPA = []
    listIdentEsc =[]
    listEnEsc = []


    for i in range(int(NumePuntosAtencion)):
        
        IdPuntoAtencion = input("Ingrese el Id del Punto de Atención "+str(cont)+ ":  ")
        listIdPA.append(IdPuntoAtencion)
        NomPuntoAtencion = input("Ingrese el nombre del Punto de Atención "+str(cont)+ ":  ")
        listNomPA.append(NomPuntoAtencion)
        DirPuntoAtencion = input("Ingrese la dirección del Punto de Atención "+str(cont)+ ":  ")
        listDirPA.append(DirPuntoAtencion)
        cadena+=  "        <puntoAtencion id='"+listIdPA[cont-1]+"'>\n"
        cadena+=  "            <nombre>" +listNomPA[cont-1] +"</nombre>\n"
        cadena+=  "            <direccion>" +listDirPA[cont-1] +"</direccion>\n"
        cadena+=  "            <listaEscritorios>\n"
        NumeEscritorios = input("Cuantos Escritorios desea en este Punto de Atención?")
        contEsc = 1
        for i in range(int(NumeEscritorios)):
            
            IdEscritorio = input("Ingrese el ID del escritorio No." + str(contEsc)+ ": ")
            listIdEsc.append(IdEscritorio)
            IdentEscritorio = input("Ingrese la identificacion del escritorio No." + str(contEsc)+ ": ")
            listIdentEsc.append(IdentEscritorio)
            EncarEscritorio = input("Ingrese elencargado  del escritorio No." + str(contEsc)+ ": ")
            listEnEsc.append(EncarEscritorio)
            cadena+=  "               <escritorio id='"+listIdEsc[contEsc-1]+"'>\n"
            cadena+=  "                <identificacion> "+listIdentEsc[contEsc-1]+"</identificacion>\n"
            cadena+=  "                <encargado> "+listEnEsc[contEsc-1]+" </encargado>\n"
            cadena+=  "                </escritorio>\n"
            contEsc+=1
         
        cadena+=  "           </listaEscritorios>\n"
        cadena+=  "        </puntoAtencion>\n"
        cont+=1
    
    cadena+=  "    </listaPuntosAtencion>\n"
    cadena+=  "    <listaTransacciones>\n"
    NumTransacciones = input("Cuantas Transacciones desea agregar?")

    ContTrans =1
    listIDTrans =[]
    listNomTransaccion = []
    listTiempoTrans =[]
    for i in range(str(NumTransacciones)):


        IdTransacciones = input("Ingrese lael id de la transaccion No." + str(ContTrans)+ ": ")
        listIDTrans.append(IdTransacciones)
        NomTransacciones = input("Ingrese el nombre de la Transaccion No." + str(ContTrans)+ ": ")
        listIDTrans.append(NomTransacciones)
        TempoTransacciones = input("Ingrese el tiempo de la Transaccion No." + str(ContTrans)+ ": ")
        listIDTrans.append(TempoTransacciones)
        cadena+=  "        <transaccion id='250'>\n"
        cadena+=  "            <nombre> Pago De chiquistrikis </nombre>\n"
        cadena+=  "            <tiempoAtencion> 10 </tiempoAtencion>\n"
        cadena+=  "        </transaccion>\n"
    cadena+=  "    </listaTransacciones>\n"
    cadena+=  "</empresa>\n"
    print(cadena)
    EmpresaNueva = ET.fromstring(cadena)
    
    root.append(EmpresaNueva)
    docxml.write(filename)
    
    actualizar()


def insertTransacciones():
    #Abrir archivos (XML y todos los archivos)
    archivo = fd.askopenfilename(initialdir="C:/", title="abrir", filetypes=(("XML files",".XML"),("Todos los archivos",".*")))
    datos = ET.parse(archivo)
    
    for k in datos.findall('configInicial'):
        config_id=(k.attrib.get('id'))
        config_idE=(k.attrib.get('idEmpresa'))
        config_idP=(k.attrib.get('idPunto'))
        escritorio_act=k.find('escritoriosActivos')
        escritorio=[]
        transaccion=[]
        cantidad=[]
        for m in escritorio_act.findall('escritorio'):
            escritorio_id=(m.attrib.get('idEscritorio'))
            escritorio.append([escritorio_id])
        clientes_list=k.find('listadoClientes')
        for n in clientes_list.findall('cliente'):
            cliente_dpi=(n.attrib.get('dpi'))
            cliente_nombre=(n.find('nombre').text)
            trans_list=n.find('listadoTransacciones')
            for l in trans_list.findall('transaccion'):
                trans_id=l.attrib.get('idTransaccion')
                trans_cantidad=l.attrib.get('cantidad')
                transaccion.append([trans_id])
                cantidad.append([trans_cantidad])

        #Agregar datos al nodo a través de la lista
        listatransacciones1.insertar_trans(config_id, config_idE, config_idP, escritorio, cliente_dpi, cliente_nombre, transaccion, cantidad)




print("Bienvenido a nuestra Aplicación")
print("---------------------------------")
print("Para poder iniciarlo, debe seleccionar una de estas opciones:")
print("(1) Limpiar sistemas")
print("(2) Cargar archivo")
print("(3) Crear nueva Empresa")
print("(4) Cargar archivo con configuracion inicial para la prueba")
print("(5) Salir")

Seleccion = input("¿Qué desea hacer?")

while Seleccion =="1" or Seleccion =="2" or Seleccion =="3" or Seleccion =="4" or Seleccion =="5":

    if Seleccion == "1":
        LimpiarSistema()
    
    elif Seleccion =="2":
        CargarArchivo()
    
    elif Seleccion =="3":
        CrearNuevaE()
    
    


    print("Bienvenido a nuestra Aplicación")
    print("---------------------------------")
    print("Para poder iniciarlo, debe seleccionar una de estas opciones:")
    print("(1) Limpiar sistemas")
    print("(2) Cargar archivo")
    print("(3) Crear nueva Empresa")
    print("(4) Cargar archivo con configuracion inicial para la prueba")
    print("(5) Salir")
    Seleccion= input("Qué desea Hacer?")























    
        # for y in transacciones.findall('transaccion'):

        #     IDTransaccion = y.attrib.get('id')
        #     NombreTransaccion = y.find('nombre').text
        #     TiempoAtencion =y.find('tiempoAtencion').text
        #     listaTransacciones.append([IDTransaccion,NombreTransaccion,TiempoAtencion])
       










