#with tkinter we can create windows and widgets used for GUI

from tkinter import *

window=Tk()

def miles_to_km():
    print(e1_value.get())
    kms=float(e1_value.get())*1.6
    t1.insert(END,kms)

b1=Button(window,text="EXECUTE",command=miles_to_km) #Creates button
b1.grid(row=0,column=0)#creates grid

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value) #Entry box beside button
e1.grid(row=0,column=1)  #creates grid

t1=Text(window,height=1,width=20) #Creates a Text box
t1.grid(row=0,column=2)#creates grid

window.mainloop()# without this the window wont popup