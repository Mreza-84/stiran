'''
for change byte format to str we can use :
str.encode("str")
'''
from tkinter import *
import dbm
import pickle
import os

def Login ():
    #Tk
    Sc.destroy()
    Ls = Tk()
    Ls.resizable(0, 0)
    Ls.geometry("500x500")
    Ls.title("STIRAN")
    Ls.configure(background='black')
    Label(Ls,text="Hello!!!\nHere is Login Page!!\nLogin now ! ",fg = "white",bg = "black", 
    font = "tahoma 16 bold italic")
    Label(Ls,text="Name : ",font = "tahoma 16 bold italic",fg = "white"
    ,bg = "black" ).grid(row=0,column=1)
    N = Entry(Ls)
    N.grid(row=0,column=2)
    Ls.mainloop()

    C1 = 0
    C = 5
    try:
        N = input("Username : ")
        F = open((str(N)+".txt"),"r+")
        P = input("Password : ")
        PS = F.readline()
        F.close()
        if str(pickle.dumps(P)) == PS:
            print("Welcome")
        else:
            while C1 != C :
                C1 = C1 + 1
                print("Wrong Password")
                print("Try again")
                P = input("Enter Your Password Again : ")
                if P == PS:
                    break
            print("Try again")
            main()
                    
    except:
        print("There is some thing wrong *___*")
        print("You don't have any account")
        print("Create a new one")
        register()
def register():
    
    if os.path.exists(str(N)+'.txt') == False :
        P = input("Password : ")
        PS = input("Confirm Your Password : ")
        if PS == P :
            F = open((str(N)+".txt"),"w+")
            F.write(str(pickle.dumps(P)))
            F.close()
            print("Register Successfull")
            print("Now login")
            Login()
        else:
            print("Try again")
            register()
    else:
        print("File has alredy exists\nTry again")
        main()
        
        
def main ():
    global Sc
    #TK
    Sc = Tk()
    Sc.resizable(0, 0) 
    
    Sc.geometry("500x500")
    Sc.title("STIRAN")
    Sc.configure(background='black')
    Label(Sc,text="Welcome to STIRAN\nRegister or login ?",fg = "white",bg = "black", 
    font = "tahoma 16 bold italic").pack()
    ######################################
    button = Button(Sc, text='Register',compound = CENTER, width=20,font = "tahoma 16 bold ", bg = 'red',
    command= register)
    button.bind('<Button-1>')
    button.pack()
    ######################################
    button1 = Button(Sc, text='Login',compound = CENTER, width=20,font = "tahoma 16 bold "
    , bg = 'red',command= Login  ) 
    button1.bind('<Button-1>')
    button1.pack()
    ######################################
    Exit =Button(Sc, text='Exit',compound = CENTER, width=20,font = "tahoma 16 bold "
    , bg = 'red',command= Sc.destroy )
    button1.bind('<Button-1>')
    Exit.pack(side = "bottom")

    mainloop()
if __name__ == '__main__':
     main()
        










    
