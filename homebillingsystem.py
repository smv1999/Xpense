import cx_Oracle
import os
import time
from tkinter import *
con=cx_Oracle.connect("system/smv")
creds = 'tempfile1.temp'
cur=con.cursor()
#cur.execute("create table home(sno int,pur_date varchar(20),item_particulars varchar(40),price int)")
def FSSignup(nameE,pwordE):
    with open(creds, 'w') as f: 
        f.write(nameE) 
        f.write('\n') 
        f.write(pwordE) 
        f.close()
    roots = Tk() 
    roots.destroy()
    if os.path.isfile(creds):
        login()

def login():
    global nameEL
    global pwordEL
    global l
    l=Tk()

    l.title("LOGIN PAGE")
    l.geometry("250x170")
    intruction = Label(l, text='Please Login\n') 
    intruction.grid(sticky=E) 
    nameL = Label(l, text='Username: ',borderwidth=2,relief="groove",fg="steel blue",font=('arial',10,'bold')) 
    pwordL = Label(l, text='Password: ',borderwidth=2,relief="groove",fg="steel blue",font=('arial',10,'bold')) 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(l,bd=11) 
    pwordEL = Entry(l, show='*',bd=11)
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(l, text='Login', command=CheckLogin)
    loginB.grid(columnspan=2, sticky=W)
    
    rmuser = Button(l, text='Delete User', fg='red', command=DelUser)
    rmuser.grid(columnspan=2, sticky=W)
    l.mainloop()
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip() 
 
    if nameEL.get() == uname and pwordEL.get() == pword:
        r = Tk()
        r.configure(background='green')
        r.title('Welcome, Jayanthi ')
        r.geometry('150x50')
        rlbl = Label(r, text='\n Login Successful!')
        rlbl.pack()
        r.mainloop()
        
        
        
       
    else:
        r = Tk()
        r.configure(background='red')
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login',borderwidth=2,relief="sunken")
        rlbl.pack()
        r.mainloop()
        exit()    
def DelUser():
    os.remove(creds) 
    l.destroy()
def function():
    FSSignup(nameE,wordE)

def mainbill():
    global root
    root=Tk()
    root.config(bg="grey")
    root.title("HOME BILLING SYSTEM")
    root.geometry("500x198+0+0")
    frame=Frame(root,bg="green",relief="raise")
    frame.pack(side=TOP,fill=BOTH)
    btn1= Button(frame,text="Proceed to Login...",command=function,padx=20)
    btn1.pack(pady=20,padx=20)
    frame3=Frame(root,bg="green",relief="raise")
    frame3.pack(side=BOTTOM,fill=BOTH)
    bt=Button(frame3,text="Details",command=input_details,padx=20)
    bt.pack(pady=20,padx=20)
    bt3=Button(frame3,text="Exit",command=root.destroy,padx=20)
    bt3.pack(pady=20,padx=20)
    root.mainloop()
    #frame.destroy()
def input_details():
    global v1,v2,v3,v4,s,p,i,pr,w2
    s=IntVar()
    p=StringVar()
    i=StringVar()
    pr=IntVar()
    #frame2=Frame(root,bg="green")
    #frame2.pack(side=RIGHT,fill=BOTH)
    w2=Tk()
    w2.title("Billing")
    w2.config(bg="grey")
    w2.geometry("590x320")
    
    #frame4.grid(side=BOTTOM,fill=BOTH)
    frame3=Frame(w2,bg="red")
    frame3.grid(row=0,sticky="nw")
    intruction1 = Label(frame3, text='Please Fill Details\n',bg="red")
    intruction1.grid(sticky=E) 
    s_no = Label(frame3, text='S.no: ',borderwidth=2,relief="groove",fg="steel blue",font=('arial',10,'bold'))
    pur_date = Label(frame3, text='Purchase Date: ',borderwidth=2,relief="groove",fg="steel blue",font=('arial',10,'bold'))
    item_name= Label(frame3, text='Item Name/Expense name: ',borderwidth=2,relief="groove",fg="steel blue",font=('arial',10,'bold'))
    price = Label(frame3, text='Price: ',borderwidth=2,relief="groove",fg="steel blue",font=('arial',10,'bold'))
    s_no.grid(row=1, sticky=W)
    pur_date.grid(row=2, sticky=W)
    item_name.grid(row=3, sticky=W)
    price.grid(row=4, sticky=W)
    v1=Entry(frame3,textvariable=s,font=('arial',9,'bold'),bd=27)
    v2=Entry(frame3,textvariable=p,font=('arial',9,'bold'),bd=27)
    v3=Entry(frame3,textvariable=i,font=('arial',9,'bold'),bd=27)
    v4=Entry(frame3,textvariable=pr,font=('arial',9,'bold'),bd=27)
    v1.grid(row=1, column=1)
    v2.grid(row=2, column=1)
    v3.grid(row=3, column=1)
    v4.grid(row=4, column=1)
    frame4=Frame(w2,bg="steel blue")
    frame4.grid(row=0,column=2,sticky="nw")
    bn=Button(frame4,text="save&next",command=save,padx=20)
    bn.pack(pady=20,padx=20)
    bn1=Button(frame4,text="Show Expense Details",command=records1,padx=20)
    bn1.pack(pady=20,padx=20)
    bn2=Button(frame4,text="Expenses of particular month",command=rcd,padx=20)
    bn2.pack(pady=20,padx=20)
    bn3=Button(frame4,text="search for Expense",command=search,padx=20)
    bn3.pack(pady=20,padx=20)
    bn4=Button(frame4,text="Exit",command=w2.destroy,padx=20)
    bn4.pack(pady=20,padx=20)
    w2.mainloop()
