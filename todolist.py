from tkinter import *
from tkinter import messagebox
t=Tk()
t.title("To Do List")
t.geometry("350x600")
add_items=StringVar()
ed=StringVar()
def ad():
    global c
    l=add_items.get()
    if l!="":
        list.insert(END, l)
        additem.delete(0,END)
    else:
        messagebox.showwarning("invalid input","Enter the task to add")


def edit_task():
    index = list.curselection()
    if index:
        task_text = list.get(index)
        additem.delete(0, END)
        additem.insert(END,task_text)
    else:
        messagebox.showwarning("Invalid input","Select the task to edit")

def update_task():
    index = list.curselection()
    if index:
        updated_task = additem.get()
        list.delete(index)
        list.insert(index, updated_task)
        additem.delete(0, END)
    else:
        messagebox.showwarning("Invalid input","Select the task to edit and the update")

def delete_task():
    index = list.curselection()
    if index:
        list.delete(index)  
    else:
        messagebox.showwarning("Invalid input","Select the task to delete")

head=Label(t,text="To Do List",font=("Arial Bold",20))
head.grid(row=0,column=0,columnspan=2,pady=10,padx=10)

add=Label(t,text="Add Items",font=("Arial",15))
add.grid(row=1,column=0,columnspan=2,pady=10,padx=10)

additem=Entry(t,text="",textvariable=add_items,font=("Arial",15),relief="solid")
additem.grid(row=2,column=0,columnspan=2,pady=10,padx=10)

sub=Button(t,text="Add",font=("Arial",15),activebackground="green",command=ad)
sub.grid(row=3,column=0,pady=10,padx=10,ipadx=10)

delet=Button(t,text="Delete",font=("Arial",15),activebackground="green",command=delete_task)
delet.grid(row=3,column=1,padx=10,pady=10)

edit=Button(t,text="Edit",font=("Arial",15),activebackground="green",command=edit_task)
edit.grid(row=4,column=0,pady=10,padx=10,ipadx=10)

update=Button(t,text="Update",font=("Arial",15),activebackground="green",command=update_task)
update.grid(row=4,column=1,padx=10,pady=10)


tasks=Label(t,text="Tasks",font=("Arial",15))
tasks.grid(row=5,column=0,columnspan=2,pady=10,padx=10)

list=Listbox(t,relief="solid",font=("Arial",15),width=25)
list.grid(row=6,column=0,columnspan=2,pady=10,padx=10)

t.mainloop()
