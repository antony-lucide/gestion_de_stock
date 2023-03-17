import mysql.connector
import tkinter as tk
from tkinter import *

db = mysql.connector.connect(host='localhost',user='root',password='root', database='boutique')
curseur = db.cursor()

def liste():
    curseur.execute('SELECT * FROM boutique')
    var = curseur.fetchall()
    Listbox.insert(END,var)


root = tk.Tk()
root.configure(bg='dark blue')
root.title('boutique')
root.geometry('600x400')
root_interface = Label(root,width=80, height=3,text='',font='arial')
root_interface.pack()
interface_boutton = Button(root,text='produits', bd=1, fg="#0059b3", bg="#ff0000",relief='sunken').place(x=250,y=20)
interface_boutton2 = Button(root,text='ajouter', bd=1, fg="#0059b3", bg="#ff0000",relief='sunken').place(x=340,y=20)
interface_boutton3 = Button(root,text='supprimer', bd=1, fg="#0059b3", bg="#ff0000",relief='sunken').place(x=150,y=20)
interface_boutton4 = Button(root,text='modifier', bd=1, fg="#0059b3", bg="#ff0000",relief='sunken').place(x=430,y=20)
list_box = Listbox(root,relief='sunken')
list_box.pack()
list_box.place(x=210,y=70)
root.mainloop()