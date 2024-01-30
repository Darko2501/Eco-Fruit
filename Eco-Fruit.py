from tkinter import*
from tkinter import ttk
import pandas as pd
import psycopg2 as psycopg2
import matplotlib.pyplot as plt
import pyautogui as pg
from psycopg2 import Error

root=Tk()

root.title("ECO-FRUIT")
meni=Menu(root)
podmeni1=Menu(meni,tearoff=0)
meni.add_cascade(label="EXCEL FILES",menu=podmeni1)
podmeni1.add_command(label="FRIUT STOCKS",command=lambda:E.stocks_ex())
podmeni1.add_command(label="FRUIT SALES",command=lambda:E.purhased_ex())
podmeni1.add_command(label="FRUIT PURSHASES",command=lambda:E.sold_ex())

podmeni2=Menu(meni,tearoff=0)
meni.add_cascade(label="CHANGES",menu=podmeni2)
podmeni2.add_command(label="ADD IN THE ASSORTMENT",command=lambda:top1())
podmeni2.add_command(label="CANCEL PURCHASE",command=lambda:top2())
podmeni2.add_command(label="CANCEL SALE",command=lambda:top3())

podmeni3=Menu(meni,tearoff=0)
meni.add_cascade(label="GRAPHIC DISPLAY",menu=podmeni3)
podmeni3.add_command(label="SHOW STOCKS",command=lambda:E.stocks_graph())
podmeni3.add_command(label="SHOW SALES",command=lambda:E.sales_graph())
podmeni3.add_command(label="SHOW PURCHAS",command=lambda:E.purchase_graf())

podmeni4=Menu(meni,tearoff=0)
meni.add_cascade(label="EXIT",menu=podmeni4)
podmeni4.add_command(label="EXIT",command=lambda:E.exit())

columns=('ID_FRUIT','FRUIT','QUANTITY')
t1=ttk.Treeview(root,columns=columns,show='headings')
t1.heading('ID_FRUIT',text='ID FRUIT')
t1.heading('FRUIT',text='FRUIT')
t1.heading('QUANTITY',text='QUANTITY (t)')
t1.grid(row=1,column=0,rowspan=10,columnspan=3)

columns1=('ID','ID_FRUIT','FRUIT','QUANTITY','PRICE_FOR_KG','DATE_OF_INPUT','VALUE_P')
t2=ttk.Treeview(root,columns=columns1,show='headings')
t2.heading('ID',text="ID ")
t2.heading('ID_FRUIT',text='ID FRUIT')
t2.heading('FRUIT',text='FRUIT')
t2.heading('QUANTITY',text='QUANTITY (t)')
t2.heading('PRICE_FOR_KG',text='PRICE FOR KG')
t2.heading('DATE_OF_INPUT',text='DATE OF INPUT')
t2.heading('VALUE_P',text='VALUE')
t2.grid(row=15,column=0,rowspan=3,columnspan=7)

l1=Label(root,text="ID FRUIT")
l1.grid(row=19,column=0)
l2=Label(root,text="FRUIT")
l2.grid(row=19,column=1)
l3=Label(root,text="QUANTITY (t)")
l3.grid(row=19,column=2)
l4=Label(root,text="PRICE (kg)")
l4.grid(row=19,column=3)

e1=Entry(root)
e1.grid(row=20,column=0)
e2=Entry(root)
e2.grid(row=20,column=1)
e3=Entry(root)
e3.grid(row=20,column=2)
e4=Entry(root)
e4.grid(row=20,column=3)

l8=Label(root,text="",fg="black",font=22)
l8.grid(row=0,column=3,columnspan=4,rowspan=7)

b2=Button(root,text='BUY',padx=35,command=lambda:l8.configure(text=E.buy(int(e1.get()),str(e2.get().upper()),float(e3.get()),float(e4.get()))))
b2.grid(row=19,column=5)
b3=Button(root,text='SELL',padx=30,command=lambda:l8.configure(text=E.sell(int(e1.get()),str(e2.get().upper()),float(e3.get()),float(e4.get()))))
b3.grid(row=20,column=5)

l5=Label(root,text='PURCHASED FRUITS',font=22,fg='blue')
l5.grid(row=14,column=0,columnspan=7)

l6=Label(root,text='STOCKS OF FRUITS',font=22,fg='blue')
l6.grid(row=0,column=0,columnspan=3)

