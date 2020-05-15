from tkinter import *
from tkinter import *
from tkinter import ttk
import pymysql as db
import time
from datetime import date
from tkinter import messagebox
Menuwindow=Tk()
Menuwindow.title("ENQUIRY MAMAGEMENT SYSTEM")
wwidth=700
wheight=600
swidth=Menuwindow.winfo_screenwidth()
sheight=Menuwindow.winfo_screenheight()
print(swidth)
print(sheight)

x1=swidth/2-wwidth/2
y1=sheight/2-wheight/2                 #
Menuwindow.geometry("%dx%d+%d+%d"%(wwidth,wheight,x1,y1))
Menuwindow.resizable(width=0,height=0)
g7=StringVar()
g8=StringVar()
def searchdetail():
    r9 = g7.get()
    r10 =g8.get()
    print(r9,r10)
    query="SELECT * FROM `detail` WHERE %s = '%s'" %(r9,r10)
    # query = "select * from detail where '%s'='%s'" %(r9,r10)
    con = db.connect("localhost", "root", "", "record")

    cur = con.cursor()
    cur.execute(query)
    count = cur.rowcount
    if count == 0:
        messagebox.showerror('ERROR', 'Incorrect detail')
    else:
        # toplist = Toplevel()
        # toplist.title("ENQUIRY MANAGEMANT SYSTEM")
        # toplist.geometry("1366x768+0+10")
        # TableMargin = Frame(toplist, height="300", width="700")
        # TableMargin.pack()
        topdel=Toplevel()
        TableMargin = Frame(topdel, height="300", width="700")
        TableMargin.pack()

        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"), height=100,
                            yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('a', text="S_No", anchor=W)
        tree.heading('b', text="Name", anchor=W)
        tree.heading('c', text="Gender", anchor=W)
        tree.heading('d', text="Address", anchor=W)
        tree.heading('e', text="District", anchor=W)
        tree.heading('f', text="Contact_No", anchor=W)
        tree.heading('g', text="Email_id", anchor=W)
        tree.heading('h', text="course", anchor=W)
        tree.heading('i', text="question", anchor=W)
        tree.heading('j', text="Date", anchor=W)

        tree.column('#0', minwidth=0, width=0)
        tree.column('#1', minwidth=0, width=50)
        tree.column('#2', minwidth=0, width=80)
        tree.column('#3', minwidth=0, width=120)
        tree.column('#4', minwidth=0, width=150)
        tree.column('#5', minwidth=0, width=180)
        tree.column('#6', minwidth=0, width=190)
        tree.column('#7', minwidth=0, width=200)
        tree.column('#8', minwidth=0, width=210)
        tree.column('#9', minwidth=0, width=220)

        tree.pack()
        # table code end
        query = "SELECT * FROM `detail` WHERE %s = '%s'" % (r9, r10)
        # query = "select * from detail where '%s'='%s'" %(r9,r10)

        con = db.connect("localhost", "root", "", "record")

        cur = con.cursor()
        cur.execute(query)
        row = cur.fetchone()
        while row is not None:
            tree.insert('', 'end', values=(row))
            row = cur.fetchone()

        cur.close()
        con.close()


