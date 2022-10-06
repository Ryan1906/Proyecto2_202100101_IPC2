from ast import While
from nodo import nodo

import xml.etree.cElementTree as ET


class listaempresa():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        

    def DELETE(self):

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
    
    
    def Select(self,IDEmpre, puntoAtencion):
            
            tmp = self.primero
            CONTPA2=0
            while tmp is not None:
                if IDEmpre != tmp.info[0]:
                    tmp=tmp.getsiguiente()
                else:
                    
                    print( "***********************************************")
                    print("                  MOSTRANDO EMPRESA             ")
                    print("ID: ", tmp.info[0])
                    print("Nombre: ", tmp.info[1])
                    print("Abreviación: ", tmp.info[2])
                    print( "***********************************************")
                    print("                    PUNTOS DE ATENCIÓN           ")
                    numeracion_puntoa=0
                    while puntoAtencion != tmp.info[3][CONTPA2][0]: #tmp.info[3] son los puntos de atención
                        CONTPA2+=1
                    else:
                        print( "***********************************************")
                        print("             MOSTRANDO PUNTOS DE ATENCIÓN        ")
                        print("ID: ", tmp.info[3][CONTPA2][0])
                        print("Nombre: ", tmp.info[3][CONTPA2][1])
                        print("Direccion: ", tmp.info[3][CONTPA2][2])
                        print( "***********************************************")
                        print("                  ESCRITORIOS ")

                        CONTESCRITORIO=0

                        for i in tmp.info[4]:
                            if tmp.info[4][CONTESCRITORIO][0]!=tmp.info[3][CONTPA2][0]:
                                CONTESCRITORIO+=1
                            else:
                                #Comparo el id conectado de los escritorios con los id del punto de atención
                                while tmp.info[4][CONTESCRITORIO][0]==tmp.info[3][CONTPA2][0]: #tmp.info[4] son los escritorios
                                    print("ID: ", tmp.info[4][CONTESCRITORIO][1])
                                    print("Código: ", tmp.info[4][CONTESCRITORIO][2])
                                    print("Nombre: ", tmp.info[4][CONTESCRITORIO][3])
                                    if tmp.info[4][CONTESCRITORIO][4]==True:
                                        print("ESTADO:  ACTIVO")
                                    else:
                                        print("ESTADO:  INACTIVO")
                                    CONTESCRITORIO+=1
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
            CONTPA=0
            print( "***********************************************")
            print("             PUNTOS DE ATENCIÓN                  ")
            for i in tmp.info[3]:
                print("ID: ", tmp.info[3][CONTPA][0])
                print("Nombre: ", tmp.info[3][CONTPA][1])
                print("Direccion: ", tmp.info[3][CONTPA][2])
                print( "***********************************************")
                print("                  ESCRITORIOS ")
                numesc=0
                for i in tmp.info[4]:
                    if tmp.info[4][numesc][0]!=tmp.info[3][CONTPA][0]:
                        numesc+=1
                    else:
                        while tmp.info[4][numesc][0]==tmp.info[3][CONTPA][0]:
                            print("ID: ", tmp.info[4][numesc][1])
                            print("Código: ", tmp.info[4][numesc][2])
                            print("Código: ", tmp.info[4][numesc][3])
                            numesc+=1
                            break

                CONTPA +=1
            CONTTRANS=0
            for j in tmp.info[5]:
                print( "***********************************************")
                print("                 TRANSACCIONES")
                print("ID: ", tmp.info[5][CONTTRANS][0])
                print("Nombre: ", tmp.info[5][CONTTRANS][1])
                print("Tiempo de Atención: ", tmp.info[5][CONTTRANS][2])
                CONTTRANS+=1
                
            print( "***********************************************")
            tmp=tmp.getsiguiente()
    
    def activarescritorios(self,IDEmpre,PUNTOA, escritorios):
        tmp = self.primero
        CONTPA2=0
        while tmp is not None:
            if IDEmpre != tmp.info[0]:
                tmp=tmp.getsiguiente()
            else:
                while PUNTOA != tmp.info[3][CONTPA2][0]: 
                    CONTPA2+=1
                else:
                    CONTESCRITORIO=0
                    for i in tmp.info[4]:
                        if tmp.info[4][CONTESCRITORIO][0]!=tmp.info[3][CONTPA2][0]:
                            CONTESCRITORIO+=1
                        else:
                           
                            while tmp.info[4][CONTESCRITORIO][0]==tmp.info[3][CONTPA2][0]:
                                while tmp.info[4][CONTESCRITORIO][1]==escritorios:
                                    tmp.info[4][CONTESCRITORIO][4]=True
                                    break
                                CONTESCRITORIO+=1
                                break
                                
                break