def records1():
    w3=Tk()
    w3.title("Expense Details")
    w3.config(bg="powder blue")
    w3.geometry("1000x500")
    snoLabel = Label(w3, text="S.no", width=10,bg="steel blue",borderwidth=2,relief="raised")
    snoLabel.grid(row=0, column=0)
    pdateLabel = Label(w3, text="Purchase date", width=10,bg="steel blue",borderwidth=2,relief="raised")
    pdateLabel.grid(row=0, column=1)
    itemLabel = Label(w3, text="Expense", width=10,bg="steel blue",borderwidth=2,relief="raised")
    itemLabel.grid(row=0, column=2)
    pLabel = Label(w3, text="Price", width=10,bg="steel blue",borderwidth=2,relief="raised")
    pLabel.grid(row=0, column=3)
    sLabel = Label(w3, text="Total Amount", width=10,bg="steel blue",borderwidth=2,relief="raised")
    sLabel.grid(row=0, column=4)
    data = readfromdatabase1()
    dt1=db1()
    for index, dat in enumerate(data):
        Label(w3, text=dat[0],bg="powder blue",borderwidth=2).grid(row=index+1, column=0)
        Label(w3, text=dat[1],bg="powder blue",borderwidth=2).grid(row=index+1, column=1)
        Label(w3, text=dat[2],bg="powder blue",borderwidth=2).grid(row=index+1, column=2)
        Label(w3, text=dat[3],bg="powder blue",borderwidth=2).grid(row=index+1, column=3)
    for ix,dt in enumerate(dt1):
        Label(w3, text=dt[0],bg="powder blue",borderwidth=2).grid(row=ix+1, column=4)
def records2():
    w3=Tk()
    w3.title("Expense Details")
    w3.config(bg="powder blue")
    w3.geometry("1000x500")
    snoLabel = Label(w3, text="S.no", width=10,bg="steel blue",borderwidth=2,relief="raised")
    snoLabel.grid(row=0, column=0)
    pdateLabel = Label(w3, text="Purchase date", width=10,bg="steel blue",borderwidth=2,relief="raised")
    pdateLabel.grid(row=0, column=1)
    itemLabel = Label(w3, text="Expense", width=10,bg="steel blue",borderwidth=2,relief="raised")
    itemLabel.grid(row=0, column=2)
    pLabel = Label(w3, text="Price", width=10,bg="steel blue",borderwidth=2,relief="raised")
    pLabel.grid(row=0, column=3)
    sLabel = Label(w3, text="Total Amount", width=10,bg="steel blue",borderwidth=2,relief="raised")
    sLabel.grid(row=0, column=4)
    data = readfromdatabase2()
    dt2=db2()
    time.sleep(7)
    for index, dat in enumerate(data):
        Label(w3, text=dat[0],bg="powder blue",borderwidth=2).grid(row=index+1, column=0)
        Label(w3, text=dat[1],bg="powder blue",borderwidth=2).grid(row=index+1, column=1)
        Label(w3, text=dat[2],bg="powder blue",borderwidth=2).grid(row=index+1, column=2)
        Label(w3, text=dat[3],bg="powder blue",borderwidth=2).grid(row=index+1, column=3)
    for ix,dt in enumerate(dt2):
        Label(w3, text=dt[0],bg="powder blue",borderwidth=2).grid(row=ix+1, column=4)
    
def rcd():
    global e1,entry1
    e1=StringVar()
    w4=Tk()
    w4.title("Expenses of a Particular Month")
    w4.config(bg="powder blue")
    w4.geometry("200x200")
    frame6=Frame(w4,bg="steel blue")
    frame6.grid(row=0,sticky="nw")
    Month = Label(frame6, text='Month: ',borderwidth=2,relief="groove",fg="steel blue",font=('arial',10,'bold'))
    Month.grid(row=1, sticky=W)
    entry1=Entry(frame6,textvariable=e1,font=('arial',9,'bold'),bd=12)
    entry1.grid(row=1, column=1)
    frame7=Frame(w4,bg="steel blue")
    frame7.grid(row=1,sticky="nw")
    bttn=Button(frame7,text="OK",command=records2,padx=20)
    bttn.pack(pady=20,padx=20)
    bn3=Button(frame7,text="Exit",command=w4.destroy,padx=20)
    bn3.pack(pady=20,padx=20)

