from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class SupplierClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+220+130")
        self.root.title("Spare Parts Management System | Developed by BC200200486")
        self.root.focus_force()

        #All Variables
        self.var_searchby = StringVar()
        self.var_Searchtext = StringVar()

        self.var_supp_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        
        
        
        

        #Search Frame
        SearchFrame = LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2, relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #Search Options
        label_search = Label(SearchFrame,text="Search by Invoice",font=("goudy old style",15))
        label_search.place(x=10,y=10)
        txt_search = Entry(SearchFrame,font=("goudy old style",15),textvariable=self.var_Searchtext,bg="light yellow").place(x=200,y=10)
        btn_search = Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        #Title
        title=Label(self.root,text="Supplier Details", font=("goudy old style",15), bg="skyblue",fg="white").place(x=50,y=100,width=1100)

        #Content
        # Row1.....
        label_supp_invoice = Label(self.root, text="Invoice No",font=("goudy old style",15),bg="white").place(x=50,y=150,)
        text_supp_invoice = Entry(self.root, textvariable=self.var_supp_invoice,font=("goudy old style",15),bg="lightyellow").place(x=190,y=150,width=180)
   

         # Row2.....
        label_name = Label(self.root, text="Employee Name",font=("goudy old style",15),bg="white").place(x=50,y=200,)
        text_name = Entry(self.root, textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=190,y=200,width=180)
        
# Row3.....

        label_contact = Label(self.root, text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=250,)
        text_contact = Entry(self.root, textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=190,y=250,width=180)
       
        
        # Row4.....
        label_Desc = Label(self.root, text="Description",font=("goudy old style",15),bg="white").place(x=50,y=300,)
        
        self.text_desc=Text(self.root, font=("goudy old style",15),bg="lightyellow")
        self.text_desc.place(x=190,y=300,width=300,height=60)
        


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

        self.supplier_table = ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #Command for Scrolling
        scrollx.config(command=self.supplier_table.xview)
        scrolly.config(command=self.supplier_table.yview)
        #table Headings
        self.supplier_table.heading("invoice",text="Invoice")
        self.supplier_table.heading("name",text="Name")
        self.supplier_table.heading("contact",text="Contact")
        self.supplier_table.heading("desc",text="Description")
        self.supplier_table["show"]="headings"
        # Table Width set
        self.supplier_table.column("invoice",width=90)
        self.supplier_table.column("name",width=100)
        self.supplier_table.column("contact",width=100)
        self.supplier_table.column("desc",width=100)
        self.supplier_table.pack(fill=BOTH,expand=1)
        self.supplier_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#=============================================================================================================================

    def add(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            if self.var_supp_invoice.get()== "":
                messagebox.showerror("Error", "Invoice must be required",parent = self.root)
            else:
                cursor.execute("select * from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row=cursor.fetchone()
                if row !=None:
                    messagebox.showerror("Error", "Invoice ID already assigned, Try Different")
                else:
                    cursor.execute("insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(

                                                                    self.var_supp_invoice.get(),
                                                                    self.var_name.get(),
                                                                    self.var_contact.get(),
                                                                    self.text_desc.get('1.0',END),
                    ))

                    conn.commit()
                    messagebox.showinfo("Successfull","Supplier Saved",parent=self.root)
                    self.show()
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

####################Show Data into tree view

    def show(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            cursor.execute("select * from supplier")
            rows = cursor.fetchall()
            self.supplier_table.delete(*self.supplier_table.get_children())
            for row in rows:
                self.supplier_table.insert("",END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

################### View Data in fields
    def get_data(self,ev):
        f=self.supplier_table.focus()
        content =(self.supplier_table.item(f))
        row = content["values"]
            
        self.var_supp_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.text_desc.delete('1.0',END),
        self.text_desc.insert(END,row[3]),
        
################ Update Data
    def update(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            if self.var_supp_invoice.get()== "":
                messagebox.showerror("Error", "Invoice No. must be required",parent = self.root)
            else:
                cursor.execute("select * from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row=cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Invalid Invoice No.")
                else:
                    cursor.execute("update supplier set name=?,contact=?,desc=? where invoice=?",(

                                                                    
                                                                    self.var_name.get(),
                                                                    self.var_contact.get(),
                                                                    self.text_desc.get('1.0',END),
                                                                    self.var_supp_invoice.get(),
                    ))

                    conn.commit()
                    messagebox.showinfo("Successfull","Supplier Updated",parent=self.root)
                    self.show()
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
    ################ Delete User Function
    def delete(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()
        try:
            if self.var_supp_invoice.get()== "":
                messagebox.showerror("Error", "Invoice No. must be required",parent = self.root)
            else:
                cursor.execute("select * from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row=cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Invalid Invoice No.")
                else:
                    op = messagebox.askyesno("Confirm","Do you Realy want to Delete ?",parent=self.root)
                    if op ==TRUE:

                        cursor.execute("delete from supplier where invoice=?",(self.var_supp_invoice.get(),))
                        conn.commit()
                        messagebox.showinfo("Successful","Supplier Deleted",parent=self.root)
                        self.clear()

            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
    ########### Clear Function

    def clear(self):
        self.var_supp_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.text_desc.delete('1.0',END),
        self.var_Searchtext.set("")
        
        self.show()
    
    ###### Search Function

    def search(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            
      
            if self.var_Searchtext.get()=="":
                messagebox.showerror("Error","Incoice No. Should be Required",parent=self.root)
            else:

            
            
                cursor.execute("select * from supplier where invoice=?",(self.var_Searchtext.get(),))
                rows = cursor.fetchone()
                if rows !=None:

                    self.supplier_table.delete(*self.supplier_table.get_children())
                    self.supplier_table.insert("",END, values=rows)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)

    root.mainloop()