from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class CategoryClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+220+130")
        self.root.title("Spare Parts Management System | Developed by BC200200486")
        self.root.focus_force()

        ###### Variables

        self.var_cat_id=StringVar()
        self.var_name= StringVar()

        label_tilte = Label(self.root, text="Product Category", font=("goudy old style",30,"bold"),bg="#1E90FF",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        label_name = Label(self.root,text="Enter Category",font=("goudy old style",20,"bold")).place(x=20,y=100)
        text_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",18) ,bg="lightyellow",width=20,).place(x=20,y=150)
        but_add = Button(self.root, text="ADD",command=self.add, font=("goudy old style",15),bg="#3CB371",fg="white").place(x=300,y=150,height=30,width=150)
        but_delete = Button(self.root, text="DELETE",command=self.delete, font=("goudy old style",15),bg="red",fg="white").place(x=470,y=150,height=30,width=150)

        ######## Category Detail Tree

        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=700,y=100,width=400,height=200)

        scrolly= Scrollbar(cat_frame, orient=VERTICAL)
        scrollx= Scrollbar(cat_frame, orient=HORIZONTAL)

        self.cat_table = ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #Command for Scrolling
        scrollx.config(command=self.cat_table.xview)
        scrolly.config(command=self.cat_table.yview)
        #table Headings
        self.cat_table.heading("cid",text="ID")
        self.cat_table.heading("name",text="Name")
        self.cat_table["show"]="headings"
        # Table Width set
        self.cat_table.column("cid",width=90)
        self.cat_table.column("name",width=100)
        self.cat_table.pack(fill=BOTH,expand=1)
        self.cat_table.bind("<ButtonRelease-1>",self.get_data)


        #### Images

        self.im1 = Image.open("images/suzuki.png")

        self.im1 = self.im1.resize((200,200),Image.LANCZOS)
        self.im1 = ImageTk.PhotoImage(self.im1)
        self.label_im1 = Label(self.root, image=self.im1)
        self.label_im1.place(x=50,y=400)

        self.im2 = Image.open("images/faw.png")

        self.im2 = self.im2.resize((200,200),Image.LANCZOS)
        self.im2 = ImageTk.PhotoImage(self.im2)
        self.label_im2 = Label(self.root, image=self.im2)
        self.label_im2.place(x=300,y=400)

        self.im3 = Image.open("images/honda.png")

        self.im3 = self.im3.resize((200,200),Image.LANCZOS)
        self.im3 = ImageTk.PhotoImage(self.im3)
        self.label_im3 = Label(self.root, image=self.im3,relief=RAISED)
        self.label_im3.place(x=500,y=400)

        self.im4 = Image.open("images/toyota.png")

        self.im4 = self.im4.resize((200,200),Image.LANCZOS)
        self.im4 = ImageTk.PhotoImage(self.im4)
        self.label_im4 = Label(self.root, image=self.im3)
        self.label_im4.place(x=700,y=400)
        self.show()
############## Add Category
    def add(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            if self.var_name.get()== "":
                messagebox.showerror("Error", "Name must be required",parent = self.root)
            else:
                cursor.execute("select * from category where name=?",(self.var_name.get(),))
                row=cursor.fetchone()
                if row !=None:
                    messagebox.showerror("Error", "Category already Present, Try Different")
                else:
                    cursor.execute("insert into category(name) values(?)",(

                                                                    
                                                                    self.var_name.get(),
                    ))                                          

                    conn.commit()
                    messagebox.showinfo("Successfull","Category Saved",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
     ################### Show Data in Tree view
    def show(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()

        try:
            cursor.execute("select * from category")
            rows = cursor.fetchall()
            self.cat_table.delete(*self.cat_table.get_children())
            for row in rows:
                self.cat_table.insert("",END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")       

    def get_data(self,ev):
        f=self.cat_table.focus()
        content =(self.cat_table.item(f))
        row = content["values"]
            
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1])
    ######## Delete Funtion
    def delete(self):
        conn = sqlite3.connect(database=r'store.db')
        cursor = conn.cursor()
        try:
            if self.var_cat_id.get()== "":
                messagebox.showerror("Error", "Select Category From the List",parent = self.root)
            else:
                cursor.execute("select * from category where cid=?",(self.var_cat_id.get(),))
                row=cursor.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Please Try Again.")
                else:
                    op = messagebox.askyesno("Confirm","Do you Realy want to Delete ?",parent=self.root)
                    if op ==TRUE:

                        cursor.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Successful","Category Deleted",parent=self.root)

                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = CategoryClass(root)

    root.mainloop()