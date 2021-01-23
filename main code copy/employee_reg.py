import tkinter
import sqlite3
rootE=None
var=None


def inp():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,var
    e1=t1.get()
    e2=t2.get()
    e3=str(var.get())
    e4=t3.get()
    e5=lb.get(tkinter.ACTIVE)
    e6=t4.get()
    e7=t5.get()
    e8=t6.get()
    e9=t7.get()
    conn = sqlite3.connect("MSP.db")
    conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDICAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")

def ex():
    rootE.destroy()

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var
    rootE=tkinter.Tk()
    rootE.title("Employee registration")
    rootE.geometry('400x400')
    rootE.configure(bg='light goldenrod yellow')
    var = tkinter.StringVar(master=rootE)
    H=tkinter.Label(rootE,text="EMPLOYEE REGISTRATION",fg='steelblue',font="Arial 23 bold",bg='light goldenrod yellow')
    H.place(x=50,y=20)
    l1=tkinter.Label(rootE,text="EMPLOYEE ID",fg='black',bg='light goldenrod yellow')
    l1.place(x="50",y="50")
    t1=tkinter.Entry(rootE)
    t1.place(x='170',y='50')
    l2 = tkinter.Label(rootE, text="EMPLOYEE NAME",fg='black',bg='light goldenrod yellow')
    l2.place(x=50,y=80)
    t2 = tkinter.Entry(rootE)
    t2.place(x='170', y='80')
    l3 = tkinter.Label(rootE, text="SEX",fg='black',bg='light goldenrod yellow')
    l3.place(x=50,y=110)
    r1 = tkinter.Radiobutton(rootE, text="MALE", variable=var, value="Male",fg='black',bg='light goldenrod yellow')
    r1.place(x=90, y=110)
    r2 = tkinter.Radiobutton(rootE, text="FEMALE", variable=var, value="Female",fg='black',bg='light goldenrod yellow')
    r2.place(x=160, y=110)
    l4 = tkinter.Label(rootE, text="AGE",fg='black',bg='light goldenrod yellow')
    l4.place(x=50,y=140)
    t3=tkinter.Entry(rootE)
    t3.place(x=100,y=140)
    l5 = tkinter.Label(rootE, text="EMPLOYEE TYPE",fg='black',bg='light goldenrod yellow')
    l5.place(x=50,y=170)
    scrollbar = tkinter.Scrollbar(rootE, width=2,bg='light goldenrod yellow')
    scrollbar.place(x=370, y=140)
    lb = tkinter.Listbox(rootE, selectmode='SINGLE', exportselection=0, height=1, width=15,yscrollcommand = scrollbar.set)
    lb.insert(tkinter.END, "DOCTOR")
    lb.insert(tkinter.END, "NURSE")
    lb.insert(tkinter.END, "RECEPTIONIST")
    lb.place(x=190, y=170)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lb.yview)
    l6=tkinter.Label(rootE,text="SALARY",fg='black',bg='light goldenrod yellow')
    l6.place(x=50,y=200)
    t4=tkinter.Entry(rootE)
    t4.place(x=140,y=200)
    l7 = tkinter.Label(rootE, text="EXPERIENCE",fg='black',bg='light goldenrod yellow')
    l7.place(x=50,y=230)
    t5 = tkinter.Entry(rootE)
    t5.place(x=140,y=230)
    l8 = tkinter.Label(rootE, text="MOBILE NO",fg='black',bg='light goldenrod yellow')
    l8.place(x=50,y=260)
    t6 = tkinter.Entry(rootE)
    t6.place(x=140,y=260)
    l9 = tkinter.Label(rootE, text="EMAIL",fg='black',bg='light goldenrod yellow')
    l9.place(x=50,y=290)
    t7=tkinter.Entry(rootE)
    t7.place(x=140,y=290)
    b1=tkinter.Button(rootE,text="SAVE",command=inp)
    b1.place(x=60,y=320)
    b2=tkinter.Button(rootE,text="DELETE EMPLOYEE",command=delo)
    b2.place(x=140,y=320)
    b3=tkinter.Button(rootE,text="EXIT",command=ex)
    b3.place(x=270,y=320)
    rootE.mainloop()

def delling():
    global d1,de
    de=str(d1.get())
    conn = sqlite3.connect("MSP.db")
    p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
    if (len(p) != 0):
        conn.execute("DELETE from employee where EMP_ID=?", (de,))
        dme = tkinter.Label(rootDE, text="EMPLOYEE DELETED FROM DATABASE", fg="green")
        dme.place(x=20, y=100)
        conn.commit()
    else:
        error = tkinter.Label(rootDE, text="EMPLOYEE DOESN'T EXIST", fg="Red")
        error.place(x=20, y=100)

rootDE=None
def delo():
    global rootDE,d1
    rootDE=tkinter.Tk()
    rootDE.geometry("250x250")
    rootDE.title("EMPLOYEE DELETION")
    rootDE.configure(bg='light goldenrod yellow')
    h1=tkinter.Label(rootDE,text="ENTER EMPLOYEE ID TO DELETE :",fg='black',bg='light goldenrod yellow')
    h1.place(x=20,y=10)
    d1=tkinter.Entry(rootDE)
    d1.place(x=20,y=40)
    B1=tkinter.Button(rootDE,text="DELETE",command=delling)
    B1.place(x=20,y=70)
    rootDE.mainloop()


