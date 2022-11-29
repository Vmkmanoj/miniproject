import tkinter as tk


calculation=""
def cal(sub):
    global calculation
    calculation=calculation+str(sub)
    print(calculation)
    




def evl():
    global calculation
    calculation=str(eval(calculation))
    print(calculation)


    


   



    # call=call+str(eval(call))

    # Label(call).place(x=10,y=10)




root=tk.Tk()


text_filed=tk.Text(root,height=2,width=100,font=("Arial 10")).grid(columnspan=20)


root.geometry("300x300")
bu1=tk.Button(root,text="1",height=2,width=4,font=("Arial,2"),command=lambda:cal(1)).place(x=10,y=50)
bu2=tk.Button(root,text="2",height=2,width=4,font=("Arial,2"),command=lambda:cal(2)).place(x=80,y=50)
bu3=tk.Button(root,text="3",height=2,width=4,font=("Arial,2"),command=lambda:cal(3)).place(x=160,y=50)
bu4=tk.Button(root,text="4",height=2,width=4,font=("Arial,2"),command=lambda:cal(4)).place(x=10,y=120)
bu5=tk.Button(root,text="5",height=2,width=4,font=("Arial,2"),command=lambda:cal(5)).place(x=80,y=120)
bu6=tk.Button(root,text="6",height=2,width=4,font=("Arial,2"),command=lambda:cal(6)).place(x=160,y=120)
bu7=tk.Button(root,text="7",height=2,width=4,font=("Arial,2"),command=lambda:cal(7)).place(x=10,y=180)
bu8=tk.Button(root,text="8",height=2,width=4,font=("Arial,2"),command=lambda:cal(8)).place(x=80,y=180)
bu9=tk.Button(root,text="9",height=2,width=4,font=("Arial,2"),command=lambda:cal(9)).place(x=160,y=180)
bu0=tk.Button(root,text="0",height=2,width=4,font=("Arial,2"),command=lambda:cal(0)).place(x=80,y=240)
bu22=tk.Button(root,text="+",height=2,width=4,font=("Arial,2"),command=lambda:cal("+")).place(x=220,y=180)
bu22=tk.Button(root,text="-",height=2,width=4,font=("Arial,2"),command=lambda:cal("-")).place(x=220,y=120)
but3=tk.Button(root,text="=",height=2,width=4,font=("Arial,2"),command=evl).place(x=220,y=240)
bu23=tk.Button(root,text="*",height=2,width=4,font=("Arial,2"),command=lambda:cal("*")).place(x=220,y=50)
bu22=tk.Button(root,text="/",height=2,width=4,font=("Arial,2"),command=lambda:cal("/")).place(x=160,y=240)
#calction
root.mainloop()