def openentry():
    global date
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")

    topentry = Toplevel()
    topentry.title("ENQUIRY MANAGEMANT SYSTEM")
    topentry.geometry("600x650+550+10")
    topentry.resizable(0,0)
    v1 = StringVar()
    aa = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    v5 = StringVar()
    ab = StringVar()
    v7 = StringVar()
    v8=StringVar()
    def insertdb():
        q1 = messagebox.askyesno("question", "are you sure to insert record")
        if q1 == True:
            print(aa.get())
            r1 = v1.get()
            r2 = aa.get()
            r3 = v3.get()
            r4 = v4.get()
            r5 = v5.get()
            r6 = ab.get()
            r7 = v7.get()
            r8 = v8.get()
            query = "INSERT INTO detail(Name,Gender,Address,District,Contact_No,Email_id,course,question,Date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            r1, r2, r3,r8, r4, r5, r6, r7,today)

            con = db.connect("localhost", "root", "", "record")
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            v1.set("")
            aa.set("")
            v3.set("")
            v4.set("")
            v5.set("")
            ab.set("")
            v7.set("")
            v8.set("")
            messagebox.showinfo("info", "Record insertion successfull")
            cur.close()
            con.close()

    f1 = Frame(topentry, height=sheight, width=650, bg="#FFFFFF")  # ,bg="#46A7FC"
    # f1.place(relx=0.15, rely=0)
    f1.pack()
    date = Label(f1, text=d1, font=('times', 20, 'bold'), bg='yellow')
    date.place(x=460, y=0)

    l1 = Label(f1, text="Registration form", font=("Algerian", 24), bg="#FFFFFF")
    l1.place(x=130, y=0)
    l2 = Label(f1, text="Student's Name", font="24", width=15, bg="#FFFFFF")  # E2=Entry(f1,text=" Name",font="24",textvariable=v1)
    l2.place(x=50, y=80)
    E2 = Entry(f1, text=" Name", font="24", textvariable=v1)
    # E2.place(relx=0.5,rely=0.5)
    E2.place(x=200, y=80)

    l3 = Label(f1, text="Gender", font="24", width=15, bg="#FFFFFF")
    l3.place(x=50, y=120)
    R1 = Radiobutton(f1, font=('Verdana', 9), text="male", value="male", variable=aa, bg="#FFFFFF")
    R1.place(x=200, y=120)
    R2 = Radiobutton(f1, font=('Verdana', 9), text="female", value="female ", variable=aa, bg="#FFFFFF")
    R2.place(x=270, y=120)

    l4 = Label(f1, text="Address", font="24", width=15, bg="#FFFFFF")
    l4.place(x=50, y=150)
    E4 = Entry(f1, text="Address", font="24", textvariable=v3)
    E4.place(x=200, y=150)

    l4 = Label(f1, text="District", font="24", width=15, bg="#FFFFFF")
    l4.place(x=50, y=180)
    E4 = Entry(f1, text="district", font="24", textvariable=v8)
    E4.place(x=200, y=180)

    l5 = Label(f1, text="Contact_No", font="24", width=15, bg="#FFFFFF")
    l5.place(x=50, y=210)
    E5 = Entry(f1, text="Contact_No", font="24", textvariable=v4)
    E5.place(x=200, y=210)

    l7 = Label(f1, text="Email_id", font="24", width=15, bg="#FFFFFF")
    l7.place(x=50, y=240)
    E7 = Entry(f1, text="Email_id", font="24", textvariable=v5)
    E7.place(x=200, y=240)

    l6 = Label(f1, text="course", font="24", width=15, bg="#FFFFFF")
    l6.place(x=50, y=270)
    R1 = Radiobutton(f1, font=('Verdana', 9), text="PY", value="PYTHON", variable=ab, bg="#FFFFFF")
    R1.place(x=200, y=270)
    R2 = Radiobutton(f1, font=('Verdana', 9), text="JA", value="JAVA ", variable=ab, bg="#FFFFFF")
    R2.place(x=250, y=270)
    R2 = Radiobutton(f1, font=('Verdana', 9), text="C#", value="C# ", variable=ab, bg="#FFFFFF")
    R2.place(x=300, y=270)
    R2 = Radiobutton(f1, font=('Verdana', 9), text="ANDROID", value="ANDROID", variable=ab, bg="#FFFFFF")
    R2.place(x=350, y=270)


    l3 = Label(f1, text="Question", font="24", width=15, bg="#FFFFFF")  # fg="#E0620A"
    l3.place(x=50, y=300)
    E3 = Entry(f1, text="Question", font="24", textvariable=v7)
    E3.place(x=200, y=300)

    B2 = Button(f1, text="Submit", fg="#E0620A", command=insertdb, width=15, bg="#FFFFFF")
    B2.place(x=210, y=330)

