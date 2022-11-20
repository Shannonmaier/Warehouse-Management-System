from tkinter import *
import tkinter as tk
from tkinter import messagebox  
import csv
import os
import os.path

##=============================Admin User Page===========================================


    
    
def AdminUserPage():
    def deletePage():
        window.destroy()

        
    def addPage():

        def Add():
            name = entName.get()
            password = entPass.get()
            username =entUsername.get()
            

            texUsers.insert(tk.END, name + "  -  " + username + '  -  ' + '  -  ' + password)
            with open('users.csv', "a", newline = '') as file:
                csvWriter = csv.writer(file)
                csvWriter.writerow([name,username,password])

        add = tk.Tk()
        add.title('Add Product')
        add.geometry('400x300')
        add.configure(bg='blue')

        frmAdd = tk.Frame(add, bg = "blue", width = 600, height = 400)
        frmAdd.pack()

    
        lblName=tk.Label(frmAdd,text='Name', bg="blue", padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmAdd, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        
        lblUsername=tk.Label(frmAdd,text='Username', bg="blue",)
        lblUsername.grid(row=0,column=1)

        entUsername=tk.Entry(frmAdd, bg='orange', width =10,)
        entUsername.grid(row=1,column=1)

        lblPass=tk.Label(frmAdd,text='Password',  bg="blue", padx = 10)
        lblPass.grid(row=0,column=2)

        entPass= tk.Entry(frmAdd, bg='orange', width = 10,)
        entPass.grid(row=1,column=2)

        btnAdd=tk.Button(frmAdd, text='Add User', bg='green', padx=30, width = 10, command = Add )
        btnAdd.grid(row=3, column=1, pady= 30)

    def RemoveUserPage():

        def RemoveUser():
            lines = []
            password= entPass.get()
            username = entUsername.get()
            
            with open('users.csv', "r") as file:
                csvReader = csv.reader(file)
                for row in csvReader:
                    if (row[1]!= username and row[2] !=username):
                        lines.append(row)
                
                             
            os.remove("users.csv")
            with open('users.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(lines)

            texUsers.delete(1.0, tk.END)
            with open('users.csv', "r") as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    texUsers.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2])

                    
        remove = tk.Tk()
        remove.title('Delete User')
        remove.geometry('400x300')
        remove.configure(bg='blue')

        frmPage = tk.Frame(remove, bg = "blue", width = 600, height = 400)
        frmPage.pack()

    
        lblUsername=tk.Label(frmPage,text='Username', bg="blue", padx = 10)
        lblUsername.grid(row=0,column=0)

        entUsername=tk.Entry(frmPage, bg='orange', width =10,)
        entUsername.grid(row=1,column=0)

        
        lblMid=tk.Label(frmPage,text='', bg="blue", width =1)
        lblMid.grid(row=1,column=1)

        lblPass=tk.Label(frmPage,text='Password',  bg="blue", padx = 10)
        lblPass.grid(row=0,column=2)

        entPass= tk.Entry(frmPage, bg='orange', width = 10,)
        entPass.grid(row=1,column=2)

        btnDelete=tk.Button(frmPage, text='Remove User', bg='green', padx=30, width = 10, command = RemoveUser)
        btnDelete.grid(row=3, column=1, pady= 30)

        
        
                

       
        
        

    import tkinter as tk
    window=tk.Tk()
    window.title('Admin User Window')
    window.geometry('1000x500')
    window.configure(bg='light blue')

    frmLeft=tk.Frame(window,bg='light blue', width=700,height=500)
    frmRight=tk.Frame(window,bg='light blue', width=300,height=500)

    frmLeft.grid(row=0,column=0)
    frmRight.grid(row=0,column=1)

    
    lblUsers=tk.Label(frmLeft,text='List of Users',bg='light blue',pady=30)
    lblUsers.grid(row=1,column=1)

    texUsers=tk.Text(frmLeft,bg='light Grey')
    texUsers.grid(row=2,column=1)

    if os.path.exists('users.csv')== True:
        texUsers.delete(1.0, tk.END)
        with open('users.csv','r') as file:
                csvReader = csv.reader(file)

                for member in csvReader:
                    texUsers.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "\n")

    btnAdd=tk.Button(frmRight,text='Add User',bg='white',padx=30, pady=10,width=10, command = addPage)
    btnAdd.grid(row=1,column=1, padx=30)

    btnRemove=tk.Button(frmRight,text='Remove User',bg='white',padx=30,pady=10,width=10, command = RemoveUserPage)
    btnRemove.grid(row=2,column=1, padx=30)

    btnBack=tk.Button(frmRight,text='Back to Menu',bg='white',padx=30,pady=10,width=10,
                      command = lambda: [deletePage(), AdminMenu()])
    btnBack.grid(row=3,column=1, padx=30)

    window.mainloop()

