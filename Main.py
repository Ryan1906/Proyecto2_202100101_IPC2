from calendar import c
from glob import glob
from telnetlib import SE
from tkinter import filedialog as fd
from xml.dom import minidom
import graphviz 
from lista import listaempresa
from listaTransacciones import listatransacciones1
listaempresa = listaempresa()
listatransacciones1 = listatransacciones1()
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET


def LimpiarSistema():
    print("Se Limpió Sistema")

    listaempresa.DELETE()

def actualizar():

    
    listaempresas =[]

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
            global listaIDEscritorio
            listaIDEscritorio = []
            for z in ListEscritorios.findall('escritorio'):

                IDEscritorio =z.attrib.get('id')
                IdentificacionEscritorio = z.find('identificacion').text
                EncargadoEscritorio = z.find('encargado').text
                ActividadEscritorio = False
                listaIDEscritorio.append(IDEscritorio)
                listaEscritorio.append([IDPuntaAtencion, IDEscritorio,IdentificacionEscritorio,EncargadoEscritorio, ActividadEscritorio, listaIDEscritorio])
        
        transacciones = x.find('listaTransacciones')
        listatransacciones=[]
        for a in transacciones.findall('transaccion'):

            Id_transaccion = a.attrib.get('id')
            Nombre_transaccion = a.find('nombre').text 
            Tiempo = a.find('tiempoAtencion').text
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

    
    listaempresas =[]

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
            global listaIDEscritorio
            listaIDEscritorio = []
            for z in ListEscritorios.findall('escritorio'):

                IDEscritorio =z.attrib.get('id')
                IdentificacionEscritorio = z.find('identificacion').text
                EncargadoEscritorio = z.find('encargado').text
                ActividadEscritorio = False
                listaIDEscritorio.append(IDEscritorio)
                listaEscritorio.append([IDPuntaAtencion, IDEscritorio,IdentificacionEscritorio,EncargadoEscritorio, ActividadEscritorio, listaIDEscritorio])
        
        transacciones = x.find('listaTransacciones')
        listatransacciones=[]
        for a in transacciones.findall('transaccion'):

            Id_transaccion = a.attrib.get('id')
            Nombre_transaccion = a.find('nombre').text 
            Tiempo = a.find('tiempoAtencion').text 
            listatransacciones.append([Id_transaccion,Nombre_transaccion,Tiempo])
            
            
        listaempresa.insertar_empresa(IDempresa,NombreEmpresa, AbreviaturaEmpresa, listaPuntosA,listaEscritorio,listatransacciones)
    listaempresa.mostrarempresa()

def graphviz1():

    cadenas =[]
    graphvizcadena = "digraph{"

    
    for k in datos.findall('configInicial'):
        global config_idE
        global config_idP
        config_id=(k.attrib.get('id'))
        config_idE=(k.attrib.get('idEmpresa'))
        config_idP=(k.attrib.get('idPunto'))
        escritorio_act=k.find('escritoriosActivos')
        global escritorio
        escritorio=[]
        transaccion=[]
        cantidad=[]
        contca =0
        for m in escritorio_act.findall('escritorio'):
            global escritorio_id
            
            escritorio_id=(m.attrib.get('idEscritorio'))
            
            escritorio.append([escritorio_id])
            cadenas.append('[label = "'+escritorio_id+ '"shape = rectangle sides = 6 color = orange style = filled peripheries = 2]')
            
            graphvizcadena +="BOXE"+str(contca)+cadenas[contca]+"\n"
            contca +=1
        cadenas1 =[]
        clientes_list=k.find('listadoClientes')
        listaclientes =[]
        contCliente = 0
        for n in clientes_list.findall('cliente'):
            cliente_dpi=(n.attrib.get('dpi'))
            cliente_nombre=(n.find('nombre').text)
            listaclientes.append([cliente_dpi,cliente_nombre])
            cadenas1.append('[label = "'+cliente_dpi+' '+ cliente_nombre +'"shape = rectangle sides = 6 color = orange style = filled peripheries = 2]')
            
            graphvizcadena +="BOXC"+str(contCliente)+cadenas1[contCliente]+"\n"
            contCliente+=1
            trans_list=n.find('listadoTransacciones')
            

            for l in trans_list.findall('transaccion'):
                trans_id=l.attrib.get('idTransaccion')
                trans_cantidad=l.attrib.get('cantidad')
                transaccion.append([cliente_dpi, trans_id,trans_cantidad])

    

       
        listatransacciones1.insertar_trans(config_id, config_idE, config_idP, escritorio, listaclientes, transaccion)
    listatransacciones1.mostrar_trans()



    
    graphvizcadena += "}" 
    miArchivo = open('Resultados.dot','w')
    miArchivo.write(graphvizcadena)
    miArchivo.close

    



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
    for i in range(int(NumTransacciones)):


        IdTransacciones = input("Ingrese lael id de la transaccion No." + str(ContTrans)+ ": ")
        listIDTrans.append(IdTransacciones)
        NomTransacciones = input("Ingrese el nombre de la Transaccion No." + str(ContTrans)+ ": ")
        listIDTrans.append(NomTransacciones)
        TempoTransacciones = input("Ingrese el tiempo de la Transaccion No." + str(ContTrans)+ ": ")
        listIDTrans.append(TempoTransacciones)
        cadena+=  "        <transaccion id='"+IdTransacciones+"'>\n"
        cadena+=  "            <nombre> "+ NomTransacciones+"</nombre>\n"
        cadena+=  "            <tiempoAtencion> "+ TempoTransacciones + "</tiempoAtencion>\n"
        cadena+=  "        </transaccion>\n"
    cadena+=  "    </listaTransacciones>\n"
    cadena+=  "</empresa>\n"
    print(cadena)
    EmpresaNueva = ET.fromstring(cadena)
    
    root.append(EmpresaNueva)
    docxml.write(filename)
    
    actualizar()