def openreport():
    topreport1=Toplevel()
    topreport1.geometry("700x600+333+84")
    def opengen():
        topgender = Toplevel()
        topgender.geometry("700x600+333+84")
        topgender.title("bjvjhsvjhsbjbk")
        g1 = StringVar()
        g2 = StringVar()
        g3 = StringVar()


        def genreport():


            r4 = g1.get()
            r5 = g2.get()
            r6 = g3.get()
            query = "SELECT Gender,Date,COUNT(`Gender`) FROM detail WHERE Gender = '%s' HAVING Date between '%s' and '%s'" % (
            r6, r4, r5)
            con1 = db.Connect("localhost", "root", "", "record")
            cur = con1.cursor()
            cur.execute(query)
            count = cur.rowcount
            if count == 0:
                messagebox.showerror('ERROR', 'Incorrect detail')
            else:
                TableMargin = Frame(topgender, height="600", width="700")
                TableMargin.pack()

                scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
                scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
                tree = ttk.Treeview(TableMargin, columns=("a", "b", "c"), height=100,
                                    yscrollcommand=scrollbary.set,
                                    xscrollcommand=scrollbarx.set)
                scrollbary.config(command=tree.yview)
                scrollbary.pack(side=RIGHT, fill=Y)
                scrollbarx.config(command=tree.xview)
                scrollbarx.pack(side=BOTTOM, fill=X)

                tree.heading('a', text="Gender", anchor=W)
                tree.heading('b', text="Date", anchor=W)
                tree.heading('c', text="count", anchor=W)

                tree.column('#0', minwidth=0, width=0)
                tree.column('#1', minwidth=0, width=50)
                tree.column('#2', minwidth=0, width=80)
                tree.pack()

                query = "SELECT Gender,Date,COUNT(`Gender`) FROM detail WHERE Gender = '%s' HAVING Date between '%s' and '%s'" % (
                r6, r4, r5)
                con = db.connect("localhost", "root", "", "record")
                cur = con.cursor()
                cur.execute(query)
                row = cur.fetchone()
                while row is not None:
                    tree.insert('', 'end', values=(row))
                    row = cur.fetchone()

                cur.close()
                con.close()

        dfrane = Frame(topgender, bd=5, bg="#ffffff", height=600, width=1000)
        dfrane.place(x=0, y=0)
        label = Label(dfrane, text="The record of student you want to search", width=50, font=("Algerian", 16),
                      bg="#ffffff")
        label.place(x=20, y=0)

        l1 = Label(dfrane, text="Start date", bg="#ffffff", font=("Algerian", 16), width=10)
        l1.place(x=200, y=50)
        es1 = Entry(dfrane, text="from date", bg="#FFFFFF", textvariable=g1)
        es1.place(x=350, y=50, width=150, height=25)

        l2 = Label(dfrane, text="End date", bg="#ffffff", font=("Algerian", 16), width=10)
        l2.place(x=200, y=100)
        es2 = Entry(dfrane, bg="#FFFFFF", text="to date", textvariable=g2)
        es2.place(x=350, y=100, width=150, height=25)
        C1 = ttk.Combobox(dfrane, textvariable=g3, values=['----gender----', 'male', 'female', 'c#', 'ANDROID'])
        C1.configure(font=('bold', 18), width=10)
        C1.place(x=350, y=150)

        C1.current(0)
        lebel = Label(dfrane, text="Gender", font=("Algerian", 16), width=10, bg="#ffffff")
        lebel.place(x=200, y=150)

        bs = Button(dfrane, text="search", fg="#FFCA27", bg="#212A37", bd=0, width=8, font=("Algerian"), command=genreport)
        bs.place(x=300, y=200)


    def opencourse():
        topcouse = Toplevel()
        topcouse.geometry("700x600+333+84")

        s1 = StringVar()
        s2 = StringVar()
        s3 = StringVar()

        def report():
            r1 = s1.get()
            r2 = s2.get()
            r3 = s3.get()
            print(r1, r2, r3)
            query = "select course,Date,COUNT(`course`) from detail where course = '%s' HAVING Date between '%s' and '%s'" % (
            r3, r1, r2)
            con = db.Connect("localhost", "root", "", "record")
            cur = con.cursor()
            cur.execute(query)
            count = cur.rowcount
            if count == 0:
                messagebox.showerror('ERROR', 'Incorrect detail')
            else:
                TableMargin = Frame(topcouse, height="300", width="700")
                TableMargin.pack()

                scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
                scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
                tree = ttk.Treeview(TableMargin, columns=("a", "b", "c"), height=100,
                                    yscrollcommand=scrollbary.set,
                                    xscrollcommand=scrollbarx.set)
                scrollbary.config(command=tree.yview)
                scrollbary.pack(side=RIGHT, fill=Y)
                scrollbarx.config(command=tree.xview)
                scrollbarx.pack(side=BOTTOM, fill=X)

                tree.heading('a', text="Course", anchor=W)
                tree.heading('b', text="Date", anchor=W)
                tree.heading('c', text="Count", anchor=W)
                tree.column('#0', minwidth=0, width=0)
                tree.column('#1', minwidth=0, width=50)
                tree.column('#2', minwidth=0, width=80)
                tree.column('#3', minwidth=0, width=120)
                tree.pack()
                query = "select course,Date,COUNT(`course`) from detail where course = '%s' HAVING Date between '%s' and '%s'" % (
                r3, r1, r2)
                con = db.connect("localhost", "root", "", "record")
                cur = con.cursor()
                cur.execute(query)
                row = cur.fetchone()
                while row is not None:
                    tree.insert('', 'end', values=(row))
                    row = cur.fetchone()
                cur.close()
                con.close()

        dfrane = Frame(topcouse, bd=5, bg="#ffffff", height=600, width=1000)
        dfrane.place(x=0, y=0)
        label = Label(dfrane, text="The record of student you want to search", width=50, font=("Algerian", 16),
                      bg="#ffffff")
        label.place(x=20, y=0)

        l1 = Label(dfrane, text="Start date", bg="#ffffff", font=("Algerian", 16), width=10)
        l1.place(x=200, y=50)
        es1 = Entry(dfrane, text="from date", bg="#FFFFFF", textvariable=s1)
        es1.place(x=350, y=50, width=150, height=25)

        l2 = Label(dfrane, text="End date", bg="#ffffff", font=("Algerian", 16), width=10)
        l2.place(x=200, y=100)
        es2 = Entry(dfrane, bg="#FFFFFF", text="to date", textvariable=s2)
        es2.place(x=350, y=100, width=150, height=25)

        C1 = ttk.Combobox(dfrane, textvariable=s3, values=['----course----', 'python', 'c++', 'c#', 'ANDROID'])
        C1.configure(font=('bold', 18), width=10)
        C1.place(x=350, y=150)
        C1.current(0)
        lebel = Label(dfrane, text="course", font=("Algerian", 16), width=10, bg="#ffffff")
        lebel.place(x=200, y=150)

        bs = Button(dfrane, text="search", fg="#FFCA27", bg="#212A37", bd=0, width=8, font=("Algerian"), command=report)
        bs.place(x=300, y=200)


    F1 = Frame(topreport1, height=sheight, width=swidth, bg="#566573")
    F1.pack()
    B1 = Button(F1, text="Gender", font=("Algerian", 24), bg="#7F8C8D", command=opengen, width="15", height="1",
                fg="#ffffff")
    B1.place(x=210, y=120)
    B2 = Button(F1, text="Course", font=("Algerian", 24), bg="#7F8C8D", command=opencourse, width="15", height="1",
                fg="#ffffff")
    B2.place(x=210, y=220)



