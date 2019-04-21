from Tkinter import *
from tkMessageBox import *
import sqlite3
import os
import random
    
root = Tk()
root.title('Password DB Manager')
x = 0
def new_entry():
    window = Toplevel(root)
    window.title('New Entry')
    
    conn = sqlite3.connect('db')
    conn.execute('create table if not exists data(Service varchar(15) primary key, Username varchar(30), Password varchar(15))')
    
    l1 = Label(window, text='Service')
    l1.pack()

    e1 = Entry(window)
    e1.pack()
    e1.focus_set()

    l2 = Label(window, text = 'Username')
    l2.pack()

    e2 = Entry(window)
    e2.pack()

    l3 = Label(window, text = 'Password')
    l3.pack()

    e3 = Entry(window)
    e3.pack()

    def insert():
        conn.execute('insert into data values(?, ?, ?)', (e1.get(), e2.get(), e3.get()))
        conn.commit()
        y = conn.execute('select Service, Username, Password from data')
        print(y.fetchall())
        
    b1 = Button(window, text = 'Add', command = insert)
    b1.pack()

def delete():
    window = Toplevel(root)
    window.title('Delete Record')
    conn = sqlite3.connect('db')

    l4 = Label(window, text = 'Service')
    l4.pack()

    e1 = Entry(window)
    e1.pack()
    e1.focus_set()

    def remove() :
        conn.execute('delete from data where Service=(?)', (e1.get(),))
        conn.commit()
        
        showinfo('Record deleted', 'Record deleted')

    b2 = Button(window, text='Delete', command = remove)
    b2.pack()
    
def fetch() :
    window = Toplevel(root)
    window.title('Fetch Record')

    conn = sqlite3.connect('db')

    l5 = Label(window, text = 'Service')
    l5.pack()

    e1 = Entry(window)
    e1.pack()
    e1.focus_set()
    
    def fetch_rec() :
        z = conn.execute('select Service, Username, Password from data where Service = ?', (e1.get(), ))
        print(z.fetchall())
        
    b3 = Button(window, text = 'Fetch record', command = fetch_rec)
    b3.pack()

def modify() :
    window = Toplevel(root)
    window.title('Modify Record')

    conn = sqlite3.connect('db')

    l6 = Label(window, text = 'Service')
    l6.pack()

    e1 = Entry(window)
    e1.pack()
    e1.focus_set()

    def service():
        global x   

        z = conn.execute('select Service from data where Service=?', (e1.get(), ))
        x = z.fetchall()

        print(x)

    a = IntVar()
    b = IntVar()

    def modify_rec() :
        service()
        twindow = Toplevel(window)
        conn = sqlite3.connect('db')
        window.quit

        if(a.get()==5 and b.get()!=3) :
            global x

            l7 = Label(twindow, text = 'Username')
            l7.pack()

            e1 = Entry(twindow)
            e1.pack()
            e1.focus_set()

            def upd():
                global x

                conn.execute('update data set Username = ? where Service = ?',(e1.get(), x[0][0]))
                conn.commit()

            b4 = Button(twindow, text='Insert',command = upd)
            b4.pack()

        if(b.get()==3 and a.get()!=5) :
            global x

            l8 = Label(twindow, text = 'Password')
            l8.pack()

            e1 = Entry(twindow)
            e1.pack()
            e1.focus_set()

            def upd():
                global x

                conn.execute('update data set Password = ? where Service = ?',(e1.get(), x[0][0]))
                conn.commit()

            b5 = Button(twindow, text = 'Insert',command = upd)
            b5.pack()

        if(b.get()==3 and a.get()==5) :
            global x

            l9 = Label(twindow, text = 'USERNAME')
            l9.pack()

            e1 = Entry(twindow)
            e1.pack()
            e1.focus_set()

            l10 = Label(twindow, text = 'PASSWORD')
            l10.pack()

            e2 = Entry(twindow)
            e2.pack()
            e2.focus_set()

            def upd():
                global x

                conn.execute('update data set Username = ?, Password = ? where Service = ?',(e1.get(), e2.get(), x[0][0]))
                conn.commit()

            b6 = Button(twindow,text = 'Insert', command = upd)
            b6.pack()
            
    Checkbutton(window, text = 'Username', variable = a, onvalue = 5).pack()
    Checkbutton(window, text = 'Password', variable = b, onvalue = 3).pack()

    b7 = Button(window, text = 'Modify', command = modify_rec)
    b7.pack()

def maspass() :
    window = Toplevel(root)

    conn = sqlite3.connect('dbpass')

    l11 = Label(window, text = 'New Password')
    l11.pack()

    e1 = Entry(window)
    e1.pack()
    e1.focus_set()

    def change_pass():
        conn.execute('update pswd set pass = ?',(e1.get(), ))
        z = conn.execute('select id,pass from pswd')
        conn.commit()

        print(z.fetchall())

        showinfo('', 'Password has been changed')    

    b8 = Button(window, text = 'Confirm', command = change_pass)
    b8.pack()

def gen_pass() : 
    root = Tk()
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    p =  "".join(random.sample(s, passlen))
    t = Text(root)
    t.pack()
    t.insert('1.0', p)
    
b9 = Button(root, text='New Entry', command = new_entry)
b9.grid(row=0, column=0)
b10 = Button(root, text='Modify Record', command = modify)
b10.grid(row = 0, column=1)
b11 = Button(root, text='Delete Record', command = delete)
b11.grid(row=0, column=2)
b12 = Button(root, text='Fetch Record', command = fetch)
b12.grid(row = 0, column=3)
b13 = Button(root, text='Generate a Password for me', command = gen_pass)
b13.grid(row=1, column=1)
b14 = Button(root, text='Change Master Password', command = maspass)
b14.grid(row=1, column=2)

root.mainloop()
