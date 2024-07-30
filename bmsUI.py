from tkinter import *
import time as t
import datetime
import csv


class UI:   
    
    def __init__(self):


        self.today = datetime.date.today()

        self.main = Tk()
        self.main.title(f'Order List : {self.today}')
        self.main.config(bg='skyblue')

        # csv filename
        self.csv_file_name = f'orders_{self.today}.csv'

        # Data storing
        self.orderID = 1100

        self.orderID_index = None

        self.time_list = []
        self.orderID_list = []
        self.name_list = []
        self.order_list = []
        self.quantity_list = []

        self.data = {'OrderID': self.orderID_list,
                     'Time' : self.time_list,
                     'Name': self.name_list,
                     'Order': self.order_list,
                     'Quantity': self.quantity_list}

        # UI structure

        # Left frame
        self.left_frame = Frame(self.main)
        self.left_frame.config(bg = 'brown')
        self.left_frame.grid(row=0, column=0,padx =10,pady=10)
    
        # Buttons
        add_button = Button(self.left_frame, text='ADD', command=self.add_order)
        add_button.grid(row=1, column=1)

        edit_button = Button(self.left_frame,text='EDIT',command = self.orderID_interface)
        edit_button.grid(row = 2,column =1)

        csv_button = Button(self.left_frame,text='CSV',command = self.make_csv)
        csv_button.grid(row=3,column=1)

        delete_button = Button(self.left_frame,text='DELETE',command = self.delete_orderID_interface)
        delete_button.grid(row = 4,column = 1)

        close_button = Button(self.left_frame, text='CLOSE', command=self.main.destroy)
        close_button.grid(row=5, column=1)

        # Right frame
        self.right_frame = Frame(self.main)
        self.right_frame.grid(row=0, column=1 ,padx =50,pady=10)



        Label(self.right_frame, text='Order ID').grid(row=0, column=0, sticky=W,padx =20,pady=10)
        Label(self.right_frame, text='Time').grid(row=0, column=1, sticky=W,padx =20,pady=10)

        Label(self.right_frame, text='Name').grid(row=0, column=2, sticky=W,padx =20,pady=10)
        Label(self.right_frame, text='Order').grid(row=0, column=3, sticky=W,padx =20,pady=10)
        Label(self.right_frame, text='Quantity').grid(row=0, column=4, sticky=W,padx =20,pady=10)

        self.show_list = [ [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]


        for i in range(5):

            Label(self.right_frame, text= f'{self.show_list[0][i]}').grid(row=i+1 , column=0, sticky=W,padx =20,pady=10)
            Label(self.right_frame, text= f'{self.show_list[0][i]}').grid(row=i+1 , column=1, sticky=W,padx =20,pady=10)

            Label(self.right_frame, text= f'{self.show_list[0][i]}').grid(row=i+1, column=2, sticky=W,padx =20,pady=10)
            Label(self.right_frame, text= f'{self.show_list[0][i]}').grid(row=i+1, column=3, sticky=W,padx =20,pady=10)
            Label(self.right_frame, text= f'{self.show_list[0][i]}').grid(row=i+1 , column=4, sticky=W,padx =20,pady=10)




        self.main.mainloop()



    def right_display(self):

        if len(self.orderID_list) >= 5:
            self.show_list[0] = self.time_list[-1:-5]
            self.show_list[1] = self.orderID_list[-1:-5]
            self.show_list[2] = self.name_list[-1:-5]
            self.show_list[3] = self.order_list[-1:-5]
            self.show_list[4] = self.quantity_list[-1:-5]
        else:
            for i in range(len(self.orderID_list)):
                self.show_list[i] = self.time_list[-1-i]
                self.show_list[i] = self.orderID_list[-1-i]
                self.show_list[i] = self.name_list[-1-i]
                self.show_list[i] = self.order_list[-1-i]
                self.show_list[i] = self.quantity_list[-1-i]


    ## add method link
    def add_order(self):
        order_window = Toplevel(self.main)
        order_window.title('Order')

        # Labels
        Label(order_window, text='Name').grid(row=1, column=1, sticky=W)
        Label(order_window, text='Order').grid(row=2, column=1, sticky=W)
        Label(order_window, text='Quantity').grid(row=3, column=1, sticky=W)

        # Inputs
        self.name_var = StringVar()
        self.order_var = StringVar()
        self.quantity_var = StringVar()

        Entry(order_window, textvariable=self.name_var, justify=RIGHT).grid(row=1, column=2)
        Entry(order_window, textvariable=self.order_var, justify=RIGHT).grid(row=2, column=2)
        Entry(order_window, textvariable=self.quantity_var, justify=RIGHT).grid(row=3, column=2)

        # Buttons
        add_button = Button(order_window, text='ADD', command=self.on_add)
        add_button.grid(row=4, column=1)
        close_button = Button(order_window, text='CLOSE', command=order_window.destroy)
        close_button.grid(row=4, column=2)

    def on_add(self):
        name = self.name_var.get()
        order = self.order_var.get()
        quantity = self.quantity_var.get()

        self.add(name, order, quantity)

    def add(self, name, order, quantity):

        self.time_list.append(t.strftime('%H:%M:%S'))
        self.orderID_list.append(self.orderID)
        self.name_list.append(name)
        self.order_list.append(order)
        self.quantity_list.append(quantity)


        
        print('Order Added. OrderID:', self.orderID)
        print('Name:', name)
        print('Order:', order)
        print('Quantity:', quantity)
        self.orderID += 1

        self.right_display()
    ##



    ## edit methods link    
    def orderID_interface(self):

        window = Toplevel(self.main)
        window.title('OrderID')

        Label(window , text = 'Enter Order ID').grid(row=0,column=0)

        self.orderID_index = StringVar()
        
        Entry(window, textvariable=self.orderID_index, justify=RIGHT).grid(row=0, column=1)

        #buttons

        enter_button = Button(window,text='ENTER',command=self.edit_with_index)
        enter_button.grid(row=1,column=0)

        cancel_button = Button(window,text='CANCEL',command = window.destroy)
        cancel_button.grid(row=1,column =1)

    def edit_order(self):
        
        # window for editing the order
        edit_window = Toplevel(self.main)
        edit_window.title('Edit Order')

        Label(edit_window, text='Name').grid(row=1, column=1, sticky=W)
        Label(edit_window, text='Order').grid(row=2, column=1, sticky=W)
        Label(edit_window, text='Quantity').grid(row=3, column=1, sticky=W)

        # original values
        Label(edit_window, text=f'{self.name_list[self.index_number]}').grid(row=1, column=2, sticky=W)        
        Label(edit_window, text=f'{self.order_list[self.index_number]}').grid(row=2, column=2, sticky=W)
        Label(edit_window, text=f'{self.quantity_list[self.index_number]}').grid(row=3, column=2, sticky=W)


        # Inputs
        self.edit_name = StringVar()
        self.edit_order = StringVar()
        self.edit_quantity = StringVar()

        Entry(edit_window, textvariable=self.edit_name, justify=RIGHT).grid(row=1, column=3)
        Entry(edit_window, textvariable=self.edit_order, justify=RIGHT).grid(row=2, column=3)
        Entry(edit_window, textvariable=self.edit_quantity, justify=RIGHT).grid(row=3, column=3)


        # Buttons
        edit_button = Button(edit_window, text='EDIT', command=self.on_edit)
        edit_button.grid(row=4, column=1)
        close_button = Button(edit_window, text='CANCEL', command=edit_window.destroy)
        close_button.grid(row=4, column=2)

    def on_edit(self):

        name = self.edit_name.get()        
        order = self.edit_order.get()
        quantity = self.edit_quantity.get()

        self.edit(name, order, quantity)

    def edit(self,name ,order,quantity):

        self.name_list[self.index_number] = name        
        self.order_list[self.index_number] = order
        self.quantity_list[self.index_number] = quantity


        self.right_display()


    def edit_with_index(self):

        self.index_number = int(self.orderID_index.get())

        self.index_number = self.orderID_list.index(self.index_number) if self.index_number in self.orderID_list else None

        if self.index_number != None:

            self.edit_order()

        else:
            print('NO order found !')
    ##


    ## make into csv methods

    def make_csv(self):
       field_names = self.data.keys()
       
       # opening file for writing

       with open(self.csv_file_name,mode='w',newline='') as file:

           writer = csv.writer(file)

           # header
           writer.writerow(field_names)

           #writing main data

           for i in range(len(self.data['OrderID'])):
               row = [self.data[key][i] for key in field_names]
               writer.writerow(row)

    ##



    ## delete order methods link  
    def delete_orderID_interface(self):

        window = Toplevel(self.main)
        window.title('OrderID')

        Label(window , text = 'Enter Order ID').grid(row=0,column=0)

        self.delete_orderID_index = StringVar()
        
        Entry(window, textvariable=self.delete_orderID_index, justify=RIGHT).grid(row=0, column=1)

        #buttons

        enter_button = Button(window,text='DELETE',command=self.delete_with_index)
        enter_button.grid(row=1,column=0)

        cancel_button = Button(window,text='CANCEL',command = window.destroy)
        cancel_button.grid(row=1,column =1)


    def delete_with_index(self):

        self.delete_index_number = int(self.delete_orderID_index.get())

        self.delete_index_number = self.orderID_list.index(self.delete_index_number) if self.delete_index_number in self.orderID_list else None

        if self.delete_index_number != None:

            self.delete_order()

        else:
            print('NO order found !')


    def delete_order(self):
        
        del self.name_list[self.delete_index_number]      
        del self.order_list[self.delete_index_number]
        del self.quantity_list[self.delete_index_number]
        del self.time_list[self.delete_index_number]      
        del self.orderID_list[self.delete_index_number]

        print('Order Deleted successfully')

        self.right_display()
    
    ##




# Create and run the UI
ui = UI()
