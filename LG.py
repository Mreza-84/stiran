'''
Login or regist
'''
import hashlib 
from tkinter import *
import dbm
import pickle
import os
def Login ():
    #

    C1 = 0
    C = 5
    try:
        N = input("Username : ")
        F = open((str(N)+".txt"),"r+")
        P = input("Password : ")
        PS = F.readline()
        F.close()
        if (hashlib.sha224(P).hexdigest()) == PS:
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
    N = input("Username : ")
    if os.path.exists(str(N)+'.txt') == False :
        P = input("Password : ")
        PS = input("Confirm Your Password : ")
        if PS == P :
            F = open((str(N)+".txt"),"w+")
            F.write(hashlib.sha224(P).hexdigest())
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
    #TK
    LR = input("login or register ? ")
    if LR == 'register':
        register()
    elif LR == 'login':
        Login()
    else:
        print("Try again")
        main()
    mainloop()
if __name__ == '__main__':
     main()
        
        










    
