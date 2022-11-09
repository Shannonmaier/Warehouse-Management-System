import tkinter as tk

adminMenu = tk.Tk()
adminMenu.title("Admin Main Menu")
adminMenu.geometry('800x500')
adminMenu.configure(bg = 'light blue')

lblAdminMenu = tk.Label(adminMenu, text = 'Admin Main Menu', bg = 'light blue', padx = 100)
lblAdminMenu.grid(row = 0, column = 2)

btnAdminProducts = tk.Button(adminMenu, text = 'View Products and Product Actions', bg = 'white', width = 20, padx = 30)
btnAdminProducts.grid(row = 2, column = 1)

btnBorrowRequests = tk.Button(adminMenu, text = 'View Borrow Requests', bg = 'white', width = 20, padx = 30)
btnBorrowRequests.grid(row = 4, column = 1)

btnUsers = tk.Button(adminMenu, text = 'View Users and User Actions', bg = 'white', width = 20, padx = 30)
btnUsers.grid(row = 2, column = 3)

btnAdminPass = tk.Button(adminMenu, text = 'Change Admin User and Password', width = 20, bg = 'white', padx = 30)
btnAdminPass.grid(row = 4, column = 3)

btnExit = tk.Button(adminMenu, text = 'Log Out', width = 10, bg = 'white', padx = 30)
btnExit.grid(row = 6, column = 3)

adminMenu.mainloop()
