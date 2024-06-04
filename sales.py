from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class SalesClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+220+130")
        self.root.title("Spare Parts Management System | Developed by BC200200486")
        self.root.focus_force()
        self.var_invoice = StringVar()

    #Title
        lable_title=Label(self.root,text="Customer Bill", font=("goudy old style",20), bg="#808080",fg="white").place(x=10,y=10,width=1170)
        label_invoice = Label(self.root, text="Invoice No.", font=("times new roman",15)).place(x=50,y=50)
        text_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman",15),bg="lightyellow").place(x=160,y=50,width=180,height=28)

        #Button
        but_search = Button(self.root,text="Search",command=self.search, font=("time new roman",15),bg="#1E90FF",fg="white").place(x=360,y=50,width=120,height=28)
        but_clear = Button(self.root,text="Clear", font=("time new roman",15),bg="#808080",fg="white").place(x=490,y=50,width=120,height=28)

        # Frame
        ####### Sale Area
        sales_frame = Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=100,width=300,height=400)

        scrolly = Scrollbar(sales_frame,orient=VERTICAL)

        self.sales_list = Listbox(sales_frame,font=("goudy old style",15),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)

        ######## Bill Area
        
        bill_frame = Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=400,y=100,width=600,height=400)
        lable_title2=Label(bill_frame,text="Bill Area", font=("goudy old style",15),bg="orange").pack(side=TOP,fill=X)
        scrolly2 = Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_list = Text(bill_frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_list.yview)
        self.bill_list.pack(fill=BOTH,expand=1)
        self.show()

############## Functions

    def show(self):
        self.sales_list.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                # self.bill_list.insert(END, i.split('.')[0])

    def get_data(self,ev):
        index_ = self.sales_list.curselection()
        file_name = self.sales_list.get(index_)
        print(file_name)
        self.bill_list.delete("1.0",END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_list.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice No. Should be Required", parent=self.root)
        else:
            if f"{self.var_invoice.get()}.txt" in os.listdir('bill'):
                fp = open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_list.delete('1.0', END)
                for i in fp:
                    self.bill_list.insert(END, i)
                fp.close()

if __name__ == "__main__":
    root = Tk()
    obj = SalesClass(root)

    root.mainloop()