from ast import While
from nodo import nodo

import xml.etree.cElementTree as ET


class listaempresa():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        

    def eliminardatos(self):

        self.primero=None
        self.ultimo= None
        self.size = 0
        


    def insertar_empresa(self, IDEmpresa, nombreE, abreviaturaE, listaPuntos, listaescritorio, listaTrans):
        global DatosEmpresa
        DatosEmpresa= nodo(info=[IDEmpresa, nombreE, abreviaturaE, listaPuntos, listaescritorio, listaTrans])
        
        if self.primero is None:
            self.primero = DatosEmpresa
            self.ultimo= DatosEmpresa
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(DatosEmpresa)
        
        self.size += 1
    
    
    def Select(self,IDEmpre, punto):
            
            tmp = self.primero
            numeracion_puntoa2=0
            while tmp is not None:
                if IDEmpre != tmp.info[0]:
                    tmp=tmp.getsiguiente()
                else:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                    print("-- EMPRESA SELECCIONADA --")
                    print("ID: ", tmp.info[0])
                    print("Nombre: ", tmp.info[1])
                    print("Abreviación: ", tmp.info[2])
                    print("--PUNTOS DE ATENCIÓN--")
                    numeracion_puntoa=0
                    while punto != tmp.info[3][numeracion_puntoa2][0]: #tmp.info[3] son los puntos de atención
                        numeracion_puntoa2+=1
                    else:
                        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                        print("-- PUNTO DE ATENCIÓN SELECCIONADO --")
                        print("ID: ", tmp.info[3][numeracion_puntoa2][0])
                        print("Nombre: ", tmp.info[3][numeracion_puntoa2][1])
                        print("Direccion: ", tmp.info[3][numeracion_puntoa2][2])
                        print("-- ESCRITORIOS --")
                        numeracion_esc=0
                        for i in tmp.info[4]:
                            if tmp.info[4][numeracion_esc][0]!=tmp.info[3][numeracion_puntoa2][0]:
                                numeracion_esc+=1
                            else:
                                #Comparo el id conectado de los escritorios con los id del punto de atención
                                while tmp.info[4][numeracion_esc][0]==tmp.info[3][numeracion_puntoa2][0]: #tmp.info[4] son los escritorios
                                    print("ID: ", tmp.info[4][numeracion_esc][1])
                                    print("Código: ", tmp.info[4][numeracion_esc][2])
                                    print("Nombre: ", tmp.info[4][numeracion_esc][3])
                                    if tmp.info[4][numeracion_esc][4]==True:
                                        print("Estado de escritorio:  ACTIVO")
                                    else:
                                        print("Estado de escritorio:  INACTIVO")
                                    numeracion_esc+=1
                                    break
                    break
    def mostrarempresa(self):
        tmp = self.primero
        conteo=0
        while tmp is not None:
            conteo=conteo+1
            print("ID: ", tmp.info[0])
            print("Nombre: ", tmp.info[1])
            print("Abreviación: ", tmp.info[2])
            numeracion_puntoa=0
            print("--PUNTOS DE ATENCIÓN--")
            for i in tmp.info[3]:
                print("ID: ", tmp.info[3][numeracion_puntoa][0])
                print("Nombre: ", tmp.info[3][numeracion_puntoa][1])
                print("Direccion: ", tmp.info[3][numeracion_puntoa][2])
                
                print("--ESCRITORIO--")
                numesc=0
                for i in tmp.info[4]:
                    if tmp.info[4][numesc][0]!=tmp.info[3][numeracion_puntoa][0]:
                        numesc+=1
                    else:
                        while tmp.info[4][numesc][0]==tmp.info[3][numeracion_puntoa][0]:
                            print("ID: ", tmp.info[4][numesc][1])
                            print("Código: ", tmp.info[4][numesc][2])
                            print("Código: ", tmp.info[4][numesc][3])
                            numesc+=1
                            break

                numeracion_puntoa +=1
            numeracion_trans=0
            for j in tmp.info[5]:
                print("--TRANSACCIONES--")
                print("ID: ", tmp.info[5][numeracion_trans][0])
                print("Nombre: ", tmp.info[5][numeracion_trans][1])
                print("Tiempo de Atención: ", tmp.info[5][numeracion_trans][2])
                numeracion_trans+=1
                
            print("---------------------------------")
            tmp=tmp.getsiguiente()
    
    def activarescritorios(self,IDEmpre,punto, escritorios):
        tmp = self.primero
        numeracion_puntoa2=0
        while tmp is not None:
            if IDEmpre != tmp.info[0]:
                tmp=tmp.getsiguiente()
            else:
                while punto != tmp.info[3][numeracion_puntoa2][0]: #tmp.info[3] son los puntos de atención
                    numeracion_puntoa2+=1
                else:
                    numeracion_esc=0
                    for i in tmp.info[4]:
                        if tmp.info[4][numeracion_esc][0]!=tmp.info[3][numeracion_puntoa2][0]:
                            numeracion_esc+=1
                        else:
                            #Comparo el id conectado de los escritorios con los id del punto de atención
                            while tmp.info[4][numeracion_esc][0]==tmp.info[3][numeracion_puntoa2][0]: #tmp.info[4] son los escritorios
                                while tmp.info[4][numeracion_esc][1]==escritorios:
                                    tmp.info[4][numeracion_esc][4]=True
                                    break
                                numeracion_esc+=1
                                break
                                
                break
