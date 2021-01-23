import tkinter

from mainWindow import menu
import sqlite3
conm=sqlite3.connect("MSP.DB")
cur = conm.cursor()

root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None


def GET():

    S1=userbox.get()
    S2=passbox.get()
    cur.execute("SELECT * FROM REG WHERE NAME=? AND Password=?", (S1,S2))
    info = cur.fetchone()

    try:
        if info[0] == S1 and info[4] == S2:
            menu()
            conm.commit()


    except:
        tkinter.messagebox.showwarning("MEDICAL DATABASE SYSTEM","Wrong Id / Password \n TRY AGAIN")
      



def REG():
    global name, phoneno, email,userid,password
    root = tkinter.Tk()
    root.geometry("650x350")
    root.configure(bg='orange')
    root.title("admin registration ")
    headinggg = tkinter.Label(root, text="ADMIN REGISTER PAGE ", bg='orange', fg='green', font='Times 25 bold ')
    headingg = tkinter.Label(root, text="NAME ", bg='orange', fg='black', font='Times 11 bold ')
    headingg1 = tkinter.Label(root, text="Phone no ", bg='orange', fg='black', font='Times 11 bold ')
    headingg2 = tkinter.Label(root, text="Email ", bg='orange', fg='black', font='Times 11 bold ')
    headingg3 = tkinter.Label(root, text="UserID ", bg='orange', fg='black', font='Times 11 bold ')
    headingg4 = tkinter.Label(root, text="Password ", bg='orange', fg='black', font='Times 11 bold ')
    login9 = tkinter.Button(root, text="SUDMIT", font="arial 10 bold", bg='black',command=MOON, fg='red' )
    login2 = tkinter.Button(root, text="exit", font="arial 10 bold", bg='black',command=quit, fg='red' )
    login9.place(x=170, y=400)
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
    login2.pack()



def MOON():
    S1 = name.get()
    S2 = password.get()
    S3=phoneno.get()
    S4=email.get()
    S5=userid.get()
    print(S1,S2)
    cur.execute("SELECT * FROM REG WHERE NAME=?", (S1,))
    info = cur.fetchone()
    print(info)
    try:
        if info[0] == S1:
            tkinter.messagebox.showwarning('msp'," Id / Password Already Exist \n TRY AGAIN")

    except:
        conm.commit()
        sql = ('''INSERT INTO REG (NAME,P_no,E_mail,UID,Password) VALUES(?,?,?,?,?)''')
        cur.execute(sql, (S1,S3,S4,S5,S2))
        conm.commit()
        tkinter.messagebox.showinfo('msp'," Successfully Created  \n TRY LOGIN")






def Entry():
    global userbox, passbox, login, topframe, bottomframe, image_1
    root = tkinter.Tk()
    root.geometry("950x450")
    root.configure(bg='pink')
    heading1 = tkinter.Label(root, text="STAR ", bg='pink', fg='green', font='Times 25 bold ')
    heading2 = tkinter.Label(root, text="⚕ MULTISPECIALITY ⚕", bg='pink', fg='red', font='Times 25 bold ')
    heading3 = tkinter.Label(root, text="HOSPITAL", bg='pink', fg='blue', font='Times 25 bold')
    heading = tkinter.Label(root, text="⚕ WELCOME TO MEDICAL SUPERVISION PORTAL ⚕", bg='pink', fg='steelblue',
                            font='herculanum 25 bold italic ')
    heading4 = tkinter.Label(root, text="LOGIN ", bg='pink', fg='PURPLE', font='Times 25 bold underline')
    username = tkinter.Label(root, text="USERNAME", bg='pink', fg='black')
    userbox = tkinter.Entry(root)
    password = tkinter.Label(root, text="PASSWORD", bg='pink', fg='black')
    passbox = tkinter.Entry(root, show="*")
    login = tkinter.Button(root, text="LOGIN", command=GET, font="arial 8 bold", bg='pink', fg='red')
    login1 = tkinter.Button(root, text="REGISTER", command=REG, font="arial 8 bold", bg='pink', fg='red')
    login1.place(x=170,y=300)
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