columns2=('ID','ID_FRUIT','FRUIT','QUANTITY','PRICE_FOR_KG','DATE_OF_SALE','VALUE_S')
t3=ttk.Treeview(root,columns=columns2,show='headings')
t3.heading('ID',text="ID ")
t3.heading('ID_FRUIT',text='ID FRUIT')
t3.heading('FRUIT',text='FRUIT')
t3.heading('QUANTITY',text='QUANTITY(t)')
t3.heading('PRICE_FOR_KG',text='PRICE  (kg)')
t3.heading('DATE_OF_SALE',text='DATE OF SALE')
t3.heading('VALUE_S',text='VALUE')
t3.grid(row=22,column=0,rowspan=3,columnspan=7)

l7=Label(root,text='SALE OF FRUITS',font=22,fg='blue')
l7.grid(row=21,column=0,columnspan=7)
root.configure(menu=meni)
def top1():
    t=Toplevel()
    l1=Label(t,text="ENTER NEW FRUIT")
    l1.pack()
    e1=Entry(t)
    e1.pack()
    b=Button(t,text="OK",command=lambda:l8.configure(text=E.add_f(e1.get().upper())))
    b.pack()
def top2():
    t=Toplevel()
    l1=Label(t,text="ENTER THE PURCHASE ID FOR CANCEL")
    l1.pack()
    e1=Entry(t)
    e1.pack()
    l2=Label(t,text="ENTER ID OF FRUIT")
    l2.pack()
    e2=Entry(t)
    e2.pack()
    l3=Label(t,text="ENTER QUANTITY (t)")
    l3.pack()
    e3=Entry(t)
    e3.pack()
    b=Button(t,text="OK",command=lambda:l8.configure(text=E.cancel_f(int(e1.get()),int(e2.get()),float(e3.get()))))
    b.pack()
def top3():
    t=Toplevel()
    l1=Label(t,text="ENTER THE SALE ID FOR CANCEL")
    l1.pack()
    e1=Entry(t)
    e1.pack()
    l2=Label(t,text="ENTER ID FRUIT")
    l2.pack()
    e2=Entry(t)
    e2.pack()
    l3=Label(t,text="ENTER QUANTITY (t)")
    l3.pack()
    e3=Entry(t)
    e3.pack()
    b=Button(t,text="OK",command=lambda:l8.configure(text=E.cancel_s(int(e1.get()),int(e2.get()),float(e3.get()))))
    b.pack()

