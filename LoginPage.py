'''
Author: Jaden Reasor
Group:ABC

"Login Page"

'''

import tkinter as tk
window=tk.Tk()
window.title('Login Page')
window.geometry('700x300')
window.configure(bg='white')

ttlName=tk.Label(window,text='Login Page',bg='white',padx=10)
ttlName.grid(row=0,column=1)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

lblUsername=tk.Label(window,text='Username', bg='white')
lblUsername.grid(row=1,column=0)

entUsername=tk.Entry(window,bg='grey')
entUsername.grid(row=2,column=0)

lblPassword=tk.Label(window,text='Password',bg='white')
lblPassword.grid(row=1,column=2)

entPhone=tk.Entry(window,bg='grey')
entPhone.grid(row=2,column=2)

btnLogin=tk.Button(window,text='Login',bg='blue',width=20, height=2)
btnLogin.grid(row=3,column=1)

window.mainloop()
