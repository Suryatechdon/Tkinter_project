from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("employee.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1366x768+0+0")
root.state("zoomed")
root.config(bg="#2f4f4f")

name=StringVar()
age=StringVar()
city=StringVar()
gender=StringVar()
mail=StringVar()
contact=StringVar()
address=StringVar()


#Entry_Frames
entries_frames=Frame(root,bg="#c0c0c0")
entries_frames.pack(padx=5,pady=8,fill=X)
title=Label(entries_frames,text="Employee Management System",font=("calibri",16,"bold"),bg="#c0c0c0",fg="black")
title.grid(padx=5,pady=8,columnspan=2)

lblname=Label(entries_frames,text="Name",font=("calibri",12,"bold"),bg="#c0c0c0",fg="black")
lblname.grid(row=1,column=0,padx=5,pady=8,sticky="w")
txtname=Entry(entries_frames,textvariable=name,font=("calibri",12,"bold"),bg="white",fg="black")
txtname.grid(row=1,column=1,padx=5,pady=8,sticky="w")

lblage=Label(entries_frames,text="Age",font=("calibri",12,"bold"),bg="#c0c0c0",fg="black")
lblage.grid(row=1,column=2,padx=5,pady=8,sticky="w")
txtage=Entry(entries_frames,textvariable=age,font=("calibri",12,"bold"),bg="white",fg="black")
txtage.grid(row=1,column=3,padx=5,pady=8,sticky="w")

lblcity=Label(entries_frames,text="City",font=("calibri",12,"bold"),bg="#c0c0c0",fg="black")
lblcity.grid(row=2,column=0,padx=5,pady=8,sticky="w")
txtcity=Entry(entries_frames,textvariable=city,font=("calibri",12,"bold"),bg="white",fg="black")
txtcity.grid(row=2,column=1,padx=5,pady=8,sticky="w")

lblgender=Label(entries_frames,text="Gender",font=("calibri",12,"bold"),bg="#c0c0c0",fg="black")
lblgender.grid(row=2,column=2,padx=5,pady=8,sticky="w")
combogender=ttk.Combobox(entries_frames,font=("calibri",12,"bold"),textvariable=gender,width="18",state="readonly")
combogender['values']=("male","female")
combogender.grid(row=2,column=3,padx=5,pady=8,sticky="w")

lblmail=Label(entries_frames,text="Mail",font=("calibri",12,"bold"),bg="#c0c0c0",fg="black")
lblmail.grid(row=3,column=0,padx=5,pady=8,sticky="w")
txtmail=Entry(entries_frames,textvariable=mail,font=("calibri",12,"bold"),bg="white",fg="black")
txtmail.grid(row=3,column=1,padx=5,pady=8,sticky="w")

lblcontact=Label(entries_frames,text="Contact",font=("calibri",12,"bold"),bg="#c0c0c0",fg="black")
lblcontact.grid(row=3,column=2,padx=5,pady=8,sticky="w")
txtcontact=Entry(entries_frames,textvariable=contact,font=("calibri",12,"bold"),bg="white",fg="black")
txtcontact.grid(row=3,column=3,padx=5,pady=8,sticky="w")

lbladdress=Label(entries_frames,text="Address",font=("calibri",12,"bold"),bg="#c0c0c0",fg="black")
lbladdress.grid(row=4,column=0,padx=5,pady=8,sticky="w")
txtaddress=Text(entries_frames,font=("calibri",12,"bold"),width=120,height=6)
txtaddress.grid(row=4,column=1,padx=5,pady=8,columnspan=10,sticky="w")



#Button_Process
def getdata(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    name.set(row[1])
    age.set(row[2])
    city.set(row[3])
    gender.set(row[4])
    mail.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[7])

def display():
    tv.delete(*tv.get_children())
    for row in db.select():
        tv.insert("",END,values=row)
def insert_data():
    if txtname.get()=="" or txtage.get()=="" or txtcity.get()=="" or combogender.get()=="" or txtmail.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error","Please Enter the Valid Values")
        return
    db.insert(txtname.get(),txtage.get(),txtcity.get(),combogender.get(),txtmail.get(),txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("success","Data added")
    clear_data()
    display()

def update_data():
    if txtname.get()=="" or txtage.get()=="" or txtcity.get()=="" or combogender.get()=="" or txtmail.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error","Please Enter the Valid Values")
        return
    db.update(txtname.get(),txtage.get(),txtcity.get(),combogender.get(),txtmail.get(),txtcontact.get(),txtaddress.get(1.0,END),row[0])
    messagebox.showinfo("success","Data updated")
    clear_data()
    display()

def delete_data():
    db.delete(row[0])
    clear_data()
    display()

def clear_data():
    name.set("")
    age.set("")
    city.set("")
    gender.set("")
    mail.set("")
    contact.set("")
    txtaddress.delete(1.0,END)


#Button_Frames
btn_frames=Frame(entries_frames,bg="#c0c0c0")
btn_frames.grid(row=5,column=0,padx=5,pady=8,columnspan=4)
btn_add=Button(btn_frames,text="Add details",command=insert_data,bg="white",fg="black",width=10).grid(row=5,column=0,padx=5,pady=8)
btn_update=Button(btn_frames,text="Update details",command=update_data,bg="blue",fg="white",width=10).grid(row=5,column=1,padx=5,pady=8)
btn_delete=Button(btn_frames,text="Delete details",command=delete_data,bg="yellow",fg="black",width=10).grid(row=5,column=2,padx=5,pady=8)
btn_clear=Button(btn_frames,text="Clear details",command=clear_data,bg="red",fg="black",width=10).grid(row=5,column=3,padx=5,pady=8)


#Table_Frames
tree_frames=Frame(root,bg="white")
tree_frames.place(x=5,y=400,width=1350,height=250)
style=ttk.Style()
style.configure("mystyle.Treeview",bg="white",fg="black",rowheight=35,anchor="center")
style.configure("mystyle.Treeview.Headings",bg="white",fg="black")
tv=ttk.Treeview(tree_frames,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=4,anchor="center")
tv.heading("2",text="Name")
tv.column("2",anchor="center")
tv.heading("3",text="Age")
tv.column("3",width=12,anchor="center")
tv.heading("4",text="City")
tv.column("4",anchor="center")
tv.heading("5",text="Gender")
tv.column("5",anchor="center")
tv.heading("6",text="Mail")
tv.column("6",anchor="center")
tv.heading("7",text="Contact")
tv.column("7",anchor="center")
tv.heading("8",text="Address")
tv.column("8",anchor="center")
tv.bind("<ButtonRelease-1>",getdata)
tv.pack(fill=X)
tv['show']="headings"


display()
root.mainloop()

