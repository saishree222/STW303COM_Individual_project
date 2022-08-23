from imp import reload
from tkinter import*
from tkinter import messagebox
from turtle import title
from unittest import result
import pymysql


class EmpSystem:
    def __init__(self, root):
        self.root= root
        self.root.title("Employee Management System")
        self.root.geometry("1350x700+0+0")
        title= Label(self.root, text="Employee Management System", font=("times new roman", 30, "bold"),
        bg="#262626", fg="white").place(x=0, y=0, relwidth=1)

        #------Frame 1

        #-------variable

        self.var_emcode= StringVar()
        self.var_emdepartment= StringVar()
        self.var_emname= StringVar()
        self.var_emage= StringVar()
        self.var_emgender= StringVar()
        self.var_emmail= StringVar()
        self.var_emdob= StringVar()
        self.var_emdoj= StringVar()
        self.var_emexp= StringVar()
        self.var_emid= StringVar()
        self.var_emnum= StringVar()


        Frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=70, width=750, height=620)
        f1title= Label(Frame1, text="Employee Details", font=("Segoe Script", 25, "bold"),
        bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        lbl_emcode = Label(Frame1, text="Employee code", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=10, y=90)
        txt_emcode = Entry(Frame1, font=("calibri(light)", 15,), textvariable=self.var_emcode, bg="lightyellow", fg="black", ).place(x=170, y=90, width=200)

        btn_search= Button(Frame1, text="Search", font=("calibri(light)", 15,), bg="grey", fg="black", ).place(x=650, y=90, height=30)


        #-----row1
        lbl_emdepartment = Label(Frame1, text="Department", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=145)
        txt_emdepartment = Entry(Frame1, font=("calibri(light)", 15,),  textvariable=self.var_emdepartment, bg="lightyellow", fg="black", ).place(x=172, y=145, width=200)

        lbl_emdob = Label(Frame1, text="D.O.B", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=410, y=145)
        txt_emdob = Entry(Frame1, font=("calibri(light)", 15,),  textvariable=self.var_emdob, bg="lightyellow", fg="black", ).place(x=500, y=145)

        #-----row2
        lbl_emname = Label(Frame1, text="Name", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=200)
        txt_emname = Entry(Frame1, font=("calibri(light)", 15,),  textvariable=self.var_emname, bg="lightyellow", fg="black", ).place(x=172, y=200, width=200)

        lbl_emdoj = Label(Frame1, text="D.O.J", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=410, y=200)
        txt_emdoj = Entry(Frame1, font=("calibri(light)", 15,),  textvariable=self.var_emdoj, bg="lightyellow", fg="black", ).place(x=500, y=200)

        #-----row3
        lbl_emage = Label(Frame1, text="Age", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=250)
        txt_emage = Entry(Frame1, font=("calibri(light)", 15,),  textvariable=self.var_emage, bg="lightyellow", fg="black", ).place(x=172, y=250, width=100)

        lbl_emexp = Label(Frame1, text="Experience", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=390, y=250)
        txt_emexp = Entry(Frame1, font=("calibri(light)", 15,),  textvariable=self.var_emexp, bg="lightyellow", fg="black", ).place(x=500, y=250)

        #-----row4
        lbl_emgender = Label(Frame1, text="Gender", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=305)
        txt_emgender = Entry(Frame1, font=("calibri(light)", 15,), textvariable=self.var_emgender, bg="lightyellow", fg="black", ).place(x=172, y=305, width=100)

        lbl_emid = Label(Frame1, text="National ID No.", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=350, y=305)
        txt_emid = Entry(Frame1, font=("calibri(light)", 15,),  textvariable=self.var_emid, bg="lightyellow", fg="black", ).place(x=500, y=305)

        #-----row5
        lbl_emmail = Label(Frame1, text="Email", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=360)
        txt_emmail = Entry(Frame1, font=("calibri(light)", 15,), textvariable=self.var_emmail, bg="lightyellow", fg="black", ).place(x=172, y=360, width=200)

        lbl_emnum = Label(Frame1, text="Contact No.", font=("calibri(light)", 14,), bg="white", fg="black", ).place(x=390, y=360)
        txt_emnum = Entry(Frame1, font=("calibri(light)", 15,),  textvariable=self.var_emnum, bg="lightyellow", fg="black", ).place(x=500, y=360)

        #-----row6
        lbl_emadd = Label(Frame1, text="Address", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=490)
        self. txt_emadd = Entry(Frame1, font=("calibri(light)", 15,), bg="lightyellow", fg="black", )
        self.txt_emadd.place(x=170, y=430, width=550, height=150)


        #------Frame 2

        #-------variable

        self.var_emmon= StringVar()
        self.var_emyear= StringVar()
        self.var_emsalary= StringVar()
        self.var_emday= StringVar()
        self.var_emabs= StringVar()
        self.var_emmed= StringVar()
        self.var_emprfd= StringVar()
        self.var_emcon= StringVar()
        self.var_emnet= StringVar()



        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame2.place(x=765, y=70, width=580, height=315) 

        f2title= Label(Frame2, text="Salary Details", font=("Segoe Script", 25, "bold"),
        bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

   
        
        #-----row1
        lbl_emmon = Label(Frame2, text="Month", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=80)
        txt_emmon = Entry(Frame2, font=("calibri(light)", 15,), textvariable=self.var_emmon, bg="lightyellow", fg="black", ).place(x=85, y=80, width=90)

        lbl_emyear = Label(Frame2, text="Year", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=190, y=80)
        txt_emyear = Entry(Frame2, font=("calibri(light)", 15,),  textvariable=self.var_emyear, bg="lightyellow", fg="black", ).place(x=245, y=80, width=90)

        lbl_emsalary = Label(Frame2, text="Initial Salary", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=350, y=80)
        txt_emsalary = Entry(Frame2, font=("calibri(light)", 15,),  textvariable=self.var_emsalary, bg="lightyellow", fg="black", ).place(x=470, y=80, width=90)

        #-----row2
        lbl_emday = Label(Frame2, text="Total Days", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=130)
        txt_emday = Entry(Frame2, font=("calibri(light)", 15,), textvariable=self.var_emday, bg="lightyellow", fg="black", ).place(x=130, y=130, width=140)

        lbl_emabs = Label(Frame2, text="Total Absents", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=285, y=130)
        txt_emabs = Entry(Frame2, font=("calibri(light)", 15,),  textvariable=self.var_emabs, bg="lightyellow", fg="black", ).place(x=420, y=130, width=140)

        #-----row3
        lbl_emmed = Label(Frame2, text="Medical ", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=180)
        txt_emmed = Entry(Frame2, font=("calibri(light)", 15,),  textvariable=self.var_emmed, bg="lightyellow", fg="black", ).place(x=130, y=180, width=140)

        lbl_emprfd = Label(Frame2, text="Provident Fund", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=275, y=180)
        txt_emprfd = Entry(Frame2, font=("calibri(light)", 15,),  textvariable=self.var_emprfd, bg="lightyellow", fg="black", ).place(x=420, y=180, width=140)

        #-----row4
        lbl_emcon = Label(Frame2, text="Conveyance", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=12, y=230)
        txt_emcon = Entry(Frame2, font=("calibri(light)", 15,),  textvariable=self.var_emcon, bg="lightyellow", fg="black", ).place(x=130, y=230, width=140)

        lbl_emnet = Label(Frame2, text="Net Salary", font=("calibri(light)", 15,), bg="white", fg="black", ).place(x=315, y=230)
        txt_emnet = Entry(Frame2, font=("calibri(light)", 15,),  textvariable=self.var_emnet, bg="lightyellow", fg="black", ).place(x=420, y=230, width=140)


        #-----btn row 5

        btn_cal= Button(Frame2, text="Calculate",  command=self.calculate, font=("calibri(light)", 14,), bg="grey", fg="black", ).place(x=310, y=280, height=22)
        btn_save= Button(Frame2, text="Save", command=self.add, font=("calibri(light)", 14,), bg="grey", fg="black", ).place(x=420, y=280, height=22)
        btn_clear= Button(Frame2, text="Clear", font=("calibri(light)", 14,), bg="grey", fg="black", ).place(x=495, y=280, height=22)




        #------Frame 3
        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame3.place(x=765, y=385, width=580, height=305)


        #------calculator
        self.var_txt = StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator= self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
           
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear():
            self.var_txt.set('')
            self.var_operator=''



        Frame_cal= Frame(Frame3, bg="white", bd=2, relief=RAISED)
        Frame_cal.place(x=5, y=5, width=280, height=290)
        txt_result= Entry(Frame_cal, bg="lightyellow", textvariable=self.var_txt, font=("calibri(light)", 15), justify=RIGHT).place(x=2, y=2, width=270, height=30,)

        btn= Button(Frame3, text='7', command= lambda:btn_click(7), font=("calibri(light)", 15,)).place(x= 10, y=42, w= 60, h= 60)
        btn= Button(Frame3, text='8', command= lambda:btn_click(8), font=("calibri(light)", 15,)).place(x= 80, y=42, w= 60, h= 60)
        btn= Button(Frame3, text='9', command= lambda:btn_click(9), font=("calibri(light)", 15,)).place(x= 150, y=42, w= 60, h= 60)
        btn= Button(Frame3, text='/',  command= lambda:btn_click('/'),font=("calibri(light)", 15,)).place(x= 220, y=42, w= 60, h= 60)
        
        btn= Button(Frame3, text='4', command= lambda:btn_click(4), font=("calibri(light)", 15,)).place(x= 10, y=105, w= 60, h= 60)
        btn= Button(Frame3, text='5', command= lambda:btn_click(5), font=("calibri(light)", 15,)).place(x= 80, y=105, w= 60, h= 60)
        btn= Button(Frame3, text='6',  command= lambda:btn_click(6),font=("calibri(light)", 15,)).place(x= 150, y=105, w= 60, h= 60)
        btn= Button(Frame3, text='*', command= lambda:btn_click('*'), font=("calibri(light)", 15,)).place(x= 220, y=105, w= 60, h= 60)

        btn= Button(Frame3, text='1', command= lambda:btn_click(1), font=("calibri(light)", 15,)).place(x= 10, y=168, w= 60, h= 60)
        btn= Button(Frame3, text='2',  command= lambda:btn_click(2),font=("calibri(light)", 15,)).place(x= 80, y=168, w= 60, h= 60)
        btn= Button(Frame3, text='3', command= lambda:btn_click(3), font=("calibri(light)", 15,)).place(x= 150, y=168, w= 60, h= 60)
        btn= Button(Frame3, text='-', command= lambda:btn_click('-'), font=("calibri(light)", 15,)).place(x= 220, y=168, w= 60, h= 60)

        btn= Button(Frame3, text='0', command= lambda:btn_click(0), font=("calibri(light)", 15,)).place(x= 10, y=231, w= 60, h= 60)
        btn= Button(Frame3, text='C', command= clear, font=("calibri(light)", 15,)).place(x= 80, y=231, w= 60, h= 60)
        btn= Button(Frame3, text='+', command= lambda:btn_click('+'), font=("calibri(light)", 15,)).place(x= 150, y=231, w= 60, h= 60)
        btn= Button(Frame3, text='=', command= result, font=("calibri(light)", 15,)).place(x= 220, y=231, w= 60, h= 60)

        #-------salary
        frame_sal= Frame(Frame3, bg= "white", bd=2, relief= RAISED)
        frame_sal.place(x= 290,y=2, width=285, height=300)


        sal_title= Label(frame_sal, text="Salary Reciept", font=("Segoe Script", 20, "bold"),
        bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        
        f2_sal= Frame(frame_sal, bg='white', bd=2, relief= RAISED)
        f2_sal.place(x=0, y=50, relwidth=1, height=220)

        from random import sample


        sample= f'''\tcompany name, ABC\n\tAddress: Abc, Floor 2
-------------
emoloyee ID\t\t: 1024
salary of\t\t: MON-YYYY
Generated on\t\t: DD-MM-YYYY
----------------------------
tota days\t\t: DD
total present\t\t: DD
total absent\t\t: DD
conyance\t\t: rs ....
medical\t\t: RS ..
PF\t\t: rs .....
gross pay\t\t: Rs .....
Net Salary\t\t: RS ......
----------------------------
'''

        scroll_y = Scrollbar(f2_sal, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.recipet_txt= Text(f2_sal, font=("calibri(light)", 15,), bg='lightyellow', yscrollcommand=scroll_y.set)
        self.recipet_txt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.recipet_txt.yview)
        # self.txt_salary_reciept.insert(END, sample)


        btn_print= Button(frame_sal, text="Print", font=("calibri(light)", 18,), bg="orange", fg="black", ).place(x=210, y=270, height=22)

        self.check_connect()




    def add(self):
        if self.var_emcode.get()=='' :
            messagebox.showerror("enter details")
        else:
     

            try:
                con=pymysql.connect(host='localhost', user='root', password='', db='ems' )
                cur=con.cursor()
                cur.execute("Select * from empsalary where emid=%s", (self.var_emcode.get()))
                row= cur.fetchone()
            
                if row!=None:
                    messagebox.showerror("error", "code already exist", parent=self.root)
                else:
                    cur.execute("insert emsalary value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_emid.get(),
                        self.var_emcode.get(),
                       self.var_emdepartment.get(),
                        self.var_emname.get(),
                        self.var_emage.get(),
                        self.var_emgender.get(),
                        self.var_emmail.get(),
                        self.txt_emadd.get('1.0', END),  
                        self.var_emdob.get(),
                        self.var_emdoj.get(),
                        self.var_emexp.get(),
                        self.var_emid.get(),
                        self.var_emnum.get(),

                   

                        self.var_emmon.get(),
                        self.var_emyear.get(),
                        self.var_emsalary.get(),
                        self.var_emday.get(),
                        self.var_emabs.get(),
                        self.var_emmed.get(),
                        self.var_emprfd.get(),
                        self.var_emcon.get(),
                        self.var_emnet.get(),
                        self.var_emcode.get()+'.txt'
                         

                    )
                    )
                    con.commit()
                    con.close()
                    file= open('salary reciept/'+str(self.var_emcode.get())+'.txt','w')
                    file.write(self.recipet_txt.get('1.0', END))
                    file.close
                    
                    messagebox.showinfo("sucess","record added")
                
            except Exception as ex:
                messagebox.showerror("Error", f'Error due to : {str(ex)}')
    

    def calculate(self):
        if self.var_emmon.get()=='' or self.var_year.get()=='' or self.var_emsalary.get()=='' or self.var_emday.get()=='' or self.var_emabs.get()=='' or self.var_emmed.get()=='' or self.var_emprfd.get()==''  or self.var_emcon.get()=='' or self.var_emnet.get()=='' or self.txt_emadd.get('1.0', END)=='':
            messagebox.showerror('error', 'all fields are required')
        else:
            # self.var_emnet.set("RESULT")
            # 35000/31 == 1752
            # 31-10=21*1752

            per_day= int(self.var_emsalary.get())/int(self.var_emday.get())
            work_day= int(self.var_emday.get())-int(self.var_emabs.get())
            salary= per_day*work_day
            deduct=int(self.var_emmed.get())+int(self.var_emprfd.get())
            add= int(self.var_emcon.get())
            net= salary-deduct+add
            self.var_emnet.set(str(round(net, 2)))

            sample= f'''\tcompany name, ABC\n\tAddress: Abc, Floor 2
-------------
emoloyee ID\t\t: {self.var_emcode.get()}
salary of\t\t: {self.var_emmon.get()}-{self.var_emyear.get()}

----------------------------
tota days\t\t: {self.var_emday.get()}
total present\t\t: {str(int(self.var_emday.get())-int(self.var_emabs.get()))}
total absent\t\t: {self.var_emabs.get()}
conyance\t\t: Rs. {self.var_emcon.get()}
medical\t\t: RS {self.var_emmed.get()}
PF\t\t: rs {self.var_emprfd}
gross pay\t\t: Rs {self.var_emsalary.get()}
Net Salary\t\t: RS {self.var_emnet.get()}
----------------------------
'''
            self.recipet_txt.delete('1.0',END)
            self.recipet_txt.insert(END, sample)


    def check_connect(self):
        try:
            con=pymysql.connect(host='localhost', user='root', password='', db='ems' )
            cur=con.cursor()
            cur.execute("Select * from empsalary")
            rows= cur.fetchall
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')



root= Tk()
obj=EmpSystem(root)
root.mainloop()