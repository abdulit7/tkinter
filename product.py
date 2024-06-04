from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class ProductClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+220+130")
        self.root.title("Spare Parts Management System | Developed by BC200200486")
        self.root.focus_force()

        ######## Variables
        self.var_searchby = StringVar()
        self.var_Searchtext = StringVar()
        self.var_cat=StringVar()
        self.var_supp=StringVar()
        self.cat_list=[]
        self.supp_list=[]
        self.fetch_cat_supp()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()


        ######## Product Frame

        product_frame = Frame(self.root, bd=2,relief=RIDGE)
        product_frame.place(x=10,y=10, width=450,height=580)

        #Titles oulmn 1
        title=Label(product_frame,text="Product Details", font=("goudy old style",15), bg="skyblue",fg="white").pack(side=TOP,fill=X)

        label_category=Label(product_frame,text="Category", font=("goudy old style",15)).place(x=30,y=60)
        label_supplier=Label(product_frame,text="Supplier", font=("goudy old style",15)).place(x=30,y=130)
        label_name=Label(product_frame,text="Name", font=("goudy old style",15)).place(x=30,y=200)
        label_price=Label(product_frame,text="Price", font=("goudy old style",15)).place(x=30,y=270)
        label_qty=Label(product_frame,text="Quantity", font=("goudy old style",15)).place(x=30,y=350)
        label_status=Label(product_frame,text="Status", font=("goudy old style",15)).place(x=30,y=420)


        #Coulmn 2 Options
        cmb_category = ttk.Combobox(product_frame,values=self.cat_list,textvariable=self.var_cat,state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_category.place(x=150,y=60,width=200)
        cmb_category.current(0)
        
        cmb_supplier = ttk.Combobox(product_frame,values=self.supp_list,textvariable=self.var_supp,state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_supplier.place(x=150,y=130,width=200)
        cmb_supplier.current(0)

        text_name = Entry(product_frame, textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=200)
        text_price = Entry(product_frame, textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=150,y=270)
        text_qty = Entry(product_frame, textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150,y=350)

        cmb_status = ttk.Combobox(product_frame,values=("Select","Active","Inactive"),textvariable=self.var_status,state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=420,width=200)
        cmb_status.current(0)

        #Buttons.......

        btn_add = Button(product_frame,text="Save",command=self.add,font=("goudy old style",15),bg="#1E90FF",fg="white",cursor="hand2").place(x=2,y=520,width=105,height=28)
        btn_update = Button(product_frame,text="Update",command=self.update,font=("goudy old style",15),bg="#3CB371",fg="white",cursor="hand2").place(x=113,y=520,width=105,height=28)
        btn_delete = Button(product_frame,text="Detele",command=self.delete,font=("goudy old style",15),bg="#FF4500",fg="white",cursor="hand2").place(x=225,y=520,width=105,height=28)
        btn_clear = Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#778899",fg="white",cursor="hand2").place(x=336,y=520,width=105,height=28)

        #Search Frame
        SearchFrame = LabelFrame(self.root,text="Search Product",font=("goudy old style",12,"bold"),bd=2, relief=RIDGE)
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #Search Options
        cmb_search = ttk.Combobox(SearchFrame,values=("Select","Category","Supplier","Name"),textvariable=self.var_searchby,state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        txt_search = Entry(SearchFrame,font=("goudy old style",15),textvariable=self.var_Searchtext,bg="light yellow").place(x=200,y=10)
        btn_search = Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)


         # Product Details Tree View===

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480,y=100,width=700,height=450)

        scrolly= Scrollbar(p_frame, orient=VERTICAL)
        scrollx= Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame,columns=("pid","Category","Supplier","Name","Price","QTY","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #Command for Scrolling
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        #table Headings
        self.product_table.heading("pid",text="Product ID")
        self.product_table.heading("Category",text="Name")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("Name",text="Name")
        self.product_table.heading("Price",text="Price")
        self.product_table.heading("QTY",text="QTY")
        self.product_table.heading("Status",text="Status")
        self.product_table["show"]="headings"
        # Table Width set
        self.product_table.column("pid",width=90)
        self.product_table.column("Category",width=100)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("Name",width=100)
        self.product_table.column("Price",width=100)
        self.product_table.column("QTY",width=100)
        self.product_table.column("Status",width=100)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()


################################## Functions
    def fetch_cat_supp(self):
        self.cat_list.append("Empty")
        self.supp_list.append("Empty")
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()
        try:
            cursor.execute("select name from category")
            cat = cursor.fetchall()
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            cursor.execute("select name from supplier")
            supp = cursor.fetchall()
            if len(supp)>0:
                del self.supp_list[:]
                self.supp_list.append("Select")
                for i in supp:
                    self.supp_list.append(i[0])


        
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
########### Add Function


    def add(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            if self.var_cat.get()== "Select" or self.var_supp.get() =="Select" or self.var_name.get()=="":
                messagebox.showerror("Error", "All Fields Required to Fill",parent = self.root)
            else:
                cursor.execute("select * from product where Name=?",(self.var_name.get(),))
                row=cursor.fetchone()
                if row !=None:
                    messagebox.showerror("Error", "Product Already Available, Try Different")
                else:
                    cursor.execute("insert into product (Category,Supplier,Name,Price,QTY,Status) values(?,?,?,?,?,?)",(

                                                                    self.var_cat.get(),
                                                                    self.var_supp.get(),
                                                                    self.var_name.get(),
                                                                    self.var_price.get(),
                                                                    self.var_qty.get(),
                                                                    self.var_status.get(),
                                                                   
                    ))

                    conn.commit()
                    messagebox.showinfo("Successfull","Product Saved",parent=self.root)
                    self.show()
                    self.clear()
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

################# Show Function
    def show(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            cursor.execute("select * from product")
            rows = cursor.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("",END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
        
    ########## Get Data Function
    def get_data(self,ev):
        f=self.product_table.focus()
        content =(self.product_table.item(f))
        row = content["values"]
            
        
    
        self.var_cat.set(row[1]),
        self.var_supp.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6])

    ################ Update Data
    def update(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            if self.var_name.get()== "":
                messagebox.showerror("Error", "Product Name must be required",parent = self.root)
            else:
                cursor.execute("select * from product where Name=?",(self.var_name.get(),))
                row=cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Invalid Product Name")
                else:
                    cursor.execute("update product set Category=?,Supplier=?,Name=?,Price=?,QTY=?,Status=?",(

                                                                    
                                                                    self.var_cat.get(),
                                                                    self.var_supp.get(),
                                                                    self.var_name.get(),
                                                                    self.var_price.get(),
                                                                    self.var_qty.get(),
                                                                    self.var_status.get(),
                                                                  
                    ))

                    conn.commit()
                    messagebox.showinfo("Successfull","Product Updated",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
    
     ################ Delete User Function
    def delete(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()
        try:
            if self.var_name.get()== "":
                messagebox.showerror("Error", "Product Name must be required",parent = self.root)
            else:
                cursor.execute("select * from product where Name=?",(self.var_name.get(),))
                row=cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Invalid Product Name")
                else:
                    op = messagebox.askyesno("Confirm","Do you Realy want to Delete ?",parent=self.root)
                    if op ==TRUE:

                        cursor.execute("delete from product where name=?",(self.var_name.get(),))
                        conn.commit()
                        messagebox.showinfo("Successful","Product Deleted",parent=self.root)
                        self.clear()

            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
    ########### Clear Function

    def clear(self):
        self.var_cat.set("Select"),
        self.var_supp.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Select"),
        
        
        self.show()
    
    def search(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by Options",parent=self.root)
            elif self.var_searchby.get()=="":
                messagebox.showerror("Error","Search Area Input Should be Required",parent=self.root)
            else:

            
            
                cursor.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_Searchtext.get()+"%'")
                rows = cursor.fetchall()
                if len(rows) !=0:

                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("",END, values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = ProductClass(root)

    root.mainloop()