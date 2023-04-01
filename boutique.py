import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter.ttk import *




root = tk.Tk()
root.configure(bg='dark blue')
root.title('boutique')
root.geometry('600x400')
root_interface = Label(root,width=80,text='',font='arial')
root_interface.pack()
root_entry_nom = Label(root,text='Nom',font='arial')
root_entry_nom.pack()
root_entry_nom.place(x=60,y=300)
root_entry_description = Label(root,text='Description',font='arial')
root_entry_description.pack()
root_entry_description.place(x=10,y=350)
root_entry_prix = Label(root,text='prix',font='arial')
root_entry_prix.pack()
root_entry_prix.place(x=320,y=350)
root_entry_quantité = Label(root,text='quantité',font='arial')
root_entry_quantité.place()
root_entry_quantité.place(x=290,y=300)
root_entry_id_catégorie = Label(root,text='id',font='arial')
root_entry_id_catégorie.pack()
root_entry_id_catégorie.place(x=210,y=325)

entrybox_nom = Entry(root)
entrybox_nom.pack()
entrybox_nom.place(x=100,y=300)
entrybox2_description = Entry(root)
entrybox2_description.pack()
entrybox2_description.place(x=100,y=350)
entrybox3_prix = Entry(root)
entrybox3_prix.pack()
entrybox3_prix.place(x=350,y=350)
entrybox4_quantité = Entry(root)
entrybox4_quantité.pack()
entrybox4_quantité.place(x=350,y=300)
entrybox5_id_catégorie = Entry(root)
entrybox5_id_catégorie.pack()
entrybox5_id_catégorie.place(x=230,y=325)




db = mysql.connector.connect(host='localhost',user='antony',password='root', database='boutique')
curseur = db.cursor()

def liste():
    curseur.execute('SELECT * FROM produit')
    var = curseur.fetchall()
    for i in var:
        list_box.insert('',END,values=i)

def ajouter():
    nom = entrybox_nom.get()
    description = entrybox2_description.get()
    prix = int (entrybox3_prix.get())
    quantité = int (entrybox4_quantité.get())
    id_catégorie =  int (entrybox5_id_catégorie.get())
    curseur.execute('INSERT INTO produit  (nom,description,prix,quantité,id_catégorie) VALUES (%s,%s,%s,%s,%s)',(nom,description,prix,quantité,id_catégorie))
    db.commit()
    remove()
    update()

def update():
    curseur.execute('SELECT * FROM produit')
    var = curseur.fetchall()
    for x in var:
        list_box.insert('',END,values=x)

def remove():
    for item in list_box.get_children():
        list_box.delete(item)

def db_remove():
    variable = list_box.focus()
    variable2 = list_box.item(variable)
    id = variable2['values'][0]
    print(list_box.item(variable))
    curseur.execute('DELETE FROM produit WHERE id=%s',[id])
    db.commit()
    remove()
    update()
    


interface_boutton = Button(root,text='produits').place(x=250,y=20)
interface_boutton2 = Button(root,text='ajouter',command=ajouter).place(x=340,y=20)
interface_boutton3 = Button(root,text='supprimer',command=db_remove).place(x=150,y=20)
interface_boutton4 = Button(root,text='modifier').place(x=430,y=20)
list_box = Treeview(root,columns=['nom','prix'])
list_box.heading('nom',text='article')
list_box.heading('prix',text='prix')
list_box['show'] = 'headings'
list_box.pack()
list_box.place(x=110,y=70)
liste()
root.mainloop()