from Tkinter import *
from tkMessageBox import *
import sqlite3
import os
root = Tk()
root.title('CREDENTIALS')
conn=sqlite3.connect('dbpass')

conn.execute('create table if not exists pswd (id varchar(25), pass varchar(30))')

def pas() :
    l1 = Label(root, text = '')
    l1.place(x = 0, y = 0, height = 300, width = 300)
    z = conn.execute('select id from pswd')
    x = z.fetchall()

    if(x==[]) :
        l2 = Label(root, text = 'Set CREDENTIALS')
        l2.place(x = 100, y = 5)

        e1 = Entry(root)
        e1.place(x = 150, y = 50)
        e1.focus_set()

        l3 = Label(root, text = 'Username')
        l3.place(x = 50, y = 50)

        e2 = Entry(root, show = '*')
        e2.place(x = 150, y = 100)

        l4 = Label(root, text = 'Password')
        l4.place(x = 50, y = 100)

        def insert() :
            conn.execute('insert into pswd values(?,?)', (e1.get(), e2.get()))
            conn.commit()
            os.startfile('main.py')
            root.quit
        b1 = Button(root, text = 'Enter', command = insert)
        b1.place(y = 180, x = 150)   
    if(x!=[]) :
        l5 = Label(root, text = 'Enter Credentials')
        l5.place(x = 100, y = 5)

        e3 = Entry(root)
        e3.place(x = 150, y = 50)

        l6 = Label(root, text = 'Username')
        l6.place(x = 50, y = 50)

        e4 = Entry(root, show = '*')
        e4.place(x = 150, y = 100)

        l7 = Label(root, text = 'Password')
        l7.place(x = 50, y = 100)
  
        def insert() :
            e3.get()
            e4.get()
   
            d = conn.execute('select id, pass from pswd')
            s = d.fetchall()

            if(s[0][0]==v and s[0][1]==w) :
                os.startfile('main.py')
            else :
                l8 = Label(root, text = 'Please check your credentials.')
                l8.place(x = 100, y = 250)
        b2 = Button(root, text = 'Enter', command = insert)
        b2.place(y = 180, x = 130)
  
l9 = Label(root, text = "Author  :  Ayush Gupta\n\nPASSWORD DATABASE MANAGER \n\nEnrollment No.  :  161B059\n")
l9.pack()

root.after(2750, pas)

root.minsize(300, 300)
root.maxsize(421, 421)

root.mainloop()
