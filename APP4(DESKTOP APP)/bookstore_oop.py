from tkinter import *

from backend_oop import Database

database=Database("books.db")


window=Tk()
window.wm_title("BOOKSTORE")

#function that selects the rows in the listbox
def get_selected_row(event):
    try:
        global selected_tuple #making it global since we cant call the this function in delete_command because of event parameter
        index=list1.curselection()[0] #when item in listbox is selected it displays the respective index and comma ex:(2,),hence first index[0]
        selected_tuple=list1.get(index)  #get the tuple based on index
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass
     


def view_command():
    list1.delete(0,END)  #to prevent repeatitive views when you click on viewall 
    for row in database.viewall():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()):
        list1.insert(END,row)


def add_command():
    #list1.delete(0,END)
    database.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    #list1.delete(0,END)
    #list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()))


def delete_command():
    database.delete(selected_tuple[0])
    
def update_command():
    database.update(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get(),selected_tuple[0])
    



#Adding labels
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)


#Adding entry bars
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)


list1=Listbox(window,height=7,width=40)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
#list1.grid(row=2,column=0)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=20)

#Apply configure methods to list and scrollbar
list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

#binding method to the list box widget
#takes 2 args --> 1.event type 2.funtion tht binds to event type

list1.bind('<<ListboxSelect>>',get_selected_row)



#Adding buttons

B1=Button(window,text="View all",width=20,command=view_command)
B1.grid(row=2,column=3)

B2=Button(window,text="Search a book",width=20,command=search_command)
B2.grid(row=3,column=3)

B3=Button(window,text="Add a book",width=20,command=add_command)
B3.grid(row=4,column=3)

B4=Button(window,text="Update selected ",width=20,command=update_command)
B4.grid(row=5,column=3)

B5=Button(window,text="delete selected",width=20,command=delete_command)
B5.grid(row=6,column=3)

B6=Button(window,text="close",width=20,command=window.destroy)
B6.grid(row=7,column=3)




window.mainloop()
#################use py installer lib to create standalone executable  file in below way
#  pyinstaller --onefile --windowed <<filename>>