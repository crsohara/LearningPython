'''
Created on Aug 5, 2013

@author: seriousbuns
'''
from Tkinter import *
import time
import threading

class Example(Frame):
  
    def __init__(self, parent):
        self.root = parent
        self.root.title("Simple Countdowntimer")
        self.frame = Frame(parent)
        self.frame.pack(expand = True, anchor=CENTER)
        self.text = StringVar()
        self.text.set("click start to begin")
        self.label = Label(self.frame, textvariable=self.text)
        self.label.pack()
        self.min_scale = Scale(self.frame, from_=60, to=0, orient=VERTICAL, label='minutes')
        self.min_scale.pack()
        self.scale = Scale(self.frame, from_=0, to=60, orient=HORIZONTAL, label='seconds')
        self.scale.pack()
        self.startbutton = Button(text="start", command=lambda: threading.Thread(target=self.do_stuff).start())
        self.startbutton.pack()
        
    def do_stuff(self):
        m = self.min_scale.get()
        i = self.scale.get()
        
        i += m*60
        for ik in range(-1, i):
            self.min_scale.set(i/60)
            self.scale.set( i % 60 )
            root.update()
            print('h')
            time.sleep(1)
            i-=1

root = Tk()
root.geometry("350x350")
app = Example(root)
root.mainloop()