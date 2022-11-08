'''
Project Phase 2
Warehouse Managment Systems
Team ABC

Author: Lauren Lietzke
Page: Products for Users
'''

import tkinter as tk
import tkmacosx as tkmac
window=tk.Tk()
window.title('Warehouse Management System')
window.geometry('800x500')
window.configure(bg='blue')

lblUser_products=tk.Label(window,text='User Product Window', bg='blue', fg='white', padx=100)
lblUser_products.grid(row=0,column=0)

texProducts=tk.Text(window, bg='white', height=25, width=50, padx=50)
texProducts.grid(row=1,column=0)

btnAdd=tkmac.Button(window, text='Add Product to Favorites List', padx=30)
btnAdd.grid(row=0, column=1)

btnRequest=tkmac.Button(window, text='Request to Borrow a Product', padx=30)
btnRequest.grid(row=1, column=1)

btnSearch=tkmac.Button(window, text='Search Product Library', padx=30)
btnSearch.grid(row=2, column=1)

btnReturn=tkmac.Button(window, text='Return to Main Menu', padx=30)
btnReturn.grid(row=3, column=1)

window.mainloop()