def openlist():
    toplist = Toplevel()
    toplist.title("ENQUIRY MANAGEMANT SYSTEM")
    toplist.geometry("1366x768+0+10")
    TableMargin1 = Frame(toplist, height="300", width="700")
    TableMargin1.pack()



    scrollbarx = Scrollbar(TableMargin1, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin1, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin1, columns=("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"), height=100,
                        yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('a', text="S_No", anchor=W)
    tree.heading('b', text="Name", anchor=W)
    tree.heading('c', text="Gender", anchor=W)
    tree.heading('d', text="Address", anchor=W)
    tree.heading('e', text="District", anchor=W)
    tree.heading('f', text="Contact_No", anchor=W)
    tree.heading('g', text="Email_id", anchor=W)
    tree.heading('h', text="course", anchor=W)
    tree.heading('i', text="question", anchor=W)
    tree.heading('j', text="Date", anchor=W)

    tree.column('#0', minwidth=0, width=0)
    tree.column('#1', minwidth=0, width=50)
    tree.column('#2', minwidth=0, width=80)
    tree.column('#3', minwidth=0, width=120)
    tree.column('#4', minwidth=0, width=150)
    tree.column('#5', minwidth=0, width=180)
    tree.column('#6', minwidth=0, width=190)
    tree.column('#7', minwidth=0, width=200)
    tree.column('#8', minwidth=0, width=210)
    tree.column('#9', minwidth=0, width=220)

    tree.pack()
    # table code end

    query = "select * from detail"

    con = db.connect("localhost", "root", "", "record")

    cur = con.cursor()
    cur.execute(query)
    row = cur.fetchone()
    while row is not None:
        tree.insert('', 'end', values=(row))
        row = cur.fetchone()
    cur.close()
    con.close()

def opendelete():
    topdelete = Toplevel()
    topdelete.title("ENQUIRY MANAGEMANT SYSTEM")
    topdelete.geometry("600x1000+550+10")

    TableMargin = Frame(topdelete, height="300", width="700")
    TableMargin.pack()

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("a", "b", "c", "d", "e", "f", "g", "h"), height=100,
                        yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('a', text="Name", anchor=W)
    tree.heading('b', text="Gender", anchor=W)
    tree.heading('c', text="Address", anchor=W)
    tree.heading('d', text="Contact_No", anchor=W)
    tree.heading('e', text="Email_id", anchor=W)
    tree.heading('f', text="course", anchor=W)
    tree.heading('g', text="question", anchor=W)

    tree.column('#0', minwidth=0, width=0)
    tree.column('#1', minwidth=0, width=50)
    tree.column('#2', minwidth=0, width=80)
    tree.column('#3', minwidth=0, width=120)
    tree.column('#4', minwidth=0, width=150)
    tree.column('#5', minwidth=0, width=120)
    tree.column('#6', minwidth=0, width=120)

    tree.pack()

    query = "select * from detail"

    con = db.connect("localhost", "root", "", "record")

    cur = con.cursor()
    cur.execute(query)
    row = cur.fetchone()
    while row is not None:
        tree.insert('', 'end', values=(row))
        row = cur.fetchone()

    cur.close()
    con.close()

    def del1():
        if not tree.selection():
            result = messagebox.showwarning('delete', 'Please Select Something First!')
        else:
            result = messagebox.askquestion('delete', 'Are you sure you want to delete this record?')
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                conn = db.connect("localhost", "root", "", "record")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM detail WHERE Name = '%s'" % selecteditem[0])
                conn.commit()
                cursor.close()
                conn.close()

    b1 = Button(topdelete, text="delete", font=("Algerian",24),bg="#7F8C8D",width="15",height="1",fg="#ffffff", command=del1)
    b1.place(x=150, y=600)



# def openlist():
#     Menuwindow.destroy()
#     import list

F1=Frame(Menuwindow, height=sheight,width=swidth,bg="#566573")
F1.pack()
l9=Label(F1,text="the record of student youy want to search",width=48,font=("Algerian",18))
l9.place(x=0,y=0)

lebel = Label(F1, text="selete basis",bg="#7F8C8D", font=("Algerian", 16),width="12",fg="#ffffff")
lebel.place(x=150, y=50)

C1 = ttk.Combobox(F1, textvariable=g7, values=['--select type--', 'Name', 'District'])
C1.configure(font=('bold', 18), width=10)
C1.place(x=350, y=50)
C1.current(0)


l10 = Label(F1, text="Name", bg="#7F8C8D", font=("Algerian", 16), width=10,fg="#ffffff")
l10.place(x=150,y=100)
es10 = Entry(F1, bg="#FFFFFF", text="name", textvariable=g8)
es10.place(x=350, y=100, width=150, height=25)
B6=Button(F1,text="search",font=("Algerian",14),bg="#7F8C8D",command=searchdetail,width="7",fg="#ffffff")
B6.place(x=550,y=100)

B1=Button(F1,text="entry",font=("Algerian",24),bg="#7F8C8D",command=openentry,width="15",height="1",fg="#ffffff")
B1.place(x=210,y=200)
B2=Button(F1,text="visiting students",font=("Algerian",24),bg="#7F8C8D",command=openlist,width="15",height="1",fg="#ffffff")
B2.place(x=210,y=300)
B3=Button(F1,text="report",font=("Algerian",24),bg="#7F8C8D",command=openreport,width="15",height="1",fg="#ffffff")
B3.place(x=210,y=400)
B4=Button(F1,text="delete",font=("Algerian",24),bg="#7F8C8D",command=opendelete,width="15",height="1",fg="#ffffff")
B4.place(x=210,y=500)


Menuwindow.mainloop()