'''
Date:11/8/22
Author:David Penafiel
Team:ABC
'''


import tkinter as tk
window=tk.Tk()
window.title('Admin User Window')
window.geometry('1000x500')
window.configure(bg='light blue')

frmLeft=tk.Frame(window,bg='light blue', width=900,height=500)
frmRight=tk.Frame(window,bg='light blue', width=100,height=500)

frmLeft.grid(row=0,column=0)
frmRight.grid(row=0,column=1)

lblUserName=tk.Label(frmLeft,text='Name of User',bg='light blue',padx=30,)
lblUserName.grid(row=0,column=2)

entUserName=tk.Entry(frmLeft,bg='light Grey')
entUserName.grid(row=1,column=2)

lblUsers=tk.Label(frmLeft,text='List of Users',bg='light blue',pady=30)
lblUsers.grid(row=2,column=1)

texUsers=tk.Text(frmLeft,bg='light Grey')
texUsers.grid(row=3,column=1)

btnAdd=tk.Button(frmRight,text='Add User',bg='white',padx=30, pady=10,width=10)
btnAdd.grid(row=4,column=3)

btnRemove=tk.Button(frmRight,text='Remove User',bg='white',padx=30,pady=10,width=10)
btnRemove.grid(row=5,column=3)

btnBack=tk.Button(frmRight,text='Back to Menu',bg='white',padx=30,pady=10,width=10)
btnBack.grid(row=6,column=3)

window.mainloop()

