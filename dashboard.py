from tkinter import *
from PIL import Image ,ImageTk
from employee import EmployeeClass
from supplier import SupplierClass
from category import CategoryClass
from product import ProductClass
from sales import SalesClass
from billing import BillClass

class SP:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1650x950+0+0")
        self.root.title("Spare Parts Management System | Developed by BC200200486")

        self.icon_title = PhotoImage(file="images/logo2.png")


        #title....
        title = Label(self.root, text="Spare Parts Management System", image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#87CEFA",fg="#000000",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #logout button
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#FFFF00", cursor="hand2").place(x=1350,y=10,height=50,width=150)

        #Clock
        self.labl_clock = Label(self.root, text="Welcome to Spare Parts Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15),bg="#5F9EA0",fg="white")
        self.labl_clock.place(x=0,y=70,relwidth=1,height=30)

        # Left Menu
        self.MenuLogo=Image.open("images/store.png")
        self.MenuLogo = self.MenuLogo.resize((200, 150), Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE,bg="lightblue")
        LeftMenu.place(x=0,y=102,width=200,height=700)

        label_Menulogo = Label(LeftMenu,image=self.MenuLogo)
        label_Menulogo.pack(side=TOP,fill=X)
        label_menu = Label(LeftMenu, text="Menu",font=("times new roman",20),bg="#008080").pack(side=TOP,fill=X)
       
        Menu_Products = Button(LeftMenu, text="Products",command=self.product,font=("times new roman",20,"bold"),bg="#1E90FF",bd=2, cursor="hand2").pack(side=TOP,fill=X,pady=4)
        Menu_Category = Button(LeftMenu, text="Gategory",command=self.category,font=("times new roman",20,"bold"),bg="#1E90FF",bd=2, cursor="hand2").pack(side=TOP,fill=X,pady=4)
        Menu_employee = Button(LeftMenu, text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="#1E90FF",bd=2, cursor="hand2").pack(side=TOP,fill=X,pady=4)
        Menu_Suppplier = Button(LeftMenu, text="Supplier",command=self.supplier,font=("times new roman",20,"bold"),bg="#1E90FF",bd=2, cursor="hand2").pack(side=TOP,fill=X,pady=4)
        Menu_Sales = Button(LeftMenu, text="Sales",command=self.bill,font=("times new roman",20,"bold"),bg="#1E90FF",bd=2, cursor="hand2").pack(side=TOP,fill=X,pady=4)
        Menu_Reports = Button(LeftMenu, text="Reports",command=self.sales,font=("times new roman",20,"bold"),bg="#1E90FF",bd=2, cursor="hand2").pack(side=TOP,fill=X,pady=4)
        Menu_Exit = Button(LeftMenu, text="Exit",font=("times new roman",20,"bold"),bg="#1E90FF",bd=2, cursor="hand2").pack(side=TOP,fill=X,pady=4)

        #Center Content
        self.label_employee=Label(self.root,text="Total Employee\n[0] ",bg="#3CB371",bd=5,relief=RIDGE,fg="white",font=("times new roman",25,"bold"))
        self.label_employee.place(x=300,y=120,width=300,height=150)

        self.label_product=Label(self.root,text="Total Products\n[0] ",bg="#3CB371",bd=5,relief=RIDGE,fg="white",font=("times new roman",25,"bold"))
        self.label_product.place(x=650,y=300,width=300,height=150)

        self.label_category=Label(self.root,text="Total Categories\n[0] ",bg="#3CB371",bd=5,relief=RIDGE,fg="white",font=("times new roman",25,"bold"))
        self.label_category.place(x=1000,y=120,width=300,height=150)

        self.label_supplier=Label(self.root,text="Total Suppliers\n[0] ",bg="#3CB371",bd=5,relief=RIDGE,fg="white",font=("times new roman",25,"bold"))
        self.label_supplier.place(x=300,y=300,width=300,height=150)

        self.label_sale=Label(self.root,text="Total Sale\n[0] ",bg="#3CB371",bd=5,relief=RIDGE,fg="white",font=("times new roman",25,"bold"))
        self.label_sale.place(x=650,y=120,width=300,height=150)
        

        #Footer
        labl_footer = Label(self.root, text="Spare Parts Management System \n Developed by BC200200486", font=("times new roman",15),bg="#5F9EA0",fg="white").pack(side=BOTTOM,fill=X)
#============================================================================================================================================================================
    ##### Employee Class
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = EmployeeClass(self.new_win)
    ###### Supplier Class

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SupplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CategoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ProductClass(self.new_win)
    
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SalesClass(self.new_win)
    def bill(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BillClass(self.new_win)
        


if __name__ == "__main__":
    root = Tk()
    obj = SP(root)

    root.mainloop()