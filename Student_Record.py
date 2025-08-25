from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
global mytree

#class------->
class database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.c=self.con.cursor()
        self.c.execute("""
             CREATE TABLE IF NOT EXISTS data(
                 pid INTEGER PRIMARY KEY,
                 Roll INTEGER NOT NULL,
                 Name TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 gender TEXT NOT NULL
                    
             )          
                       """)
        self.con.commit()
    def insert(self,rol,name,age,gender):
        sql="""
        INSERT INTO data VALUES(NULL,?,?,?,?)
        """
        self.c.execute(sql,(rol,name,age,gender))
        self.con.commit()
    def update(self,rol,name,age,gender,pid):
        sql=""" 
        UPDATE data set Roll=?,Name=?,Age=?,Gender=? WHERE pid=?
        """
        self.c.execute(sql,(rol,name,age,gender,pid))
        self.con.commit()
    def fetch(self):
       return self.c.execute("SELECT * FROM data").fetchall()
    def delete(self,pid):
       sql="""
       DELETE FROM data WHERE pid=?
       """
       self.c.execute(sql,(pid,))
       self.con.commit()
    def alldatadel(self):
        self.c.execute("DELETE FROM data")
        self.con.commit()
        
#----------------------< 
         
#functions-------------->
def add():
    mytree.insert("",index="end",values=(naro.get(),naname.get(),naage.get(),nagender.get()))
    datas=database("update.db")
    datas.insert(naro.get(),naname.get(),naage.get(),nagender.get())
    naro.delete(0,END)   
    naname.delete(0,END)   
    naage.delete(0,END)   
    nagender.delete(0,END) 
def select():
    naro.delete(0,END)   
    naname.delete(0,END)   
    naage.delete(0,END)   
    nagender.delete(0,END) 
    id=mytree.focus()
    value=mytree.item(id,"values")
    naro.insert(0,value[0])   
    naname.insert(0,value[1])   
    naage.insert(0,value[2])   
    nagender.insert(0,value[3])
def update():
    id = naro.get()
  
    index=mytree.focus()
    iid=mytree.focus()
    mytree.item(index,values=(id,naname.get(),naage.get(),nagender.get()))
    datas=database("update.db")
    datas.update(id,naname.get(),naage.get(),nagender.get(),iid)
    naro.delete(0,END)   
    naname.delete(0,END)   
    naage.delete(0,END)   
    nagender.delete(0,END) 
def delete():
    id=mytree.focus()    
    mytree.delete(id)
    datas=database("update.db")
    datas.delete(id)
    naro.delete(0,END)   
    naname.delete(0,END)   
    naage.delete(0,END)   
    nagender.delete(0,END)
def deleteall():
    for i in mytree.get_children():
        mytree.delete(i)
    
    datas=database("update.db")
    datas.alldatadel()
#--------------<    
    
        
    

krish=Tk()
krish.config(bg="#DEC3BE")
#frames----->
newfram=Frame(krish,bg="#DEC3BE")
newfram.grid(row=0,column=0)

btnframe=Frame(krish,bg="#DEC3BE")
btnframe.grid(row=1,column=0)

treeframe=Frame(krish,bg="#DEC3BE")
treeframe.grid(row=2,column=0)
#---------<
#heading----->
heading=Label(newfram,text="Studen Record Management System",font=("times",20,"bold"),fg="blue",bg="#DEC3BE")
heading.grid(columnspan=3)
#---------<
krish.geometry("1000x500")
krish.title("student record")

#labels#--------->
labrol=Label(newfram,text="Roll",font=("times",20,"bold"))
labrol.grid(row=1,column=0,pady=20)
labname=Label(newfram,text="Name",font=("times",20,"bold"))
labname.grid(row=2,column=0,pady=20)
labage=Label(newfram,text="Age",font=("times",20,"bold"))
labage.grid(row=3,column=0,pady=20)
labgender=Label(newfram,text="Gender",font=("times",20,"bold"))
labgender.grid(row=4,column=0,pady=20)
#---------<
#Entrys------>
naro=Entry(newfram,font=("times",20,"bold"),fg="black")
naro.grid(row=1,column=1,pady=5)
naname=Entry(newfram,font=("times",20,"bold"))
naname.grid(row=2,column=1,pady=5)
naage=Entry(newfram,font=("times",20,"bold"))
naage.grid(row=3,column=1,pady=5)
nagender=Entry(newfram,font=("times",20,"bold"))
nagender.grid(row=4,column=1,pady=5)
#---------<
#Tree view------>
mytree=ttk.Treeview(treeframe,selectmode="extended")
mytree["columns"]=("Roll","Name","Age","Gender")
mytree.column("#0",width=0,stretch=NO)
mytree.column("#1",width=50)
mytree.column("#2",width=200)
mytree.column("#3",width=200)
mytree.column("#4",width=200)

mytree.heading("#0",text="")
mytree.heading("#1",text="Roll")
mytree.heading("#2",text="Name")
mytree.heading("#3",text="Age")
mytree.heading("#4",text="Gender")
mytree.grid(row=7,column=1,pady=20,padx=50)
#---------<
#fetch the data into database--------->
datas=database("update.db")
value=datas.fetch()
for i in value:
    pid, roll, name, age, gender = i
    mytree.insert("", "end", iid=str(pid), values=(roll, name, age, gender))
#---------<
#-----Buttons---------# 
addbtn=Button(btnframe,text="add datas",font=("times",20,"bold"),command=add,bg="green",fg="white")
addbtn.pack(side="left", padx=5)

btnselet=Button(btnframe,text="select",font=("times",20,"bold"),command=select,bg="red",fg="white")
btnselet.pack(side="left", padx=5)

btnupdate=Button(btnframe,text="update",font=("times",20,"bold"),command=update,bg="yellow",fg="white")
btnupdate.pack(side="left", padx=5)

btndelet=Button(btnframe,text="Delete",font=("times",20,"bold"),command=delete,bg="blue",fg="white")
btndelet.pack(side="left", padx=5)

btndeletall=Button(btnframe,text="Deleteall",font=("times",20,"bold"),command=deleteall,bg="orange",fg="white")
btndeletall.pack(side="left", padx=5)
#---------<
krish.mainloop()