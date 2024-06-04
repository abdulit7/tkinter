from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class EmployeeClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+220+130")
        self.root.title("Spare Parts Management System | Developed by BC200200486")
        self.root.focus_force()

        #All Variables
        self.var_searchby = StringVar()
        self.var_Searchtext = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        
        

        #Search Frame
        SearchFrame = LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2, relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #Search Options
        cmb_search = ttk.Combobox(SearchFrame,values=("Select","Name","Contact","Email"),textvariable=self.var_searchby,state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        txt_search = Entry(SearchFrame,font=("goudy old style",15),textvariable=self.var_Searchtext,bg="light yellow").place(x=200,y=10)
        btn_search = Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        #Title
        title=Label(self.root,text="Employee Details", font=("goudy old style",15), bg="skyblue",fg="white").place(x=50,y=100,width=1100)

        #Content
        # Row1.....
        label_empid = Label(self.root, text="Employee ID",font=("goudy old style",15),bg="white").place(x=50,y=150,)
        label_gender = Label(self.root, text="Gender",font=("goudy old style",15),bg="white").place(x=450,y=150,)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=550,y=150,width=180)
        cmb_gender.current(0)
        label_contact = Label(self.root, text="Contact",font=("goudy old style",15),bg="white").place(x=850,y=150,)

        text_empid = Entry(self.root, textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=190,y=150,width=180)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=550,y=150,width=180)
        cmb_gender.current(0)
        text_contact = Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=950,y=150,width=180)

         # Row2.....
        label_name = Label(self.root, text="Employee Name",font=("goudy old style",15),bg="white").place(x=50,y=200,)
        label_dob = Label(self.root, text="D.O.B",font=("goudy old style",15),bg="white").place(x=450,y=200,)
        label_doj = Label(self.root, text="D.O.J",font=("goudy old style",15),bg="white").place(x=850,y=200,)

        text_name = Entry(self.root, textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=190,y=200,width=180)
        text_dob = Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="white").place(x=550,y=200,width=180)
        text_doj = Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=950,y=200,width=180)
# Row3.....

        label_email = Label(self.root, text="Employee Email",font=("goudy old style",15),bg="white").place(x=50,y=250,)
        label_pass = Label(self.root, text="Password",font=("goudy old style",15),bg="white").place(x=450,y=250,)
        label_utype = Label(self.root, text="User Type",font=("goudy old style",15),bg="white").place(x=850,y=250,)

        text_email = Entry(self.root, textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=190,y=250,width=180)
        text_pass = Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="white").place(x=550,y=250,width=180)
        cmb_utype = ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","User"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=950,y=250,width=180)
        cmb_utype.current(0)
        
        # Row4.....
        label_address = Label(self.root, text="Address",font=("goudy old style",15),bg="white").place(x=50,y=300,)
        label_salary = Label(self.root, text="Salary",font=("goudy old style",15),bg="white").place(x=520,y=300,)
        
        self.text_address=Text(self.root, font=("goudy old style",15),bg="lightyellow")
        self.text_address.place(x=190,y=300,width=300,height=60)
        text_salary= Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="white").place(x=600,y=300,width=180)


        #Buttons.......

        btn_add = Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#1E90FF",fg="white",cursor="hand2").place(x=600,y=360,width=110,height=28)
        btn_update = Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#3CB371",fg="white",cursor="hand2").place(x=712,y=360,width=110,height=28)
        btn_delete = Button(self.root,text="Detele",command=self.delete,font=("goudy old style",15),bg="#FF4500",fg="white",cursor="hand2").place(x=824,y=360,width=110,height=28)
        btn_clear = Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#778899",fg="white",cursor="hand2").place(x=936,y=360,width=110,height=28)

        # Employee Details===

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0,y=400,relwidth=1,height=200)

        scrolly= Scrollbar(emp_frame, orient=VERTICAL)
        scrollx= Scrollbar(emp_frame, orient=HORIZONTAL)

        self.employee_table = ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #Command for Scrolling
        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)
        #table Headings
        self.employee_table.heading("eid",text="EMP ID")
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("contact",text="Contact")
        self.employee_table.heading("dob",text="D.O.B")
        self.employee_table.heading("doj",text="D.O.J")
        self.employee_table.heading("pass",text="Password")
        self.employee_table.heading("utype",text="User Type")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("salary",text="Salary")
        self.employee_table["show"]="headings"
        # Table Width set
        self.employee_table.column("eid",width=90)
        self.employee_table.column("name",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("contact",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("pass",width=100)
        self.employee_table.column("utype",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("salary",width=100)
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#=============================================================================================================================

    def add(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            if self.var_emp_id.get()== "":
                messagebox.showerror("Error", "Employee ID must be required",parent = self.root)
            else:
                cursor.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cursor.fetchone()
                if row !=None:
                    messagebox.showerror("Error", "This Employee ID already assigned, Try Different")
                else:
                    cursor.execute("insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(

                                                                    self.var_emp_id.get(),
                                                                    self.var_name.get(),
                                                                    self.var_email.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_contact.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_doj.get(),
                                                                    self.var_pass.get(),
                                                                    self.var_utype.get(),
                                                                    self.text_address.get('1.0',END),
                                                                    self.var_salary.get(),
                    ))

                    conn.commit()
                    messagebox.showinfo("Successfull","Employee Saved",parent=self.root)
                    self.show()
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

####################Show Data into tree view

    def show(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            cursor.execute("select * from employee")
            rows = cursor.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert("",END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

################### View Data in fields
    def get_data(self,ev):
        f=self.employee_table.focus()
        content =(self.employee_table.item(f))
        row = content["values"]
            
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.text_address.delete('1.0',END),
        self.text_address.insert(END,row[9]),
        self.var_salary.set(row[10]),
        
################ Update Data
    def update(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            if self.var_emp_id.get()== "":
                messagebox.showerror("Error", "Employee ID must be required",parent = self.root)
            else:
                cursor.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Invalid Employee ID")
                else:
                    cursor.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(

                                                                    
                                                                    self.var_name.get(),
                                                                    self.var_email.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_contact.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_doj.get(),
                                                                    self.var_pass.get(),
                                                                    self.var_utype.get(),
                                                                    self.text_address.get('1.0',END),
                                                                    self.var_salary.get(),
                                                                    self.var_emp_id.get(),
                    ))

                    conn.commit()
                    messagebox.showinfo("Successfull","Employee Updated",parent=self.root)
                    self.show()
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
    ################ Delete User Function
    def delete(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()
        try:
            if self.var_emp_id.get()== "":
                messagebox.showerror("Error", "Employee ID must be required",parent = self.root)
            else:
                cursor.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Invalid Employee ID")
                else:
                    op = messagebox.askyesno("Confirm","Do you Realy want to Delete ?",parent=self.root)
                    if op ==TRUE:

                        cursor.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Successful","Employee Deleted",parent=self.root)
                        self.clear()

            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
    ########### Clear Function

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.text_address.delete('1.0',END),
        self.var_salary.set(""),
        
        self.show()
    
    ###### Search Function

    def search(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by Options",parent=self.root)
            elif self.var_searchby.get()=="":
                messagebox.showerror("Error","Search Area Input Should be Required",parent=self.root)
            else:

            
            
                cursor.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_Searchtext.get()+"%'")
                rows = cursor.fetchall()
                if len(rows) !=0:

                    self.employee_table.delete(*self.employee_table.get_children())
                    for row in rows:
                        self.employee_table.insert("",END, values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = EmployeeClass(root)

    root.mainloop()