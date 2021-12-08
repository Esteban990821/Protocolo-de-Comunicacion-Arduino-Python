import tkinter as tk
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk 
from tkinter.constants import TRUE
from serial import*
import threading

def main_codigo():
    
    global root
    global leftFrame
    global rightFrameSerial
    root=Tk()
    root.geometry("500x300")
    root.title("Protocolo de Comunicación Automatica II")
    leftFrame=tk.Frame(root)
    leftFrame.config(width="220",height="300",bg="#111b54")
    leftFrame .place(x=0, y=0)
    rightFrameSerial = tk.Frame(root)
    rightFrameSerial.config(width="280", height="300",)
    rightFrameSerial.place(x=220, y=0)
    button = tk.Button(leftFrame ,width="20", height="2", text="Comunicación Serial", bg="#111b54", fg="white",command=go)
    button.place(x=25, y=10) 
    lbl2=Label(rightFrameSerial,text="Trama:",width="5",height="1",font=("Times New Roman",15),fg="Black",anchor="w")
    lbl2.place(x=20,y=20)
    lbl4=Label(rightFrameSerial,text="Estado:",width="5",height="1",font=("Times New Roman",15),fg="Black",anchor="w")
    lbl4.place(x=20,y=60)
    lbl5=Label(rightFrameSerial,text="Mensaje:",width="7",height="1",font=("Times New Roman",15),fg="Black",anchor="w")
    lbl5.place(x=20,y=100)
    lbl5=Label(rightFrameSerial,text="Sensor:",width="7",height="1",font=("Times New Roman",15),fg="Black",anchor="w")
    lbl5.place(x=20,y=140)
    lbl6=Label(rightFrameSerial,text="CheckSum R:",width="10",height="1",font=("Times New Roman",15),fg="Black",anchor="w")
    lbl6.place(x=20,y=180)
    lbl7=Label(rightFrameSerial,text="CheckSum:",width="8",height="1",font=("Times New Roman",15),fg="Black",anchor="w")
    lbl7.place(x=20,y=220)
    root.mainloop()
def go():
    hil1.start()
def checkSum(a):
    xor = 0
    for i in a:
        xor ^= ord(i)
    return xor

def serialRe():
    while True:
        trama= ser.readline().decode('utf-8')
        Inicio=trama[0]
        mensaje=trama[0:5]
        datoTemperatura=trama[1:5]
        checksumR=int(trama[5:8])
        checksumP=int(checkSum(trama[0:4]))

        print()
        lbl3=Label(rightFrameSerial,text=trama,width="10",height="2",font=("Times New Roman",12),fg="Black")
        lbl3.place(x=140,y=30)
        if Inicio=='K':
            lbl7=Label(rightFrameSerial,text="Leyendo Sensor ",width="15",height="1",font=("Times New Roman",10),fg="BLUE")
            lbl7.place(x=140,y=58)
            lbl8=Label(rightFrameSerial,text="de Temperatura",width="14",height="1",font=("Times New Roman",10),fg="BLUE")
            lbl8.place(x=140,y=75)

        lbl1=Label(rightFrameSerial,text=mensaje,width="10",height="2",font=("Times New Roman",12),fg="Black")
        lbl1.place(x=140,y=95)
        lbl9=Label(rightFrameSerial,text=datoTemperatura,width="10",height="2",font=("Times New Roman",12),fg="Black")
        lbl9.place(x=140,y=135)
        lbl10=Label(rightFrameSerial,text=checksumR,width="10",height="2",font=("Times New Roman",12),fg="Blue")
        lbl10.place(x=140,y=175)
        lbl12=Label(rightFrameSerial,text=checksumP,width="10",height="2",font=("Times New Roman",12),fg="Blue")
        lbl12.place(x=140,y=210)
        if checksumP==checksumR:
            lbl11=Label(rightFrameSerial,text="La información enviada es igual a la recibida",width="40",height="2",font=("Times New Roman",10),fg="Blue")
            lbl11.place(x=10,y=250)
        else:
            lbl11=Label(rightFrameSerial,text="La información enviada es diferente",width="40",height="2",font=("Times New Roman",10),fg="Red")
            lbl11.place(x=10,y=250)
        time.sleep(1)

hil1=threading.Thread(target=serialRe,daemon=True)
ser =Serial('COM3', 115200)
main_codigo() 

    



    