def CrearClientes():
    print("Se va a crear Clientes")


    #Pedimos los datos del nuevo cliente, tanto su nombre, como el dpi
    DPICCliente = input("Ingrese el dpi del nuevo cliente")
    NombreCCliente = input("Ingrese el nombre del cliente")
    numTrans = input("Cuantas Transacciones desea agregar?")

    #------------------------------------------------------------------------------------
    DatsoClienteN ="<cliente dpi='"+str(DPICCliente)+"'>\n"
    DatsoClienteN += "<nombre>"+str(NombreCCliente)+"</nombre>\n"
    DatsoClienteN += " <listadoTransacciones>\n"
    for i in range(int(numTrans)):
        IDNtranssacion = input("Cuál es el ID de la Transaccion?")
        CantNTransaccion = input("Qué cantidad de transaccione desea")
        DatsoClienteN += '<transaccion idTransaccion="'+ str(IDNtranssacion)+'" cantidad ="'+str(CantNTransaccion)+'"/>\n'


    DatsoClienteN += " </listadoTransacciones>"
    DatsoClienteN += "</cliente>"
    #------------------------------------------------------------------------------------
    #Miramos la configuración donde sea integrar al cliente

    ChooseConfig = input("Que simulación desea seleccionar?(ID)")



    #Lo metemos dentro el listado de Clientes
    for i in datos.findall('.//configInicial[@id="'+ChooseConfig+'"]'): #Aqui se puede filtrar por ID './/empresa[@id="'+i+'"]'
        clientes_list=i.find('listadoClientes')
        print(clientes_list)
        print(DatsoClienteN)
        ClienteNueva = ET.fromstring(DatsoClienteN)
        print(ClienteNueva)
        clientes_list.append(ClienteNueva)
        datos.write(filename2)
    
    actualizar2()

   


def actualizar2():

    
    for k in datos.findall('configInicial'):
        global config_idE
        global config_idP
        config_id=(k.attrib.get('id'))
        config_idE=(k.attrib.get('idEmpresa'))
        config_idP=(k.attrib.get('idPunto'))
        escritorio_act=k.find('escritoriosActivos')
        global escritorio
        escritorio=[]
        transaccion=[]
        cantidad=[]
        for m in escritorio_act.findall('escritorio'):
            global escritorio_id
            
            escritorio_id=(m.attrib.get('idEscritorio'))
            
            escritorio.append([escritorio_id])

        clientes_list=k.find('listadoClientes')
        listaclientes =[]
        for n in clientes_list.findall('cliente'):
            cliente_dpi=(n.attrib.get('dpi'))
            cliente_nombre=(n.find('nombre').text)
            listaclientes.append([cliente_dpi,cliente_nombre])
            trans_list=n.find('listadoTransacciones')
            

            for l in trans_list.findall('transaccion'):
                trans_id=l.attrib.get('idTransaccion')
                trans_cantidad=l.attrib.get('cantidad')
                transaccion.append([cliente_dpi, trans_id,trans_cantidad])
                

        
        listatransacciones1.insertar_trans(config_id, config_idE, config_idP, escritorio, listaclientes, transaccion)
    listatransacciones1.mostrar_trans()



