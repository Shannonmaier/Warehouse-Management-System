'''
Date: 11/8/22
Author: Dan Aulbach
Group: ABC

"User Main Menu"

'''

import tkinter as tk
window=tk.Tk()
window.title('User Main Menu-- WMS')
window.geometry('700x300')
window.configure(bg='blue')




ttlName=tk.Label(window,text='User Main Menu',bg='white',padx=10)
ttlName.grid(row=0,column=1)


window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)


btnProduct=tk.Button(window,text='View Products and User Product Actions', width=30, height=5)
btnProduct.grid(row=1,column=0)

btnFavorite=tk.Button(window,text='View Favorites List', width=30, height=5)
btnFavorite.grid(row=1,column=2)

btnBorrowed=tk.Button(window,text='View Borrowed Items History', width=30, height=5)
btnBorrowed.grid(row=2,column=1)

btnExit=tk.Button(window,text='Exit',bg='red', width=20, height = 2)
btnExit.grid(row=3,column=2)


window.mainloop
