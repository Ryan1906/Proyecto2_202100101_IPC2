from nodo import nodo

import xml.etree.cElementTree as ET


class listaempresa():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        




    def insertar_empresa(self, IDEmpresa, nombreE, abreviaturaE, listaPuntos, listaescritorio):
        global DatosEmpresa
        DatosEmpresa= nodo(info=[IDEmpresa, nombreE, abreviaturaE, listaPuntos, listaescritorio])
        self.size += 1
        if self.primero is None:
            self.primero = DatosEmpresa
            self.ultimo= DatosEmpresa
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(DatosEmpresa)
    

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
            print("---------------------------------")
            tmp=tmp.getsiguiente()