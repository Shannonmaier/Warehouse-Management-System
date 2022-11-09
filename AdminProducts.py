'''
Date:11/8/22
Author:Shannon Maier
Team:ABC
Title: CMPT Group Project Phase 02
'''

import tkinter as tk
window=tk.Tk()
window.title('Admin Products and Actions')
window.geometry('900x500')
window.configure(bg= 'blue')


lftFrame = tk.Frame(master = window, width = 700, height = 500, bg ="blue", padx = 40)
lftFrame.pack(side = tk.LEFT)

rtFrame = tk.Frame(master = window, width = 500, height = 500, bg = "blue")
rtFrame.pack(side = tk.LEFT)

              
lblName=tk.Label(lftFrame,text='Product List', bg='white', padx=30, width = 10)
lblName.pack()

texProduct = tk.Text(lftFrame)
texProduct.pack()

btnAdd = tk.Button(rtFrame,text="Add Product", width= 10, height = 2)
btnAdd.grid(row = 1, column = 2, pady=15)

btnDel = tk.Button(rtFrame, text="Remove Product", width= 10, height = 2,)
btnDel.grid(row = 2, column =2, pady =15)

btnEdit = tk.Button(rtFrame, text="Edit Product", width= 10, height = 2,)
btnEdit.grid(row = 3, column =2, pady =15)

btnSearch = tk.Button(rtFrame, text="Search Product", width= 10, height = 2,)
btnSearch.grid(row = 4, column =2, pady =15)


btnBack = tk.Button(rtFrame, text="Back to menu", width= 7, height = 1,)
btnBack.grid(row =5, column =2, pady =15)

window.mainloop()