#=============================Login Page===========================================


AdminUser = "Admin"
AdminPass = "Password"

if os.path.exists('AdminLogin.csv')!= True:
    with open('AdminLogin.csv', "w",) as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow([AdminUser, AdminPass])

if os.path.exists('users.csv')!= True:
    with open('users', "a",) as file:
        csvWriter = csv.writer(file)





def LoginPage():
    def deleteLogin():
        window.destroy()

    def Login():
        User =entUsername.get()
        Pass =  entPassword.get()
        

        with open ('AdminLogin.csv', "r",) as file:
            csvReader = csv.reader(file)
            for member in csvReader:
                if(User == member[0] and Pass == member[1]):
                    messagebox.showinfo("","Login Success")
                    deleteLogin()
                    AdminMenu()
                else:
                    with open('users.csv', "r",) as file:
                        csvRead=csv.reader(file)
                        for member in csvRead:
                            if (User == member[1] and Pass == member[2]):
                                messagebox.showinfo("","Login Success")
                                deleteLogin()
                                userMenu()
                            else:
                                messagebox.showinfo("","Incorrect Username or Password ")

                    
                                
            
        
             
        
    import tkinter as tk
    window=tk.Tk()
    window.title('Login Page')
    window.geometry('700x300')
    window.configure(bg='white')

    frmPage = tk.Frame(window, bg = "blue", width = 600, height = 400)
    frmPage.pack()

    lblTop = tk.Label(frmPage,text='LOGIN PAGE', bg="white", )
    lblTop.grid(row=0,column=1, pady = 40)
    
    lblUsername=tk.Label(frmPage,text='Username', bg='white')
    lblUsername.grid(row=1,column=0)

    entUsername=tk.Entry(frmPage,bg='grey')
    entUsername.grid(row=2,column=0)
 
    lblMid=tk.Label(frmPage,text='', bg="blue", width =1)
    lblMid.grid(row=1,column=1)

    lblPassword=tk.Label(frmPage,text='Password',bg='white')
    lblPassword.grid(row=1,column=2)

    entPassword=tk.Entry(frmPage,bg='grey')
    entPassword.grid(row=2,column=2)

    btnLogin=tk.Button(frmPage,text='Login',bg='blue',width=20, height=2,  command =Login)
    btnLogin.grid(row=3,column=1, pady = 30)

    btnExit =  tk.Button(frmPage,text='Exit',bg='blue',width=10, height=1, command = deleteLogin )
    btnExit.grid(row=4,column=1, pady = 9)

    window.mainloop()
    




#=============================Admin Products Page===========================================


