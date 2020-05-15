from tkinter import *
from tkinter import ttk
import pymysql as db
from tkinter import messagebox
Adminwindow=Tk()
Adminwindow.title("ENQUIRY MANAGEMENT SYSTEM")
wwidth=700
wheight=600
swidth=Adminwindow.winfo_screenwidth()
sheight=Adminwindow.winfo_screenheight()
x1=swidth/2-wwidth/2
y1=sheight/2-wheight/2                 #
Adminwindow.geometry("%dx%d+%d+%d"%(wwidth,wheight,x1,y1))
Adminwindow.resizable(width=0,height=0)
t1=StringVar()
t2=StringVar()

def logged():

	# if q1 == True:
		r1 = t1.get()
		r2 = t2.get()
		query = "select * from idpass where user_name='%s' and password='%s'"% (r1,r2)
		con = db.connect("localhost", "root", "", "match")

		cur = con.cursor()
		cur.execute(query)
		count = cur.rowcount
		if count == 0:
			messagebox.showerror('ERROR', 'Incorrect Username or Password')
		else:
			messagebox.showinfo('info', 'Successfully login ')
			Adminwindow.destroy()
			import Menu
		cur.close()
		con.close()

f1=Frame(Adminwindow,bd=10,bg="#A9A9A9",height=600,width=700)
f1.pack(fill=BOTH)

l1=Label(f1,text="ADMIN LOGIN",fg="#F5F5F5",bg="#A9A9A9",padx=10,font=("Algerian",25))
l1.place(x=250,y=25)

l2=Label(f1,text="Username",fg="#F5F5F5",bg="#A9A9A9",font=("Algerian",15))
l2.place(x=188,y=100)
e1=Entry(f1,bg="#F5F5F5",fg="#202321",width=35,bd=2,font=(18),textvariable=t1)
e1.place(x=190,y=130)

l3=Label(f1,text="Password",fg="#F5F5F5",bg="#A9A9A9",font=("Algerian",15))
l3.place(x=188,y=160)
e2=Entry(f1,show="#",bg="#F5F5F5",fg="#202321",width=35,bd=2,font=(18),textvariable=t2)
e2.place(x=188,y=190)

b1=Button(f1,text="login",fg="#F5F5F5",width=39,bg="#A9A9A9",font=("Algerian",10),command=logged)
b1.place(x=188,y=240)

Adminwindow.mainloop()