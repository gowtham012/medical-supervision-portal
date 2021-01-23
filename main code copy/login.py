import tkinter
from mainWindow import menu

#root=login page
#root1=menu
#rootp=patient form

#variables
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
#command for login button
def GET1():
    global userbox,passbox,error
    root = tkinter.Tk()
    root.geometry("650x350")
    root.configure(bg='BLACK')
    headinggg= tkinter.Label(root, text="ADMIN REGISTER PAGE ",bg='black',fg='green',font='Times 25 bold ')
    headingg= tkinter.Label(root, text="NAME ",bg='black',fg='white',font='Times 11 bold ')
    headingg1= tkinter.Label(root, text="Phone no ",bg='black',fg='white',font='Times 11 bold ')
    headingg2= tkinter.Label(root, text="Email ",bg='black',fg='white',font='Times 11 bold ')
    headingg3= tkinter.Label(root, text="UserID ",bg='black',fg='white',font='Times 11 bold ')
    headingg4= tkinter.Label(root, text="Password ",bg='black',fg='white',font='Times 11 bold ')
    login9= tkinter.Button(root, text="SUDMIT",font="arial 10 bold",bg='black',fg='red')
    login9.place(x=170,y=370)
    name = tkinter.Entry(root)
    phoneno = tkinter.Entry(root)
    email = tkinter.Entry(root)
    userid = tkinter.Entry(root)
    password = tkinter.Entry(root)
    headinggg.pack()
    headingg.pack()
    name.pack()
    headingg1.pack()
    phoneno.pack()
    headingg2.pack()
    email.pack()
    headingg3.pack()
    userid.pack()
    headingg4.pack()
    password.pack()
    login9.pack()


   

def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='gowtham' and S2=='1234'):
        menu()
    elif(S1=='hruday' and S2=='4321'):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font="bold")
        error.pack()


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("650x350")
    root.configure(bg='BLACK')
    heading1= tkinter.Label(root, text="STAR ",bg='black',fg='green',font='Times 25 bold ')
    heading2= tkinter.Label(root, text="⚕️ MULTISPECIALITY ⚕️",bg='black',fg='red',font='Times 25 bold ')
    heading3= tkinter.Label(root, text="HOSPITAL",bg='black',fg='blue',font='Times 25 bold')
    heading = tkinter.Label(root, text="⚕️ WELCOME TO MEDICAL SUPERVISION PORTAL ⚕️",bg='black',fg='steelblue',font='herculanum 25 bold italic ')
    heading4= tkinter.Label(root, text="LOGIN ",bg='black',fg='PURPLE',font='Times 25 bold underline')
    username=tkinter.Label(root,text="USERNAME",bg='black',fg='white')
    userbox = tkinter.Entry(root)
    password=tkinter.Label(root,text="PASSWORD",bg='black',fg='white')
    passbox = tkinter.Entry(root,show="*")
    login = tkinter.Button(root, text="LOGIN", command=GET,font="arial 8 bold",bg='black',fg='red')
    login1= tkinter.Button(root, text="REGISTER", command=GET1,font="arial 8 bold",bg='black',fg='red')
    heading1.pack()
    heading2.pack()
    heading3.pack()
    heading.pack()
    heading4.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    login1.pack()
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()

