from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time


class BillClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Spare Parts Management System | Developed by BC200200486")

        self.icon_title = PhotoImage(file="images/logo2.png")

        self.var_cart_list = []


        #title....
        title = Label(self.root, text="Spare Parts Management System", image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#87CEFA",fg="#000000",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #logout button
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#FFFF00", cursor="hand2").place(x=1350,y=10,height=50,width=150)

        #Clock
        self.labl_clock = Label(self.root, text="Welcome to Spare Parts Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15),bg="#5F9EA0",fg="white")
        self.labl_clock.place(x=0,y=70,relwidth=1,height=30)

    ############# Product Frame
        

        ProductFrame1 = Frame(self.root,bd=3, relief=RIDGE)
        ProductFrame1.place(x=6,y=110,width=410,height=650)
        Ptitle = Label(ProductFrame1,text="Product Details", font=("times new roman",20,"bold"),bg="#000000",fg="white").pack(side=TOP,fill=X)
        
        ######### Search Frame #########
        self.var_search = StringVar()
        
        ProductFrame2 = Frame(ProductFrame1,bd=3, relief=RIDGE)
        ProductFrame2.place(x=2,y=42,width=400,height=98)

        label_search = Label(ProductFrame2,text="Search Product | By Name", font=("goudy old style",15,"bold"),fg="green").place(x=2,y=5)
        label_product = Label(ProductFrame2,text="Product Name",font=("goudy old style",15,"bold")).place(x=5,y=45)
        txt_search = Entry(ProductFrame2,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=135,y=47,width=150,height=22)
        btn_search = Button(ProductFrame2,text="Search",command=self.search,font=("times new roman",15),bg="#FFFF00",cursor="hand2").place(x=290,y=47,width=100,height=22)
        btn_shAll = Button(ProductFrame2,text="Show All",command=self.show,font=("times new roman",15),bg="#000000",cursor="hand2",fg="white").place(x=290,y=5,width=100,height=22)

        # Product Details===

        ProductFrame3 = Frame(ProductFrame1, bd=2, relief=RIDGE)
        ProductFrame3.place(x=2,y=145,width=400,height=470)

        scrolly= Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx= Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(ProductFrame3,columns=("pid","Name","Price","QTY","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #Command for Scrolling
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        #table Headings
        self.product_table.heading("pid",text="pid")
        self.product_table.heading("Name",text="Name")
        self.product_table.heading("Price",text="Price")
        self.product_table.heading("QTY",text="QTY")
        self.product_table.heading("Status",text="Status")
        self.product_table["show"]="headings"
        # Table Width set
        self.product_table.column("pid",width=40)
        self.product_table.column("Name",width=50)
        self.product_table.column("Price",width=50)
        self.product_table.column("QTY",width=50)
        self.product_table.column("Status",width=50)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        label_note = Label(ProductFrame1,text="Note: 'Enter 0 Qty to Remove Product From Cart'",font=("times new roman",12),bg="yellow").pack(side=BOTTOM,fill=X)


        ########### Customer Frame
        self.var_name = StringVar()
        self.var_contact = StringVar()

        CustomerFrame = Frame(self.root,bd=3, relief=RIDGE)
        CustomerFrame.place(x=420,y=110,width=630,height=70)
        ctitle = Label(CustomerFrame,text="Customer Details", font=("times new roman",15,"bold"),bg="lightgray",).pack(side=TOP,fill=X)

        label_name = Label(CustomerFrame,text="Name",font=("goudy old style",15,"bold")).place(x=5,y=35)
        txt_name = Entry(CustomerFrame,textvariable=self.var_name,font=("goudy old style",13),bg="lightyellow").place(x=70,y=35,width=180)

        label_contact = Label(CustomerFrame,text="Contact No.",font=("goudy old style",15,"bold")).place(x=260,y=35)
        txt_contact = Entry(CustomerFrame,textvariable=self.var_contact,font=("goudy old style",13),bg="lightyellow").place(x=370,y=35,width=150)

        Cal_CartFrame = Frame(self.root,bd=2, relief=RIDGE)
        Cal_CartFrame.place(x=420,y=190,width=630,height=460)
        ############# Calculator Frame
        self.var_cal_input= StringVar()

        Cal_Frame = Frame(Cal_CartFrame,bd=8, relief=RIDGE)
        Cal_Frame.place(x=5,y=10,width=300,height=400)

        txt_cal_input = Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),state="readonly",width=24,bd=10,relief=GROOVE,justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        ###### Call Button Row 1
        bnt_7 = Button(Cal_Frame,text="7",font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=15,cursor="hand2").grid(row=1,column=0)
        bnt_8 = Button(Cal_Frame,text="8",font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=15,cursor="hand2").grid(row=1,column=1)
        bnt_9 = Button(Cal_Frame,text="9",font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=15,cursor="hand2").grid(row=1,column=2)
        bnt_plus = Button(Cal_Frame,text="+",font=("arial",15,"bold"),command=lambda:self.get_input("+"),bd=5,width=4,pady=15,cursor="hand2").grid(row=1,column=3)
           ###### Call Button Row 2
        bnt_4 = Button(Cal_Frame,text="4",font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=15,cursor="hand2").grid(row=2,column=0)
        bnt_5 = Button(Cal_Frame,text="5",font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=15,cursor="hand2").grid(row=2,column=1)
        bnt_6 = Button(Cal_Frame,text="6",font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=15,cursor="hand2").grid(row=2,column=2)
        bnt_minus = Button(Cal_Frame,text="-",font=("arial",15,"bold"),command=lambda:self.get_input("-"),bd=5,width=4,pady=15,cursor="hand2").grid(row=2,column=3)
             ###### Call Button Row 3
        bnt_1 = Button(Cal_Frame,text="1",font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=15,cursor="hand2").grid(row=3,column=0)
        bnt_2 = Button(Cal_Frame,text="2",font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=15,cursor="hand2").grid(row=3,column=1)
        bnt_3 = Button(Cal_Frame,text="3",font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=15,cursor="hand2").grid(row=3,column=2)
        bnt_multiply = Button(Cal_Frame,text="x",font=("arial",15,"bold"),command=lambda:self.get_input("x"),bd=5,width=4,pady=15,cursor="hand2").grid(row=3,column=3)
             ###### Call Button Row 4
        bnt_0 = Button(Cal_Frame,text="0",font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        bnt_c = Button(Cal_Frame,text="C",font=("arial",15,"bold"),command=self.cal_clear,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        bnt_eq = Button(Cal_Frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        bnt_div = Button(Cal_Frame,text="/",font=("arial",15,"bold"),command=lambda:self.get_input("/"),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)


        ######## Cart Frame
        CartFrame = Frame(Cal_CartFrame, bd=2, relief=RIDGE)
        CartFrame.place(x=310,y=10,width=300,height=400)
        self.CartTitle= Label(CartFrame,text="Total Product \t [0]",font=("times new roman",15),bg="lightgray")
        self.CartTitle.pack(side=TOP,fill=X)

        scrolly= Scrollbar(CartFrame, orient=VERTICAL)
        scrollx= Scrollbar(CartFrame, orient=HORIZONTAL)

        self.cart_table = ttk.Treeview(CartFrame,columns=("pid","Name","Price","QTY","Stock"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #Command for Scrolling
        scrollx.config(command=self.cart_table.xview)
        scrolly.config(command=self.cart_table.yview)
        #table Headings
        self.cart_table.heading("pid",text="pid")
        self.cart_table.heading("Name",text="Name")
        self.cart_table.heading("Price",text="Price")
        self.cart_table.heading("QTY",text="QTY")
        self.cart_table.heading("Stock",text="Stock")
        self.cart_table["show"]="headings"
        # Table Width set
        self.cart_table.column("pid",width=40)
        self.cart_table.column("Name",width=50)
        self.cart_table.column("Price",width=50)
        self.cart_table.column("QTY",width=50)
        self.cart_table.column("Stock",width=50)

        self.cart_table.pack(fill=BOTH,expand=1)
        self.cart_table.bind("<ButtonRelease-1>",self.get_data_cart)

        ################ Add Cart Frame
        self.var_pid= StringVar()
        self.var_pname= StringVar()
        self.var_price= StringVar()
        self.var_qty= StringVar()
        self.var_stock= StringVar()

        Add_CartFrame = Frame(self.root,bd=2, relief=RIDGE)
        Add_CartFrame.place(x=420,y=650,width=630,height=200)

        
        label_p_name = Label(Add_CartFrame,text="Product Name.",font=("goudy old style",15,"bold")).place(x=5,y=5)
        txt_p_name = Entry(Add_CartFrame,textvariable=self.var_pname,font=("goudy old style",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)

        label_p_price = Label(Add_CartFrame,text="Price Per Qty",font=("goudy old style",15,"bold")).place(x=230,y=5)
        txt_p_price = Entry(Add_CartFrame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow",state="readonly").place(x=230,y=35,width=150,height=22)

        label_p_qty = Label(Add_CartFrame,text="Qty",font=("goudy old style",15,"bold")).place(x=420,y=5)
        txt_p_qty = Entry(Add_CartFrame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=420,y=35,width=150,height=22)

        self.label_p_InStock = Label(Add_CartFrame,text="In Stock",font=("goudy old style",15,"bold"))
        self.label_p_InStock.place(x=5,y=70)

        btn_clear = Button(Add_CartFrame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=100)
        btn_add = Button(Add_CartFrame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=100)

        ########################  Billing Area #################

        BillFrame = Frame(self.root,bd=2,relief=RIDGE)
        BillFrame.place(x=1055,y=110,width=530,height=530)
        Btitle = Label(BillFrame,text="Customer Bills", font=("times new roman",20,"bold"),bg="#FF4500",fg="white").pack(side=TOP,fill=X)
        scrolly = Scrollbar(BillFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area = Text(BillFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        

          ########################  Billing Buttons #################

        BillBtnFrame = Frame(self.root,bd=2,relief=RIDGE)
        BillBtnFrame.place(x=1055,y=642,width=530,height=230)

        self.label_amount = Label(BillBtnFrame,text="Bill Amount\n[0]",cursor="hand2",font=("goudy old style",15,"bold"),bg="#1E90FF")
        self.label_amount.place(x=20,y=5,width=150,height=100)
        
        self.label_disc = Label(BillBtnFrame,text="Discount\n[5%]",cursor="hand2",font=("goudy old style",15,"bold"),bg="#9ACD32")
        self.label_disc.place(x=180,y=5,width=150,height=100)
        
        self.label_netpay = Label(BillBtnFrame,text="Net Pay\n[0]",cursor="hand2",font=("goudy old style",15,"bold"),bg="#CCCC00")
        self.label_netpay.place(x=338,y=5,width=150,height=100)
        
        self.label_print = Label(BillBtnFrame,text="Print",cursor="hand2",font=("goudy old style",15,"bold"),bg="#C0C0C0")
        self.label_print.place(x=20,y=110,width=150,height=100)
        
        self.label_clear_all = Button(BillBtnFrame,text="Clear All",command=self.clear_all,cursor="hand2",font=("goudy old style",15,"bold"),bg="#8A2BE2")
        self.label_clear_all.place(x=180,y=110,width=150,height=100)
        
        self.label_generate = Button(BillBtnFrame,text="Generate",command=self.generate_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="#008080")
        self.label_generate.place(x=338,y=110,width=150,height=100)
        self.show()
        
        #Footer
        labl_footer = Label(self.root, text="Spare Parts Management System | Developed by BC200200486", font=("times new roman",15),bg="#5F9EA0",fg="white").pack(side=BOTTOM,fill=X)



        ################### ALL Function###############
    def get_input(self,num):
        xnum = self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
    
    def cal_clear(self):
        self.var_cal_input.set("")

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    ################# Show Function
    def show(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            cursor.execute("select pid,Name,Price,QTY,Status from product where Status=='Active'")
            rows = cursor.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("",END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

############### Search
    def search(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search Area Input Should be Required",parent=self.root)
            else:

                cursor.execute("select pid,Name,Price,QTY,Status from product where Name LIKE '%"+self.var_search.get()+"%' and Status=='Active'")
                rows = cursor.fetchall()
                if len(rows) !=0:

                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("",END, values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")   
    
    ######### Get Data from Click
    def get_data(self,ev):
        f=self.product_table.focus()
        content =(self.product_table.item(f))
        row = content["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.label_p_InStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_qty.set('1')
        self.var_stock.set(row[3])

    def get_data_cart(self,ev):
        f=self.cart_table.focus()
        content =(self.cart_table.item(f))
        row = content["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.label_p_InStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])

    ############ Add to Cart

    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Select Product from List",parent=self.root)
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity Required",parent=self.root)
        elif int(self.var_qty.get())> int(self.var_stock.get()):
            messagebox.showerror("Error", "This QTY is not Available")
        else:
            # total_price = int(self.var_qty.get())*float(self.var_price.get())
            # total_price = float(total_price)
            total_price =(self.var_price.get())
            cart_data =[self.var_pid.get(),self.var_pname.get(),total_price,self.var_qty.get(),self.var_stock.get()]
            

            ######### Update Cart
            present ='no'
            index_ =0
            for row in self.var_cart_list:
                if self.var_pid.get()==row[0]:
                    present = 'yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product Already Present Do yoy want to Update | Remove",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.var_cart_list.pop(index_)
                    else:
                        # self.var_cart_list[index_][2]= total_price
                        self.var_cart_list[index_][3]= self.var_qty.get()
            else:

                self.var_cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()
    ############ Bill Update

    def bill_update(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.var_cart_list:
            self.bill_amnt = self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount = ((self.bill_amnt*5)/100)
        self.net_pay= self.bill_amnt - self.discount
        self.label_amount.config(text=f"Bill Amount\n{str(self.bill_amnt)}")
        self.label_netpay.config(text=f"Net Amount\n{str(self.net_pay)}")
        self.CartTitle.config(text=f"Total Product \t {str(len(self.var_cart_list))}")
    
    ########## Show Data into Cart



    def show_cart(self):
    
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.var_cart_list:
                self.cart_table.insert('',END,values=row)
   
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
   
    def generate_bill(self):
        if self.var_name.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","Required Customer Details")
        elif len(self.var_cart_list)==0:
            messagebox.showerror("Error","Add Product to Cart")
        else:
            self.bill_top()
            self.bill_middle()
            self.bill_botom()

            fp = open(f"bill/{str(self.invoice)}.txt",'w')
            fp.write(self.txt_bill_area.get("1.0",END))
            fp.close
            messagebox.showinfo("Successful", "Bill Saved")

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
        bill_top_temp =f'''
\t\t Spare Parts Managment System
\t Ph No. +923154249508, Gujranwala Pakistan
{str("="*60)}
Customer Name : {self.var_name.get()}
Ph No. {self.var_contact.get()}
Bill No. {str(self.invoice)}\t\t\t\t\tDate: {str(time.strftime("%d/%m/%y"))}
{str("="*60)}
Product Name\t\t\t\tQTY\t\t  Price
{str("="*60)}
        '''
        self.txt_bill_area.delete("1.0",END)
        self.txt_bill_area.insert("1.0",bill_top_temp)
        

    def bill_botom(self):
        bill_botom_temp=f'''
{str("="*60)}
Bill Amount \t\t\t\t Rs. {self.bill_amnt}
Discount \t\t\t\t Rs. {self.discount}
Net Payment \t\t\t\t Rs. {self.net_pay}
{str("="*60)}
'''
        self.txt_bill_area.insert(END,bill_botom_temp)

    def bill_middle(self):
        for row in self.var_cart_list:
            name = (row[1])
            price =float(row[2])*int(row[3])
            price = str(price)
            qty = (row[3])
            self.txt_bill_area.insert(END,"\n "+name+"\t\t\t\t "+qty+"\t\t Rs."+price)
    def clear_cart(self):
        f=self.cart_table.focus()
        content =(self.cart_table.item(f))
        row = content["values"]
        self.var_pid.set("")
        self.var_pname.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.label_p_InStock.config(text=f"In Stock")
        self.var_stock.set("")
    def clear_all(self):
        del self.var_cart_list[:]
        self.clear_cart()
        self.txt_bill_area.delete("1.0",END)
        self.var_name.set("")
        self.var_contact.set("")
        self.CartTitle.config(text=f"Cart \t Total Product: ")
        self.show()
        self.show_cart()
        
        
if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)

    root.mainloop()