class ECO:
    def __init__(self):
        self.con=psycopg2.connect(database='Eco-Fruit',
                           port='5432',
                           user='postgres',
                           password='postgres',
                           host='localhost')
        
        self.fruit=None
    def fruits(self):
        cursor=self.con.cursor()
        cursor.execute('SELECT*FROM Stocks;')
        z=cursor.fetchall()
        for i in t1.get_children():
            t1.delete(i)
        for i in z:
            t1.insert('',END,values=i)
        cursor=self.con.cursor()
        cursor.execute('SELECT ID,ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG,DATE_OF_INPUT,QUANTITY*PRICE_FOR_KG*100 AS VALUE_P FROM Purchased;')
        u=cursor.fetchall()
        for i in t2.get_children():
            t2.delete(i)
        for i in u:
            t2.insert('',END,values=i)
        cursor=self.con.cursor()
        cursor.execute('SELECT ID,ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG,DATE_OF_INPUT,QUANTITY*PRICE_FOR_KG*100 AS VALUE_S FROM Sales;')
        p=cursor.fetchall()
        for i in t3.get_children():
            t3.delete(i)
        for i in p:
            t3.insert('',END,values=i)
    def sell(self,ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG):
        try:
            cursor=self.con.cursor()
            cursor.execute('''UPDATE Stocks SET QUANTITY=QUANTITY-{} WHERE ID_FRUIT={};'''.format(QUANTITY,ID_FRUIT))
            self.con.commit()
            cursor=self.con.cursor()
            k=('''INSERT INTO Sales(ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG) VALUES({},'{}',{},{})'''.format(ID_FRUIT, FRUIT, QUANTITY, PRICE_FOR_KG))
            cursor.execute(k)
            self.con.commit()
            self.fruits()
            return "YOU HAVE SCCESSFULLY SOLD\n FRUIT FOR OUR COMPANY\n ID FRUIT:{}\n FRUIT:{}\n QUANTITY:{}(t)\n PRICE:{} ($/kg)".format(ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG)
        except Error as e:
            return("YOU HAVE NOT FILLED IN THE INPUT FIELDS CORRECTLY",e)
    def buy(self,ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG):
        try:
            cursor=self.con.cursor()
            cursor.execute('''UPDATE Stocks SET QUANTITY=QUANTITY+{} WHERE ID_FRUIT={};'''.format(QUANTITY,ID_FRUIT))
            self.con.commit()
            cursor=self.con.cursor()
            k=('''INSERT INTO Purchased(ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG) VALUES({},'{}',{},{})'''.format(ID_FRUIT, FRUIT, QUANTITY, PRICE_FOR_KG))
            cursor.execute(k)
            self.con.commit()
            self.fruits()
            return "YOU HAVE SCCESSFULLY BUY\n FRUIT FOR OUR COMPANY\n ID FRUIT:{}\n FRUIT:{}\n QUANTITY:{}(t)\n PRICE:{} ($/kg)".format(ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG)
        except Error as e:
            return("YOU HAVE NOT FILLED IN THE INPUT FIELDS CORRECTLY",e)
    def stocks_ex(self):
        self.fruit=pd.read_sql_query('SELECT*FROM Stocks;',self.con)
        self.fruit.to_excel('Stocks.xlsx',index=False)
    def purhased_ex(self):
        self.fruit=pd.read_sql_query('SELECT ID,ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG,DATE_OF_INPUT,QUANTITY*PRICE_FOR_KG*100 AS VALUE_P FROM Purchased;',self.con)
        self.fruit.to_excel('Purchased.xlsx',index=False)
    def sold_ex(self):
        self.fruit=pd.read_sql_query('SELECT ID,ID_FRUIT,FRUIT,QUANTITY,PRICE_FOR_KG,DATE_OF_INPUT,QUANTITY*PRICE_FOR_KG*100 AS VALUE_P FROM Sales; ',self.con)
        self.fruit.to_excel('Sales.xlsx',index=False)
    def stocks_graph(self):
        self.fruit=pd.read_sql_query('SELECT*FROM Stocks',self.con)
        l=self.fruit.fruit
        l1=self.fruit.quantity
        plt.figure(figsize=(10,10))
        plt.pie(l1,labels=l,autopct='%1.2f.%%')
        plt.legend(title="STOCKS",loc='upper left')
        plt.show()
    def sales_graph(self):
        self.fruit=pd.read_sql_query('SELECT SUM(QUANTITY*PRICE_FOR_KG*1000)AS VALUE,FRUIT FROM Sales GROUP BY FRUIT;',self.con)
        l=self.fruit.fruit
        l1=self.fruit.value
        plt.bar(l,l1,color='blue',width=0.1)
        plt.xlabel('FRUITS')
        plt.ylabel('VALUE OF SOLD FRUITS ')
        plt.grid()
        plt.show()
    def purchase_graf(self):
        self.fruit=pd.read_sql_query('SELECT SUM(QUANTITY*PRICE_FOR_KG*1000)AS VALUE,FRUIT FROM Purchased GROUP BY FRUIT;',self.con)
        l=self.fruit.fruit
        l1=self.fruit.value
        plt.bar(l,l1,color='red',width=0.1)
        plt.xlabel('FRUITS')
        plt.ylabel('VALUE OF PURCHASED FRUITS')
        plt.grid()
        plt.show()
    def exit(self):
        print(pg.confirm('DO YOU WANT TO EXIT',buttons=['OK'],title='EXIT'))
        if 'OK':
            root.quit()
    def add_f(self,FRUIT):
        
        cursor=self.con.cursor()
        cursor.execute('''INSERT INTO Stocks(FRUIT,QUANTITY) VALUES('{}',0);'''.format(FRUIT))
        self.con.commit()
        self.fruits()
        return"{} HAVE BECOME PART OF \n OUR ASSORTMENT".format(FRUIT)
    def cancel_f(self,ID,ID_FRUIT,QUANTITY):
        try:
            cursor=self.con.cursor()
            cursor.execute('''DELETE FROM  Purchased WHERE ID={};'''.format(ID))
            self.con.commit()
            cursor=self.con.cursor()
            cursor.execute('''UPDATE Stocks SET QUANTITY=QUANTITY - {} WHERE ID_FRUIT={}'''.format(QUANTITY,ID_FRUIT))
            self.con.commit()
            self.fruits()
            return"YOU CANCEL PURCHASED FRUIT\n ID PURCHASED {}".format(ID)
        except Error as e:
            return("YOU HAVE NOT FILLED IN THE INPUT FIELDS CORRECTLY",e)
    def cancel_s(self,ID,ID_FRUIT,QUANTITY):
        try:
            cursor=self.con.cursor()
            cursor.execute('''DELETE FROM Sales WHERE ID={};'''.format(ID))
            self.con.commit()
            cursor=self.con.cursor()
            cursor.execute('''UPDATE Stocks SET QUANTITY=QUANTITY + {} WHERE ID_FRUIT={}'''.format(QUANTITY,ID_FRUIT))
            self.con.commit()
            self.fruits()
            return"YOU CANCEL SALES\n ID OF SALES {}".format(ID)
        except Error as e:
            return("YOU HAVE NOT FILLED IN THE INPUT FIELDS CORRECTLY",e)
    


E=ECO()
E.fruits()
root.mainloop()
