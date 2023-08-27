'''
Create a system usinhg object composition and encapsulation concepts that allpws customers to place orders for products.
The program consits of three classes : Customer ,Order and Product.
The custoner class allows customers to place orders and it stores the customers name email 
The order class represents an individual order with an order ID and a list of products.
The product class stores information about each product including its name and price.
'''


class Customer:
    def __init__(self,name,email):
        self.__name=name #customer name private
        self.__email=email #private
        self.orders=[] #list to store order

    def place_order(self,order):
        self.orders.append(order) #add the order

    def get_orders(self):
        return self.orders #return
    
    def get_name(self):
        return self.__name #getter method to access the private attritube
    
    def get_email(self):
        return self.__email #getter method
    

class Order:
    def __init__(self,order_id,products):
        self.__order_id= order_id #order id(private)
        self.products=products

    def get_order_id(self):
        return self.__order_id #getter method to access the private order_id
    
    def get_total_price(self):
        total_price=0
        for product in self.products:
            total_price=total_price+product.get_price()
        return total_price
    

class Product:
    def __init__(self,name,price):
        self.__name=name #private name
        self.__price=price

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price #getter method to access the private price attribute
    
#creating objects
customer1=Customer("Kartik","kartikj@gmail.com")
customer2=Customer("Ram","ram123@gmail.com")

product1=Product("Iphone",50000)
product2=Product("Galaxyfold",60000)
product3=Product("Pixel",40000)

#placing an order
order1=Order(1,[product1,product2])

customer1.place_order(order1)


#Accessing customer information using the getter methods
print("Customer Name:",customer1.get_name())
print("Customer Email:",customer1.get_email())

#Accessing order information 
orders=customer1.get_orders()
for order in orders:
    print("Order ID:",order.get_order_id())
    print("Products:")
    for product in order.products:
        print(product.get_name() , "RS" ,product.get_price())
        print("Total price:",order.get_total_price())







