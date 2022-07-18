from cProfile import label
from pickle import FRAME
from textwrap import fill
from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
from tkinter import font
class hospital:
    def __init__(self , root):
        
        self.root = root
        self.root.title('Hospital management System ')
        self.root.geometry("1540x800+0+0")
        
        lbtitle = Label(self.root , bd = 10 , relief = RIDGE , text='HOSPITAL MANAGEMENT SYSTEM',fg = 'blue' , bg = 'white', font = ('times new roman' , 50 , 'bold'))
        lbtitle.pack(side =TOP , fill = 'x') 

        #--------------------------------------data frame--------------------------------------
        dataframe = Frame(self.root , bd =5 ,padx=5 ,relief=RIDGE)
        dataframe.place(x = 0 , y = 100 , width=1540 , height=400)

        lablelleft = LabelFrame(dataframe, bd =5 ,padx=5,relief=RIDGE, font = ('times new roman' , 20 , 'bold'),text='Patient Information')
        lablelleft.place(x = 0 , y = 5 , width=900 , height=370)
        
        lablelright = LabelFrame(dataframe, bd =5 ,padx=5,relief=RIDGE, font = ('times new roman' , 20 , 'bold'),text='prescription\'s')
        lablelright.place(x = 905 , y = 5 , width=600 , height=370)

        # ----------------------------- buttons -----------------------------
        buttonframe = Frame(self.root , bd = 5 , padx = 5 , relief=RIDGE)
        buttonframe.place(x = 0 , y = 500 , width=1540 , height=50)

        # ----------------------------- Table -----------------------------
        detailsframe = Frame(self.root , bd = 5 , padx = 5 , relief=RIDGE)
        detailsframe.place(x = 0 , y = 550 , width=1540 , height=240)

        #------------------------------data entries at left------------------
        tablename = Label(lablelleft , text='Tablets Name' ,  font = ('times new roman' , 13 , 'bold') , padx=2 ,pady=5)
        tablename.grid(row = 0,  column=0 ,sticky=W)

        tablet_container = ttk.Combobox(lablelleft , font = ('times new roman' , 13 , 'bold'),width=32)

        tablet_container["values"] = ('Nice' , 'Corona vaccine' , 'Paracitamol' , 'Electrol powder' ,'Iodex', 'Croseen')
        tablet_container.grid(row=0 , column=1)


        list_of_entries = ['Patient Name:','Date Of Birth:' , 'Address:' ,'Patient Id:' ,'Contact Number:' , 'Relative Name:', 'Relative Contact:','Refrence no:','Further Info:']
        for i in range(len(list_of_entries)):
            self.inputs_label(lablelleft, list_of_entries[i], i+1,0)
            
        list_of_entries = ['Dose:' , 'Number of Tablets:' , 'Issue Date:' , 'Expire Date:' ,'Storage Advice:', 'Daily dose:' , 'Side Effect:','Medication:']
        for i in range(len(list_of_entries)):
            self.inputs_label(lablelleft, list_of_entries[i], i,2)

    def inputs_label(self, labelfeild ,feild , row_no,column_no):

        tablename = Label(labelfeild , text=feild ,  font = ('times new roman' , 13 , 'bold') , padx=2 ,pady=5)
        tablename.grid(row = row_no,  column=column_no ,sticky=W)
        txtbox = Entry(labelfeild, font = ('times new roman' , 13 , 'bold'),width=33)
        txtbox.grid(row = row_no,  column=column_no+1)





root = Tk()
obj = hospital(root)
root.mainloop()
