from nodo import nodo
import numpy as np
import xml.etree.cElementTree as ET


class listatransacciones1():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0

    def insertar_trans(self, id, idE, idP, idEs, listclien, idT):
        
        global empresa_trans
        empresa_trans= nodo(info=[id, idE, idP, idEs, listclien, idT])
        self.size +=1
        if self.primero is None:
            self.primero = empresa_trans
            self.ultimo= empresa_trans
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(empresa_trans)




    def mostrar_trans(self):
        tmp = self.primero
        while tmp is not None:
            print("--TRANSACCIONES--")
            print("ID: ", tmp.info[0])
            print("ID Empresa: ", tmp.info[1])
            print("ID Punto de Atención: ", tmp.info[2])
            cont_trans=0
            for i in tmp.info[3]:
                print("Escritorios activos: ", tmp.info[3][cont_trans][0])
                cont_trans+=1
            cont_Cliente =0
            for i in tmp.info[4]:
                print("DPI: ", tmp.info[4][cont_Cliente][0])
                print("Nombre del cliente: ", tmp.info[4][cont_Cliente][1])
                
                cont_id=0
                for i in tmp.info[5]:
                    if tmp.info[5][cont_id][0]!=tmp.info[4][cont_Cliente][0]:
                        cont_id+=1
                    else:
                        while tmp.info[5][cont_id][0]==tmp.info[4][cont_Cliente][0]: 
                            print("ID transacción: ", tmp.info[5][cont_id][1])
                            print("Cantidad: ", tmp.info[5][cont_id][2])
                            cont_id+=1
                            break
                cont_Cliente+=1
            tmp=tmp.getsiguiente()
            