def AdminProducts():
    def deletePage():
        window.destroy()


    def Print():
        if os.path.exists('warehouse.csv')== True:
            texProduct.delete(1.0, tk.END)
            with open('warehouse.csv','r') as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    texProduct.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "  -  "+member[3] + "  -  "
                                  + member[4] + "  -  " +member[5] + "  -  " + member[6] + "  -  " + member[7] +'\n')

        
                
    def editPage():

        def Edit():
            name = entName.get()
            Type = entType.get()
            ID = entID.get()
            time = entTime.get()
            provider = entProvide.get()
            quant = entQuantity.get()
            place = entPlace.get()
            Price = entPrice.get() 

            lines = []
            

            with open('warehouse.csv', "r") as file:
                csvReader = csv.reader(file)
                for row in csvReader:
                    if (row[0]!= name and row[1] !=Type and row[2] !=ID and row[3] != time and
                         row[4] != provider and row[5] !=quant and row[6] !=place and row[7] != Price):
                        lines.append(row)
            lines.append([name, Type, ID, time, provider, quant, place, Price])
            
            
              
                                          
            os.remove("warehouse.csv")
            with open('warehouse.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(lines)

            texProduct.delete(1.0, tk.END)
            with open('warehouse.csv', "r") as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    if member[0] == "Name" and member[1] == "Number":
                        continue
                    texProduct.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "  -  "
                                      + member[4] + "  -  " +member[5] + "  -  " + member[6] + "  -  " + member[7] +'\n')
                



        edit = tk.Tk()
        edit.title('Edit Product')
        edit.geometry('600x400')
        edit.configure(bg='blue')

        frmEdit = tk.Frame(edit, bg = "blue", width = 600, height = 400)
        frmEdit.pack()

    


        lblName=tk.Label(frmEdit,text='Name', bg="blue", width = 10, padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmEdit, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        lblID=tk.Label(frmEdit,text='Id #',  bg="blue", width = 10, padx = 10)
        lblID.grid(row=0,column=1)

        entID= tk.Entry(frmEdit, bg='orange', width = 10,)
        entID.grid(row=1,column=1)

        lblType= tk.Label(frmEdit,text='Product Type',  bg="blue", width = 10, padx = 10)
        lblType.grid(row=0,column=2)

        entType=tk.Entry(frmEdit, bg='orange', width =10)
        entType.grid(row=1,column=2,)

        lblTime= tk.Label(frmEdit,text='Time Stored',  bg="blue", width = 10, padx = 10,)
        lblTime.grid(row=2,column=0)

        entTime=tk.Entry(frmEdit, bg='orange', width =10)
        entTime.grid(row=3,column=0)


        lblProvide= tk.Label(frmEdit,text='Provider',  bg="blue", width = 10, padx = 10,)
        lblProvide.grid(row=2,column=1)

        entProvide=tk.Entry(frmEdit, bg='orange', width =10)
        entProvide.grid(row=3,column=1)

        lblQuantity= tk.Label(frmEdit,text='Quantity',  bg="blue", width = 10, padx = 10,)
        lblQuantity.grid(row=2,column=2)

        entQuantity=tk.Entry(frmEdit, bg='orange', width =10)
        entQuantity.grid(row=3,column=2)

        lblPlace= tk.Label(frmEdit,text='Place Stored',  bg="blue", width = 10, padx = 10,)
        lblPlace.grid(row=4,column=0)

        entPlace=tk.Entry(frmEdit, bg='orange', width =10)
        entPlace.grid(row=5,column=0)


        lblPrice= tk.Label(frmEdit,text='Price',  bg="blue", width = 10, padx = 10,)
        lblPrice.grid(row=4,column=1)

        entPrice=tk.Entry(frmEdit, bg='orange', width =10)
        entPrice.grid(row=5,column=1)

        btnEdit=tk.Button(frmEdit, text='Edit', bg='green', padx=30, width = 10,command = Edit)
        btnEdit.grid(row=6, column=1, pady= 30)


    def removePage():
        def Delete():
            lines = []
            name = entName.get()
            ID = entID.get()
            
            with open('warehouse.csv', "r") as file:
                csvReader = csv.reader(file)
                for row in csvReader:
                    if (row[0]!= name and row[2] !=ID):
                        lines.append(row)
                
                             
            os.remove("warehouse.csv")
            with open('warehouse.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(lines)

            texProduct.delete(1.0, tk.END)
            with open('warehouse.csv', "r") as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    texProduct.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "  -  "
                                  + member[4] + "  -  " +member[5] + "  -  " + member[6] + "  -  " + member[7] +'\n')



        remove = tk.Tk()
        remove.title('Delete Product')
        remove.geometry('400x300')
        remove.configure(bg='blue')

        frmPage = tk.Frame(remove, bg = "blue", width = 600, height = 400)
        frmPage.pack()

    
        lblName=tk.Label(frmPage,text='Name', bg="blue", padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmPage, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        
        lblMid=tk.Label(frmPage,text='', bg="blue", width =1)
        lblMid.grid(row=1,column=1)

        lblID=tk.Label(frmPage,text='Id #',  bg="blue", padx = 10)
        lblID.grid(row=0,column=2)

        entID= tk.Entry(frmPage, bg='orange', width = 10,)
        entID.grid(row=1,column=2)

        btnDelete=tk.Button(frmPage, text='Remove Product', bg='green', padx=30, width = 10,command = Delete )
        btnDelete.grid(row=3, column=1, pady= 30)

        
    

    def addPage():
        def Add():
            name = entName.get()
            Type = entType.get()
            ID = entID.get()
            time = entTime.get()
            provider = entProvide.get()
            quant = entQuantity.get()
            place = entPlace.get()
            Price = entPrice.get()
          

            

            with open('warehouse.csv', "a", newline = '') as file:
                csvWriter = csv.writer(file)
                csvWriter.writerow([name, Type, ID, time, provider, quant, place, Price])
                texProduct.insert(tk.END, name + "  -  " + Type + "  -  "+ ID + "  -  " +time + "  -  " + provider + "  -  "+ quant + "  -  "+ place + "  -  "+ Price + '\n')



                




            

                        

                    

                            
                            
                        
               
           
            
        add = tk.Tk()
        add.title('Add Product')
        add.geometry('600x400')
        add.configure(bg='blue')

        frmAll = tk.Frame(add, bg = "blue", width = 600, height = 400)
        frmAll.pack()

    


        lblName=tk.Label(frmAll,text='Name', bg="blue", width = 10, padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmAll, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        lblID=tk.Label(frmAll,text='Id #',  bg="blue", width = 10, padx = 10)
        lblID.grid(row=0,column=1)

        entID= tk.Entry(frmAll, bg='orange', width = 10,)
        entID.grid(row=1,column=1)

        lblType= tk.Label(frmAll,text='Product Type',  bg="blue", width = 10, padx = 10)
        lblType.grid(row=0,column=2)

        entType=tk.Entry(frmAll, bg='orange', width =10)
        entType.grid(row=1,column=2,)

        lblTime= tk.Label(frmAll,text='Time Stored',  bg="blue", width = 10, padx = 10,)
        lblTime.grid(row=2,column=0)

        entTime=tk.Entry(frmAll, bg='orange', width =10)
        entTime.grid(row=3,column=0)


        lblProvide= tk.Label(frmAll,text='Provider',  bg="blue", width = 10, padx = 10,)
        lblProvide.grid(row=2,column=1)

        entProvide=tk.Entry(frmAll, bg='orange', width =10)
        entProvide.grid(row=3,column=1)

        lblQuantity= tk.Label(frmAll,text='Quantity',  bg="blue", width = 10, padx = 10,)
        lblQuantity.grid(row=2,column=2)

        entQuantity=tk.Entry(frmAll, bg='orange', width =10)
        entQuantity.grid(row=3,column=2)

        lblPlace= tk.Label(frmAll,text='Place Stored',  bg="blue", width = 10, padx = 10,)
        lblPlace.grid(row=4,column=0)

        entPlace=tk.Entry(frmAll, bg='orange', width =10)
        entPlace.grid(row=5,column=0)


        lblPrice= tk.Label(frmAll,text='Price',  bg="blue", width = 10, padx = 10,)
        lblPrice.grid(row=4,column=1)

        entPrice=tk.Entry(frmAll, bg='orange', width =10)
        entPrice.grid(row=5,column=1)

        btnAdd=tk.Button(frmAll, text='Add', bg='green', padx=30, width = 10, command = Add)
        btnAdd.grid(row=6, column=1, pady= 30)

    

        
    def SearchPage():
        def Search():
            name = entName.get()
            ID = entID.get()


            texProduct.delete(1.0, tk.END)
            with open('warehouse.csv','r') as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    if member[0] !=name and member[2] != ID:
                        continue
                    texProduct.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "  -  "+member[3] + "  -  "
                                     + member[4] + "  -  " +member[5] + "  -  " + member[6] + "  -  " + member[7] +'\n')

        search = tk.Tk()
        search.title('Search Product')
        search.geometry('400x300')
        search.configure(bg='blue')

        frmSearch = tk.Frame(search, bg = "blue", width = 600, height = 400)
        frmSearch.pack()

    
        lblName=tk.Label(frmSearch,text='Name', bg="blue", padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmSearch, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        
        lblMid=tk.Label(frmSearch,text='', bg="blue", width =1)
        lblMid.grid(row=1,column=1)

        lblID=tk.Label(frmSearch,text='Id #',  bg="blue", padx = 10)
        lblID.grid(row=0,column=2)

        entID= tk.Entry(frmSearch, bg='orange', width = 10,)
        entID.grid(row=1,column=2)

        btnSearch=tk.Button(frmSearch, text='Search Product', bg='green', padx=30, width = 10,command = Search )
        btnSearch.grid(row=3, column=1, pady= 30)

                


     

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

    btnAdd = tk.Button(rtFrame,text="Add Product", width= 10, height = 2, command =addPage)
    btnAdd.grid(row = 1, column = 2, pady=15)

    btnDel = tk.Button(rtFrame, text="Remove Product", width= 10, height = 2,command =removePage)
    btnDel.grid(row = 2, column =2, pady =15)

    btnEdit = tk.Button(rtFrame, text="Edit Product", width= 10, height = 2,command=editPage)
    btnEdit.grid(row = 3, column =2, pady =15)

    btnSearch = tk.Button(rtFrame, text="Search Product", width= 10, height = 2,command = SearchPage)
    btnSearch.grid(row = 4, column =2, pady =15)

    btnPrint = tk.Button(rtFrame, text="Print", width= 10, height = 2, command = Print)
    btnPrint.grid(row = 5, column =2, pady =15)


    btnBack = tk.Button(rtFrame, text="Back to menu", width= 7, height = 1, command= lambda:[deletePage(), AdminMenu()])
    btnBack.grid(row =6, column =2, pady =15)


    window.mainloop()



    
    
#=============================Admin Main Menu Page===========================================




def AdminMenu():
    def changePage():
        def changeLogin():
            newUser = entnewUser.get()
            newPass = entnewPass.get()

            lines = []
           
            lines = [newUser, newPass]
            
             
                             
            with open('AdminLogin.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(lines)
        

    
    
        change = tk.Tk()
        change.title('Search Product')
        change.geometry('400x300')
        change.configure(bg='blue')

        frmChange = tk.Frame(change, bg = "blue", width = 600, height = 400)
        frmChange.pack()

    
        lblnewUser=tk.Label(frmChange,text='New Username', bg="blue", padx = 10)
        lblnewUser.grid(row=0,column=0)

        entnewUser=tk.Entry(frmChange, bg='orange', width =10,)
        entnewUser.grid(row=1,column=0)

        
        lblMid=tk.Label(frmChange,text='', bg="blue", width =1)
        lblMid.grid(row=1,column=1)

        lblnewPass=tk.Label(frmChange,text='New password',  bg="blue", padx = 10)
        lblnewPass.grid(row=0,column=2)

        entnewPass= tk.Entry(frmChange, bg='orange', width = 10,)
        entnewPass.grid(row=1,column=2)

        btnSearch=tk.Button(frmChange, text='Change Info ', bg='green', padx=30, width = 10,command = changeLogin )
        btnSearch.grid(row=3, column=1, pady= 30)

                
    def deleteMenu():
        adminMenu.destroy()
    

    adminMenu = tk.Tk()
    adminMenu.title("Admin Main Menu")
    adminMenu.geometry('800x500')
    adminMenu.configure(bg = 'light blue')


    lblAdminMenu = tk.Label(adminMenu, text = 'Admin Main Menu', bg = 'light blue', padx = 100)
    lblAdminMenu.grid(row = 0, column = 2)

    btnAdminProducts = tk.Button(adminMenu, text = 'View Products and Product Actions',
                                 bg = 'white', width = 20, padx = 30, command =lambda: [deleteMenu(), AdminProducts()])
    btnAdminProducts.grid(row = 2, column = 1)

    btnBorrowRequests = tk.Button(adminMenu, text = 'View Borrow Requests', bg = 'white', width = 20, padx = 30,
                                  command = lambda: [deleteMenu(),BorrowReqPage()] )
    btnBorrowRequests.grid(row = 4, column = 1)

    btnUsers = tk.Button(adminMenu, text = 'View Users and User Actions', bg = 'white', width = 20, padx = 30, command =
                         lambda:[deleteMenu(),AdminUserPage()])
    btnUsers.grid(row = 2, column = 3)

    btnAdminPass = tk.Button(adminMenu, text = 'Change Admin User and Password', width = 20, bg = 'white', padx = 30, command = changePage)
    btnAdminPass.grid(row = 4, column = 3)

    btnExit = tk.Button(adminMenu, text = 'Log Out', width = 10, bg = 'white', padx = 30, command = lambda: [deleteMenu(), LoginPage()])
    btnExit.grid(row = 6, column = 3)

    adminMenu.mainloop()



 



#=============================User Product Menu ===========================================

def UserProductPage():

    
    def deleteProdPage():
        UserProd.destroy()

    def BorrowPage():
        def deleteBorrowPage():
            Borrow.destroy()

        def BorRequest():
            name = entName.get()
            ID = entID.get()
            amount = entLength.get()

            with open('warehouse.csv', "r") as file:
                csvReader = csv.reader(file)
                for row in csvReader:
                    if (row[0]== name and row[2] ==ID):
                        with open ('borrowrequest.csv', "a", newline ="") as file:
                            csvWriter = csv.writer(file)
                            csvWriter.writerow([name, ID, amount])
                    
            

    

             
            

        Borrow = tk.Tk()
        Borrow.title('Borrow Product')
        Borrow.geometry('400x300')
        Borrow.configure(bg='blue')

        frmBor = tk.Frame(Borrow, bg = "blue", width = 600, height = 400)
        frmBor.pack()

    
        lblName=tk.Label(frmBor,text='Name', bg="white", padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmBor, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        
        lblLength=tk.Label(frmBor,text='How Long?', bg="white",)
        lblLength.grid(row=0,column=1)
        

        entLength=tk.Entry(frmBor, bg='orange', width =10,)
        entLength.grid(row=1,column=1)

        lblID=tk.Label(frmBor,text='Id #',  bg="white", padx = 10)
        lblID.grid(row=0,column=2)

        entID= tk.Entry(frmBor, bg='orange', width = 10,)
        entID.grid(row=1,column=2)

        btnBorrow=tk.Button(frmBor, text='Request to Borrow ', bg='green', padx=30, width = 10,
                            command = lambda : [BorRequest(), deleteBorrowPage()] )
        btnBorrow.grid(row=3, column=1, pady= 30)

        

        Borrow.mainloop
        

    def SearchProd():
        def Search():
            name = entName.get()
            Type = entType.get()
            ID = entID.get()
            time = entTime.get()
            provider = entProvide.get()
            quant = entQuantity.get()
            place = entPlace.get()
            Price = entPrice.get()


            texProduct.delete(1.0, tk.END)
            with open('warehouse.csv','r') as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    if (member[0] !=name and member[2] != ID and member[3] != ID and member[4] != ID and member[5] != ID
                        and member[6] != ID  and member[7] != ID):
                        continue
                    texProduct.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "  -  "+member[3] + "  -  "
                                      + member[4] + "  -  " +member[5] + "  -  " + member[6] + "  -  " + member[7] +'\n')




        
        search = tk.Tk()
        search.title('Search Product')
        search.geometry('400x300')
        search.configure(bg='blue')

        frmSearch = tk.Frame(search, bg = "blue", width = 600, height = 400)
        frmSearch.pack()

    
        lblName=tk.Label(frmSearch,text='Name', bg="blue", padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmSearch, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        
        lblMid=tk.Label(frmSearch,text='', bg="blue", width =1)
        lblMid.grid(row=1,column=1)

        lblID=tk.Label(frmSearch,text='Id #',  bg="blue", padx = 10)
        lblID.grid(row=0,column=2)

        entID= tk.Entry(frmSearch, bg='orange', width = 10,)
        entID.grid(row=1,column=2)

        btnSearch=tk.Button(frmSearch, text='Search Product', bg='green', padx=30, width = 10, command=Search )
        btnSearch.grid(row=3, column=1, pady= 30)

        search.mainloop

                

        


    def FavPage():
        def addFav():
            name = entName.get()
            ID = entID.get()

            with open('warehouse.csv', "r") as file:
                csvReader = csv.reader(file)
                for row in csvReader:
                    if (row[0]== name and row[2] ==ID):
                        with open ('favorites.csv', "a", newline ="") as file:
                            csvWriter = csv.writer(file)
                            csvWriter.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
                            texFavorite.insert(tk.END, row[0]+ "  -  " + row[1] + "  -  " + row[2] + "  -  "+row[3] + "  -  "
                                  + row[4] + "  -  " +row[5] + "  -  " + row[6] + "  -  " + row[7] +'\n')

                            
                            
            
            
        Fav=tk.Tk()
        Fav.title('Favorites')
        Fav.geometry('850x400')
        Fav.configure(bg= 'blue')


        lftFrame = tk.Frame(Fav , width = 500, height = 400, bg ="blue", padx = 40)
        lftFrame.pack(side = tk.LEFT)

        rtFrame = tk.Frame(Fav, width = 350, height = 400, bg = "blue")
        rtFrame.pack(side = tk.LEFT)

              
        lblTitle=tk.Label(lftFrame,text='Favorite List', bg='white', padx=30, width = 10)
        lblTitle.pack()

        texFavorite = tk.Text(lftFrame)
        texFavorite.pack()


        if os.path.exists('favorites.csv')== True:

            texFavorite.delete(1.0, tk.END)
            with open('favorites.csv','r') as file:
                csvReader = csv.reader(file)

                for member in csvReader:
                    texFavorite.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "  -  "+member[3] + "  -  "
                                  + member[4] + "  -  " +member[5] + "  -  " + member[6] + "  -  " + member[7] +'\n')
            



        
    
        lblName=tk.Label(rtFrame,text='Name ', bg='white', padx=30, width = 5)
        lblName.grid(row = 0, column = 0)

        entName= tk.Entry(rtFrame, bg='orange', width = 10,)
        entName.grid(row=1,column=0)

        lblID=tk.Label(rtFrame,text='ID # ', bg='white', padx=30, width = 5)
        lblID.grid(row = 2, column = 0)

        entID= tk.Entry(rtFrame, bg='orange', width = 10,)
        entID.grid(row=3,column=0)

        
        btnAdd = tk.Button(rtFrame,text="Add Product", width= 10, height = 2, command =addFav)
        btnAdd.grid(row = 4, column = 0, pady=15)

        

        Fav.mainloop()
            
        
    UserProd=tk.Tk()
    UserProd.title('User Products and Actions')
    UserProd.geometry('900x500')
    UserProd.configure(bg= 'blue')

    lftFrame = tk.Frame(master = UserProd, width = 700, height = 500, bg ="blue", padx = 40)
    lftFrame.pack(side = tk.LEFT)

    rtFrame = tk.Frame(UserProd, width = 500, height = 500, bg = "blue")
    rtFrame.pack(side = tk.LEFT)

              
    lblName=tk.Label(lftFrame,text='Product List', bg='white', padx=30, width = 10)
    lblName.pack()

    texProduct = tk.Text(lftFrame)
    texProduct.pack()

    if os.path.exists('warehouse.csv')== True:
        texProduct.delete(1.0, tk.END)
        with open('warehouse.csv','r') as file:
                csvReader = csv.reader(file)

                for member in csvReader:
                    texProduct.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "  -  "+member[3] + "  -  "
                                  + member[4] + "  -  " +member[5] + "  -  " + member[6] + "  -  " + member[7] +'\n')
            

    btnAddFav = tk.Button(rtFrame,text="Add Product to Favorites", width= 15, height = 2,command =FavPage)
    btnAddFav.grid(row = 1, column = 2, pady=15)

    btnBorrow = tk.Button(rtFrame, text="Request to Borrow a Product", width= 15, height = 2, command = BorrowPage)
    btnBorrow.grid(row = 2, column =2, pady =15)

    btnSearch = tk.Button(rtFrame, text="Search", width= 15, height = 2,command = SearchProd)
    btnSearch.grid(row = 3, column =2, pady =15)

    btnBack = tk.Button(rtFrame, text="Back to User Menu", width= 13, height = 2,
                        command = lambda:[deleteProdPage(),userMenu()])
    btnBack.grid(row = 4, column =2, pady =15)


#=============================Admin View Borrow Requests Menu ===========================================



def BorrowReqPage():
    def closePage1():
        window.destroy()
    def AcceptPage():
        def closePage():
            Accept.destroy()
        

        def acceptReq():
            length = entLength.get()
            name = entName.get()
            ID = entID.get()
            lines = []

            with open ('accepts.csv', "a", newline = "") as file:
                csvWriter = csv.writer(file)
                csvWriter.writerow([name, ID, length])

            with open('borrowrequest.csv', "r") as file:
                csvReader = csv.reader(file)
                for row in csvReader:
                    if (row[0]!= name and row[1] !=ID and row[2] !=length):
                        lines.append(row)
                
                             
            os.remove("borrowrequest.csv")
            with open('borrowrequest.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(lines)

            texRequest.delete(1.0, tk.END)
            with open('borrowrequest.csv', "r") as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    texRequest.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + '\n')





            


            

            

        Accept = tk.Tk()
        Accept.title('Accept Request')
        Accept.geometry('400x300')
        Accept.configure(bg='blue')

        frmAccept = tk.Frame(Accept, bg = "blue", width = 600, height = 400)
        frmAccept.pack()

    
        lblName=tk.Label(frmAccept,text='Name', bg="blue", padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmAccept, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        
        lblID=tk.Label(frmAccept,text='ID #', bg="blue", )
        lblID.grid(row=0,column=1)

        entID=tk.Entry(frmAccept, bg='orange', width =10,)
        entID.grid(row=1,column=1)

        
        lblLength=tk.Label(frmAccept,text='Time to borrow',  bg="blue", padx = 10)
        lblLength.grid(row=0,column=2)

        entLength= tk.Entry(frmAccept, bg='orange', width = 10,)
        entLength.grid(row=1,column=2)

        btnAccept=tk.Button(frmAccept, text='Accept', bg='green', padx=30, width = 10,
                            command = lambda: [acceptReq(),closePage()])
        btnAccept.grid(row=3, column=1, pady= 30)


    def declinePage():

        def closeDecline():
            decline.destroy()
        

        def declineReq():
            length = entLength.get()
            name = entName.get()
            ID = entID.get()
            lines = []

            with open('borrowrequest.csv', "r") as file:
                csvReader = csv.reader(file)
                for row in csvReader:
                    if (row[0]!= name and row[1] !=ID and row[2] != length):
                        lines.append(row)
                
                             
            os.remove("borrowrequest.csv")
            with open('borrowrequest.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(lines)

            texRequest.delete(1.0, tk.END)
            with open('borrowrequest.csv', "r") as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    texRequest.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + '\n')

            




        decline= tk.Tk()
        decline.title('Delete Product')
        decline.geometry('400x300')
        decline.configure(bg='blue')

        frmPage = tk.Frame(decline, bg = "blue", width = 600, height = 400)
        frmPage.pack()

    
        lblName=tk.Label(frmPage,text='Name', bg="blue", padx = 10)
        lblName.grid(row=0,column=0)

        entName=tk.Entry(frmPage, bg='orange', width =10,)
        entName.grid(row=1,column=0)

        
        lblID=tk.Label(frmPage,text='ID #', bg="blue", )
        lblID.grid(row=0,column=1)

        entID=tk.Entry(frmPage, bg='orange', width =10,)
        entID.grid(row=1,column=1)

        
        lblLength=tk.Label(frmPage,text='Time to borrow',  bg="blue", padx = 10)
        lblLength.grid(row=0,column=2)

        entLength= tk.Entry(frmPage, bg='orange', width = 10,)
        entLength.grid(row=1,column=2)



        btnDelete=tk.Button(frmPage, text='Decline', bg='green', padx=30, width = 10,
                            command = lambda: [declineReq(), closeDecline()] )
        btnDelete.grid(row=3, column=1, pady= 30)

        


        


        
    
    window=tk.Tk()
    window.title('Borrow Request')
    window.geometry('900x500')
    window.configure(bg= 'blue')


    lftFrame = tk.Frame(master = window, width = 700, height = 500, bg ="blue", padx = 40)
    lftFrame.pack(side = tk.LEFT)

    rtFrame = tk.Frame(master = window, width = 500, height = 500, bg = "blue")
    rtFrame.pack(side = tk.LEFT)

              
    lblName=tk.Label(lftFrame,text='Borrow Requests', bg='white', padx=30, width = 10)
    lblName.pack()

    texRequest = tk.Text(lftFrame)
    texRequest.pack()

    if os.path.exists('borrowrequest.csv')== True:
            texRequest.delete(1.0, tk.END)
            with open('borrowrequest.csv','r') as file:
                csvReader = csv.reader(file)

                for member in csvReader:
                    texRequest.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] +'\n')

                    



    btnAccept = tk.Button(rtFrame,text="Accept", width= 10, height = 2, command = AcceptPage)
    btnAccept.grid(row = 1, column = 2, pady=15)

    btnDecline = tk.Button(rtFrame, text="Decline", width= 10, height = 2,command = declinePage)
    btnDecline.grid(row = 2, column =2, pady =15)
 

    btnBack = tk.Button(rtFrame, text="Back to menu", width= 7, height = 1,
                        command = lambda: [closePage1(), AdminMenu()] )
    btnBack.grid(row =3, column =2, pady =15)


    window.mainloop()


#=============================User Main Menu ===========================================
def userMenu():
    def deleteUser():
        UserMenu.destroy()

    def borrowHistoryPage():

        window=tk.Tk()
        window.title('Admin Products and Actions')
        window.geometry('600x400')
        window.configure(bg= 'blue')


        lftFrame = tk.Frame(master = window, width = 600, height = 400, bg ="blue", padx = 40)
        lftFrame.pack(side = tk.LEFT)


              
        lblName=tk.Label(lftFrame,text='Borrow History', bg='white', padx=30, width = 10)
        lblName.pack()

        texProduct = tk.Text(lftFrame)
        texProduct.pack()

        if os.path.exists('accepts.csv')== True:
            texProduct.delete(1.0, tk.END)
            with open('accepts.csv','r') as file:
                csvReader = csv.reader(file)
                for member in csvReader:
                    texProduct.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2]  +'\n')
            


        window.mainloop()
        

    def Favorites():
        def deleteFave():
            Faves.destroy()
            
        Faves=tk.Tk()
        Faves.title('Favorites List')
        Faves.geometry('850x450')
        Faves.configure(bg= 'blue')


        lftFrame = tk.Frame(Faves , width = 850, height = 500, bg ="blue", padx = 40)
        lftFrame.pack()

      
        lblTitle=tk.Label(lftFrame,text='Favorite List', bg='white', padx=30, width = 10)
        lblTitle.pack()
        


        texFavorite = tk.Text(lftFrame)
        texFavorite.pack()

        if os.path.exists('favorites.csv')== True:
            texFavorite.delete(1.0, tk.END)
            with open('favorites.csv','r') as file:
                csvReader = csv.reader(file)

                for member in csvReader:
                    texFavorite.insert(tk.END, member[0]+ "  -  " + member[1] + "  -  " + member[2] + "  -  "+member[3] + "  -  "
                                  + member[4] + "  -  " +member[5] + "  -  " + member[6] + "  -  " + member[7] +'\n')



        btnBack = tk.Button(lftFrame, text="Back to User Menu", width= 13, height = 2,
                        command = lambda:[deleteFave(),userMenu()])
        btnBack.pack(pady =30)

    

   

    UserMenu=tk.Tk()
    UserMenu.title('User Main Menu-- WMS')
    UserMenu.geometry('900x500')
    UserMenu.configure(bg='blue')

    

    ttlName=tk.Label(UserMenu,text='User Main Menu',bg='white',padx=10)
    ttlName.grid(row=0,column=1)


    UserMenu.grid_rowconfigure(1, weight=1)
    UserMenu.grid_columnconfigure(1, weight=1)


    btnProduct=tk.Button(UserMenu,text='View Products and User Product Actions', width=30, height=5,
                         command = lambda:[deleteUser(), UserProductPage()])
    btnProduct.grid(row=1,column=0)

    btnFavorite=tk.Button(UserMenu,text='View Favorites List', width=30, height=5,command = lambda:[deleteUser(),Favorites()])
    btnFavorite.grid(row=1,column=2)

    btnBorrowed=tk.Button(UserMenu,text='View Borrowed Items History', width=30, height=5, command = borrowHistoryPage)
    btnBorrowed.grid(row=2,column=1)

    btnExit=tk.Button(UserMenu,text='Exit',bg='red', width=20, height = 2, command = deleteUser)
    btnExit.grid(row=3,column=2)


    UserMenu.mainloop



LoginPage()
