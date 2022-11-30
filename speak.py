from tkinter import *
import pyttsx3

root=Tk()

engine=pyttsx3.init()

def text_speh():
    
    engine.say(speech.get())
    engine.runAndWait()
    engine.stop()
    
    

    






speech=StringVar()



Lab=Label(text="enter the text:" ,font="arial 10")
Lab.place(x=30,y=80)
enter1=Entry(textvariable=speech, font="arial").place(x=120,y=80)

but1=Button(text="speack now",command=lambda:text_speh(),font="arial", bg="black",fg="white")
but1.place(x=350,y=80)


root.geometry("500x300")
root.mainloop()
