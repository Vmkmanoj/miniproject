from tkinter import *
from tkinter import messagebox
import time




        
        
    






root=Tk()
root.resizable(False,False)
root.configure(bg="#fff")
root.geometry("850x500")
root.title("login")

def on_enter(e):
    entery.delete(0,"end")

def on_leave(e):
    entery1.delete(0,"end")

def create():
    new=Toplevel(root)
    new.geometry("300x300")
    new.config(bg="white")
    new.title("create acc")
    new.resizable(False,False)
    Label(new,text="let create a acc",font="arial 22",bg="white").place(x=5,y=5)

    new.mainloop()
    
    





def load():
    time.sleep(2)

    name1=name.get()
    passw=password.get()


    if name1=="manoj" and passw=="1234":
        new=Toplevel(root)
        new.geometry("1300x1400")
        new.title("App")
        Label(new,text="Hello dear custmor",font="Arial 30 bold").place(x=450,y=400)
        new.mainloop()


    elif name1!="manoj" and passw!="1234":
        messagebox.showerror("invalid","invalid user name and password")
    elif passw!="1234":
        messagebox.showerror("invalid","invalid password")
    elif name!="manoj":
        messagebox.showerror("invalid","invalid name")
#----imgae insert-----#
img=PhotoImage(file="login.png")
Label(root,image=img,bg="white").place(x=20,y=40)

########-----input---###########


frame=Frame(root,width=300,height=300,bg="white",border=10).place(x=500,y=60)
sign=Button(frame,text="create account..",font="Arial 7",bg="white",command=lambda:create()).place(x=600,y=280)


heading=Label(frame,text="Sign in",font=("microsoft yahei ui light",15,"bold"),bg="white").place(x=610,y=75)
#------shoring-----#

# name=StringVar()

name=StringVar()
password=StringVar()



#-------entery-------#


entery=Entry(frame,font=("microsoft yahei ui light",9),width=30,border=0,textvariable=name)
entery.place(x=550,y=140)
entery.insert(0,"user name")
entery.bind("<FocusIn>",on_enter)



entery1=Entry(frame,font=("microsoft yahei ui light",9),width=30,border=0,textvariable=password)
entery1.place(x=550,y=180)
entery1.insert(0,"password")
entery1.bind("<FocusOut>",on_leave)

Frame(frame,width=200,height=2,bg="black").place(x=550,y=160)
Frame(frame,width=200,height=2,bg="black").place(x=550,y=205)

#------submit button----#

but=Button(frame,text="submit",font=("microsoft yahei ui light",10),bg="#71acd9",command=lambda:load(),width=23)
but.place(x=550,y=220)




root.mainloop()
