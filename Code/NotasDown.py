import threading
import time
import note

class Timer(threading.Thread):
    def __init__(self,Green,Red,Blue,Yellow,Orange,notas,screen):
        self.Green = Green
        self.Red = Red
        self.Blue = Blue
        self.Yellow = Yellow
        self.Orange = Orange
        self.notas = notas
        self.screen = screen
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
            note.Down(self.Green,self.Red,self.Blue,self.Yellow,self.Orange,self.notas,self.screen)
            self.event.wait( 1 )

    def stop(self):
        self.event.set()
