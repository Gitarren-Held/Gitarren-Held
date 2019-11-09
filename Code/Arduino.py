import serial
import pygame


def Leer(direccion):
    arduino = serial.Serial(port=direccion, baudrate=9600)
    listaInteprete = [0,0,0,0,0,0,0,0]
    line = arduino.readline().decode('utf-8')
    #print(line)
    partes = line.split(',')
    for i in range(0,7):
        print(partes[i])
        listaInteprete[i]=int(partes[i])
    return listaInteprete
    