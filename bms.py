import time as t
import datetime

class Order:

    def __init__(self, name = 1 , order = 1 , quantity = 1 ):

        
        self.time = t.strftime('%H:%M:%S')


        self.name = name
        self.order = order
        self.quantity = quantity

    def __repr__(self):

        return f"Order --> \nName : {self.name}\nOrder : {self.order}\nQuantity : {self.quantity} \n"




class OrderList:

    today = datetime.date.today()
    

    def __init__(self):

        # Just keep increamenting order ID by 1 as new order is added
        self.count = 0
        self.orderID = 1100

        # lists for storing data into dictionary
        self.sr_list = []
        self.orderID_list = []
        self.name_list = []
        self.order_list = []
        self.quantity_list = []
        

        # serial number ; orders stores Order object
        self.data = {'SrNo' : self.sr_list, 'OrderID' : self.orderID_list ,'Name' : self.name_list, 'Order' : self.order_list,'Quantity': self.quantity_list }
        


    def add(self , OrderObject):

        #create order object
        CurrentOrder = Order()

        CurrentOrder.name = OrderObject.name
        CurrentOrder.order = OrderObject.order
        CurrentOrder.quantity = OrderObject.quantity

        #take inputs for data in order object
        """CurrentOrder.name = input('Enter Name : ')
        CurrentOrder.order = input('Enter Order : ')
        CurrentOrder.quantity = input('Enter Quantity : ')"""

        #set orderID
        self.orderID = self.orderID + 1




        # store it into data
        self.data['SrNo'] = self.sr_list.append(self.count+1) #appending count+1 
        self.data['OrderID'] = self.orderID_list.append(self.orderID) #appending orderID
        self.data['Order'] = self.order_list.append(OrderObject.order) # appending current object
        self.data['Name'] = self.name_list.append(CurrentOrder.name) #appending count+1 
        self.data['Quantity'] = self.quantity_list.append(CurrentOrder.quantity) # appending current object

        




        #adding count by one
        self.count += 1

        print('Order Added! Order ID : ', self.orderID)

        return self.data



    def edit(self,order_ID):

        # if orderID is in the list
        orderIDs = self.data.get('OrderID')
        index_number = orderIDs.index((order_ID)) if order_ID in orderIDs else None
        
        if index_number != None:
            # take Edited inputs
            Ed_name = input('Edit Name : ')
            Ed_order = input('Edit Order : ')
            Ed_quantity = input('Edit Quantity : ')
            
            # Edit according to Edited Inputs
            self.name[index_number] = Ed_name
            self.order[index_number] = Ed_order
            self.quantity[index_number] = Ed_quantity

            print('Order Edited')
        else:
            print('Failed to Edit the order')


    def display_list(self):
        # i will do it later once i am done with GUI.
        pass

    def __repr__(self):
        return f'Order List of : {self.today}'