def ArchTrans():
    global filename2
    filename2 = fd.askopenfilename(initialdir="C:/", title="abrir", filetypes=(("XML files",".XML"),("Todos los archivos",".*")))
    global datos
    datos = ET.parse(filename2)
    global root2
    root2 = datos.getroot()


    
    for k in datos.findall('configInicial'):

        global config_idE
        global config_idP
        global escritorio

        config_id=(k.attrib.get('id'))
        config_idE=(k.attrib.get('idEmpresa'))
        config_idP=(k.attrib.get('idPunto'))

        escritorio1=k.find('escritoriosActivos')
        
        escritorio=[]
        transaccion=[]
        

        for l in escritorio1.findall('escritorio'):
            global escritorio_id
            
            escritorio_id=(l.attrib.get('idEscritorio'))
            
            escritorio.append([escritorio_id])

        clienteslistado=k.find('listadoClientes')
        listaclientes =[]

        for j in clienteslistado.findall('cliente'):
            cliente_dpi=(j.attrib.get('dpi'))
            cliente_nombre=(j.find('nombre').text)
            listaclientes.append([cliente_dpi,cliente_nombre])
            trans_list=j.find('listadoTransacciones')
            

            for k in trans_list.findall('transaccion'):
                trans_id=k.attrib.get('idTransaccion')
                trans_cantidad=k.attrib.get('cantidad')
                transaccion.append([cliente_dpi, trans_id,trans_cantidad])
                

        listatransacciones1.insertar_trans(config_id, config_idE, config_idP, escritorio, listaclientes, transaccion)
    listatransacciones1.mostrar_trans()

def PuntosAtencionArray():
    datos = ET.parse(filename2)
      
    for k in datos.findall('configInicial'):
        trans_id=(k.attrib.get('id'))
    
        trans_idE=(k.attrib.get('idEmpresa'))
        
        trans_idP=(k.attrib.get('idPunto'))
        escritorio_act=k.find('escritoriosActivos')
        
        escritorio=[]
        transaccion=[]
        cantidad=[]
        clientes=[]
        for m in escritorio_act.findall('escritorio'):
            
            escritorio_id=(m.attrib.get('idEscritorio'))
            escritorio.append([escritorio_id])
        clientes_list=k.find('listadoClientes')
        for n in clientes_list.findall('cliente'):
            cliente_dpi=(n.attrib.get('dpi'))
            cliente_nombre=(n.find('nombre').text)
            clientes.append([cliente_dpi, cliente_nombre])
            trans_list=n.find('listadoTransacciones')
            for l in trans_list.findall('transaccion'):
                trans_id=l.attrib.get('idTransaccion')
                trans_cantidad=l.attrib.get('cantidad')
                transaccion.append([cliente_dpi, trans_id, trans_cantidad])

        for i in escritorio:
            listaempresa.activarescritorios(trans_idE,trans_idP,*i)                    
        listaempresa.Select(trans_idE,trans_idP)


print("Bienvenido a nuestra Aplicación")
print("---------------------------------")
print("Para poder iniciarlo, debe seleccionar una de estas opciones:")
print("(1) Limpiar sistemas")
print("(2) Cargar archivo")
print("(3) Crear nueva Empresa")
print("(4) Cargar archivo con configuracion inicial para la prueba")
print("(5) Activar Escritorios")
print("(6) Crear Clientes")
print("(7) Generar Graphviz")

Seleccion = input("¿Qué desea hacer?")

while Seleccion =="1" or Seleccion =="2" or Seleccion =="3" or Seleccion =="4" or Seleccion =="5"or Seleccion =="6" or Seleccion =="7":

    if Seleccion == "1":
        LimpiarSistema()
    
    elif Seleccion =="2":
        CargarArchivo()
    
    elif Seleccion =="3":
        CrearNuevaE()
    
    elif Seleccion =="4":
        ArchTrans()
    
    elif Seleccion =="5":
        PuntosAtencionArray()
    
    elif Seleccion =="6":
        CrearClientes()
    
    elif Seleccion =="7":
        graphviz1()
    


        
    


    print("Bienvenido a nuestra Aplicación")
    print("---------------------------------")
    print("Para poder iniciarlo, debe seleccionar una de estas opciones:")
    print("(1) Limpiar sistemas")
    print("(2) Cargar archivo")
    print("(3) Crear nueva Empresa")
    print("(4) Cargar archivo con configuracion inicial para la prueba")
    print("(5) Activar Escritorios")
    print("(6) Crear Clientes")
    print("(7) Generar Graphviz")

    Seleccion= input("Qué desea Hacer?")

