def records3():
    w3=Tk()
    w3.title("Expense Details")
    w3.config(bg="powder blue")
    w3.geometry("1000x500")
    snoLabel = Label(w3, text="S.no", width=10,bg="steel blue",borderwidth=2,relief="raised")
    snoLabel.grid(row=0, column=0)
    pdateLabel = Label(w3, text="Purchase date", width=10,bg="steel blue",borderwidth=2,relief="raised")
    pdateLabel.grid(row=0, column=1)
    itemLabel = Label(w3, text="Expense", width=10,bg="steel blue",borderwidth=2,relief="raised")
    itemLabel.grid(row=0, column=2)
    pLabel = Label(w3, text="Price", width=10,bg="steel blue",borderwidth=2,relief="raised")
    pLabel.grid(row=0, column=3)
    sLabel = Label(w3, text="Total Amount", width=10,bg="steel blue",borderwidth=2,relief="raised")
    sLabel.grid(row=0, column=4)
    data = readfromdatabase3()
    dt3=db3()
    for index, dat in enumerate(data):
        
        Label(w3, text=dat[0],bg="powder blue",borderwidth=2).grid(row=index+1, column=0)
        Label(w3, text=dat[1],bg="powder blue",borderwidth=2).grid(row=index+1, column=1)
        Label(w3, text=dat[2],bg="powder blue",borderwidth=2).grid(row=index+1, column=2)
        Label(w3, text=dat[3],bg="powder blue",borderwidth=2).grid(row=index+1, column=3)
    for ix,dt in enumerate(dt3):
        Label(w3, text=dt[0],bg="powder blue",borderwidth=2).grid(row=ix+1, column=4)
    
def search():
    global e2,entry2
    e2=StringVar()
    w5=Tk()
    w5.title("Search for an expense")
    w5.config(bg="powder blue")
    w5.geometry("200x200")
    frame8=Frame(w5,bg="steel blue")
    frame8.grid(row=0,sticky="nw")
    Month = Label(frame8, text='Expense: ',borderwidth=2,relief="groove",fg="steel blue",font=('arial',10,'bold'))
    Month.grid(row=1, sticky=W)
    entry2=Entry(frame8,textvariable=e2,font=('arial',9,'bold'),bd=12)
    entry2.grid(row=1, column=1)
    frame9=Frame(w5,bg="steel blue")
    frame9.grid(row=1,sticky="nw")
    bttn=Button(frame9,text="OK",command=records3,padx=20)
    bttn.pack(pady=20,padx=20)
    bn3=Button(frame9,text="Exit",command=w5.destroy,padx=20)
    bn3.pack(pady=20,padx=20)    
def readfromdatabase1():
        
        cur.execute("SELECT * FROM home")
        return cur.fetchall()    
def readfromdatabase2():
        q="%"+"/"+entry1.get()+"/"+"%"
        cur.execute("SELECT * FROM home where pur_date like '%s'"%(q))
        return cur.fetchall()    
def readfromdatabase3():
        q2="%"+entry2.get()+"%"
        cur.execute("SELECT * FROM home where item_particulars like '%s'"%(q2))
        return cur.fetchall()    
def db1():
    cur.execute("select sum(price) from home")
    return cur.fetchall()
def db2():
    q1="%"+"/"+entry1.get()+"/"+"%"
    cur.execute("select sum(price) from home where pur_date like '%s'"%(q1))
    l=cur.fetchall()
    if(l[0][0]>20000):
        high()    
    return l
def db3():
    q3="%"+entry2.get()+"%"
    cur.execute("select sum(price) from home where item_particulars like '%s'"%(q3))
    return cur.fetchall()
def high():
    h=Tk()
    h.title("ALERT!!!")
    h.config(bg="grey")
    hLabel = Label(h, text="Expenses going too high!", width=20,bg="steel blue",borderwidth=2,relief="raised")
    hLabel.grid(row=1, column=4)
def Reset():
    v1.delete(0,'end')
    v2.delete(0,'end')
    v3.delete(0,'end')
    v4.delete(0,'end')
def save():
    cur.execute("insert into home(sno,pur_date,item_particulars,price) values(%d,'%s','%s',%d)"%(int(v1.get()),v2.get(),v3.get(),int(v4.get())))
    con.commit()
    Reset()


   
global nameE 
global wordE
nameE = 'jayanthi'
wordE = 'jayanthi'
con.commit()
mainbill()

#FSSignup(nameE,wordE)
#https://stackoverflow.com/questions/36590476/taking-data-from-a-database-and-putting-into-a-table-in-a-gui



