import tkinter as tk
from tkinter import *    
from tkinter import ttk 
from tkinter.constants import TRUE
from serial import*
import threading

def main():
    
    global root
    global leftFrame
    global raiz
    raiz=Tk()
    raiz.geometry("500x240")
    raiz.title("Interfaz Grafica Control de Movimiento(IGCM)")
    
      
    Label(raiz,text="Automatica 2: Protocolo de comuniación",width="50",height="1",font=("Times New Roman",15),fg="Black",anchor="w").place(x=100,y=5)
    Label(raiz,text="Estudiante: Sonya Daniel Peña Niño",width="50",height="1",font=("Times New Roman",15),fg="Black",anchor="w").place(x=100,y=40)
    Label(raiz,text="Trama:",width="5",height="1",font=("Times New Roman",15),fg="Black",anchor="w").place(x=140,y=100)
    Label(raiz,text="Presion:",width="7",height="1",font=("Times New Roman",15),fg="Black",anchor="w").place(x=140,y=140)
    Label(raiz,text="CheckSum 1:",width="10",height="1",font=("Times New Roman",15),fg="Black",anchor="w").place(x=100,y=180)
    Label(raiz,text="CheckSum 2:",width="10",height="1",font=("Times New Roman",15),fg="Black",anchor="w").place(x=280,y=180)
    hil1.start()
    raiz.mainloop()


    
def checkSum(a):
    xor = 0
    i = 0
    while i < len(a):
        xor = xor ^ ord(a[i])
        i += 1
    return xor

def serialStar():
    while True:
        rawString = ser.readline().decode('utf-8')   
        datoTemperatura=rawString[1:5]
        checksumR=int(rawString[5:8])
        checksumP=int(checkSum(rawString[0:4]))

        
        Label(raiz,text=rawString ,width="8",height="2",font=("Times New Roman",12),fg="Black").place(x=200,y=100)
        Label(raiz,text=datoTemperatura,width="7",height="2",font=("Times New Roman",12),fg="Black").place(x=210,y=135)
        Label(raiz,text=checksumR,width="5",height="2",font=("Times New Roman",12),fg="Black").place(x=220,y=170)
        Label(raiz,text=checksumP,width="6",height="2",font=("Times New Roman",12),fg="Black").place(x=400,y=170)
        time.sleep(1)

hil1=threading.Thread(target=serialStar,daemon=True)
ser =Serial('COM3', 115200)
main() 

    


