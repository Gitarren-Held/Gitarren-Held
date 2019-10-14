import serial
import pygame


class InputArduino:
      
    def Input():
        arduino = serial.Serial(port='/dev/cu.usbmodem142101', baudrate=9600)
        listaInteprete = [0,0,0,0,0,0,0,0]
        line = arduino.readline().decode('utf-8')
        print(line)
        partes = line.split(',')
        for i in range(8):
            
            listaInteprete[i]=int(partes[i])

        return [listaInteprete]
    