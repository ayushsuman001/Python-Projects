import customer
import sys
import mysql.connector as co




# Function for Main Menu




def main_menu(user,passwd):
    print("\n\n\t\t\t.......using the default table customer for further queries.................\n\n")
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    query="""CREATE TABLE `customer` (
  `purchase_id` bigint NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(30) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `phone_no` bigint NOT NULL,
  `address` varchar(50) DEFAULT NULL,
  `purchase_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `rate` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  `item_name` varchar(40) DEFAULT NULL,
  `item_quantity` bigint DEFAULT NULL,
  PRIMARY KEY (`purchase_id`)
)"""

    
    try:
        cursor.execute(query)
    except:
        print("..........Table already exists.........., Using table customer ")

        
    while True:
        print("\t\t\t............................................................................")
        print("\t\t\t............................................................................")
        print("\t\t\t............................................................................")
        print("\t\t\t.......Welcome To Computer Shop Record Management System's MAIN MENU........")
        print("\t\t\t............................................................................")
        print("\t\t\t............................................................................")
        print("\t\t\t............................................................................")
        print("1: Transactions ")
        print("2: Customer's details")
        print("3. Manage Stock")
        print("4: Edit Admin ")
        print("5: Return to Admin log in page")
        print("6: Exit")
        print("\t\t\t----------------------------------------------------------------------------")
        choice=int(input("Enter your choice :  "))
        if choice==1:
            customer.transactions(user,passwd)
        elif choice==2:
            customer.customer_details(user,passwd)
        elif choice==3:
            customer.stock(user,passwd)
        elif choice==4:
            customer.admin_login(user,passwd)
        elif choice==5:
            break
        elif choice==6:
            sys.exit()
        else:
            print("ERROR: Invalid Choice Try again...")

            

# function for transactions




def transactions(user,passwd):
    print("\n\n\t\t\t.......using the default table customer for further queries.................\n\n")
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    print("1: purchase an item")
    print("2: See all transaction ")
    print("3: Back to main menu")
    print("4: Exit the program")
    choice=int(input("Enter your choice from the above options: "))
    while True:
        if choice==1:
            customer.purchase(user,passwd)
        elif choice==2:
            customer.all_transactions(user,passwd)
        elif choice==3:
            break
        elif choice==4:
            sys.exit()
        else:
            print("\n\n\t\t\t..................Enter a valid choice.................\n\n")




# Function for purchasing items




def purchase(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    p='y'
    cart=0
    while p=='y':
        customer_name=input("Enter customer's name : ")
        address=input("Enter address : ")
        phone_no=int(input("Enter phone number : "))
        email=input("Enter email address : ")
        item_name=input("Enter the name of product : ")
        item_quantity=int(input("Enter product's quantity : "))
        rate=float(input("Enter the rate of product: "))
        price=float(rate*item_quantity)
        query="insert into customer(customer_name,address,phone_no,email,item_name,item_quantity,rate,price) values('{}','{}',{},'{}','{}',{},{},{})".format(customer_name,address,phone_no,email,item_name,item_quantity,rate,price)
        cursor.execute(query)
        mycon.commit()
        cart+=price
        print("Total amount to be paid: ",cart)
        p=input("To add more products press .......y........ else press .........n........")
        if p=="n":
            break
    query1="select purchase_id from customer where customer_name='{}' and address='{}' and phone_no={} and email='{}'".format(customer_name,address,phone_no,email)
    cursor.execute(query1)
    print("\n\n\t\t\tYour purchase ID is : ",cursor.fetchall()[0][0],"\n\n")
    print("Records have been saved successfully\n\n")
    mycon.close()
    cursor.close()
    customer.transactions(user,passwd)    




# function for viewing all transactions




def all_transactions(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    query="Select * from customer"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print("\n",row,"\n")
    mycon.commit()
    mycon.close()
    cursor.close()
    customer.transactions(user,passwd)

    



# function for customer details




def customer_details(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    while True:
        print("1: Search for a customer")
        print("2: Edit customer details")
        print("3: Delete customer data")
        print("4: Return to main menu")
        print("5: Exit")
        choice=int(input("Enter your choice from the above options: "))
        if choice==1:
            customer.search(user,passwd)
        elif choice==2:
            customer.edit(user,passwd)
        elif choice==3:
            customer.delete_customer(user,passwd)
        elif choice==4:
            customer.main_menu(user,passwd)
        elif choice==5:
            sys.exit()
    cursor.close()
    mycon.close()




# function for searching for customer




def search(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    purchase_id=int(input("Enter your purchase ID: "))
    query="Select * from customer where purchase_id={}".format(purchase_id)
    cursor.execute(query)
    data=cursor.fetchall()
    print("\n\n\t\t\t name = ",data[0][1])
    print("\t\t\t email = ",data[0][2])
    print("\t\t\t phone no. = ",data[0][3])
    print("\t\t\t address = ",data[0][4])
    print("\t\t\t purchase date ,time = ",data[0][5])
    print("\t\t\t purchase_id = ",data[0][0],"\n\n")
    cursor.close()
    mycon.close()



    
# function for editing cutomer's details




def edit(user,passwd):
    print("""\t\t\t.........................................Select your choice from the options below....................................""")
    print(" 1: Edit the name of customer ")
    print(" 2: Edit address ")
    print(" 3: Edit phone number")
    print(" 4: Edit email of the customer")
    print(" 5: Return to main menu")
    print(" 6: Exit")
    choice=int(input("Enter your choice from the above options : "))
    while True:
        if choice==1:
            customer.edit_name(user,passwd)
        elif choice==2:
            customer.edit_address(user,passwd)
        elif choice==3:
            customer.edit_phone_number(user,passwd)
        elif choice==4:
            customer.edit_email(user,passwd)
        elif choice==5:
            customer.main_menu(user,passwd)
        elif choice==6:
            sys.exit(user,passwd)
        else:
            print("ERROR:Invalid input ")
            



# function for editing cutomer's name




def edit_name(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    purchase_id=int(input("Enter your purchase_id : "))
    name=input("Enter the correct name : ")
    query="update customer set customer_name='{}' where purchase_id={}".format(name,purchase_id)
    cursor.execute(query)
    print("\n\n*****************your name has been updated***********\n\n")
    mycon.commit()
    mycon.close()
    cursor.close()
    customer.main_menu(user,passwd)
    



# function for editing cutomer's address




def edit_address(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    purchase_id=int(input("Enter your purchase_id : "))
    address=input("Enter the correct address : ")
    query="update customer set address='{}' where purchase_id={}".format(address,purchase_id)
    cursor.execute(query)
    print("\n\n*****************your address has been updated***********\n\n")
    mycon.commit()
    mycon.close()
    cursor.close()
    customer.main_menu(user,passwd)


    

# function for editing customer's phone number




def edit_phone_number(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    purchase_id=int(input("Enter your purchase_id : "))
    phone_no=input("Enter the correct phone number : ")
    query="update customer set phone_no={} where purchase_id={}".format(phone_no,purchase_id)
    cursor.execute(query)
    print("\n\n*****************your phone_no has been updated***********\n\n")
    mycon.commit()
    mycon.close()
    cursor.close()
    customer.main_menu(user,passwd)


    

# function for editing cutomer's email address




def edit_email(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    purchase_id=int(input("Enter your purchase_id : "))
    email=input("Enter the correct email address : ")
    query="update customer set email= '%s' where purchase_id=%s"%(email,purchase_id)
    cursor.execute(query)
    print("\n\n*****************your email has been updated***********\n\n")
    mycon.commit()
    mycon.close()
    cursor.close()
    customer.main_menu(user,passwd)




# Function for deleting customer details




def delete_customer(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    purchase_id=int(input("Enter your purchase_id : "))
    query="delete from customer where purchase_id={}".format(purchase_id)
    try:
        cursor.execute(query)
        print("\n\n*****************Customer data succesfully removed from database***********\n\n")
        mycon.commit()
    except:
        print("\n\nAn error occured while removing customer from database")
        customer.customer_details(user,passwd)
    mycon.close()
    cursor.close()
    customer.customer_details(user,passwd)
    
    
        
    
# function for managing stock




def stock(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    query1="""CREATE TABLE `stock` (
  `pname` varchar(30) DEFAULT NULL,
  `quantity` bigint DEFAULT NULL,
  `price` float DEFAULT NULL,
  `amount` bigint DEFAULT NULL
)"""
    try:
        cursor.execute(query1)
        print("\n\n\t\t\tTable stock created successfully\n\n")
    except:
        print("\n\n\t\tTable stock already exists , Using it for furthwe queries\n\n")
    p='y'
    print("1. For adding item in stock")
    print("2. For remove items from stock")
    print("3. View stock")
    print("4. Back to Main Menu")
    print("5: Exit")
    print("\n\n\t\t\t....................Using default table stock.....................\n\n")
    query="""CREATE TABLE `stock` (
  `pname` varchar(30) DEFAULT NULL,
  `quantity` bigint DEFAULT NULL,
  `price` float DEFAULT NULL
)"""
    try:
        cusrsor.execute(query)
    except:
        print("\n\n\t\t\tdatabase already exists, using the existing database\n\n") 
    choice=int(input("\nEnter your choice from the above options: "))
    while True:
        if choice==1:
            customer.add_stock(user,passwd) 
        elif choice==2:
            customer.remove_stock(user,passwd)
        elif choice==3:
            customer.view_stock(user,passwd)
        elif choice==4:
            customer.main_menu(user,passwd)
        elif choice==5:
            sys.exit()
        else:
            print("\n\n\t ERROR!  Enter a valid choice\n\n")
            customer.main_menu()
    mycon.commit()
    cursor.close()
    mycon.close()



# Function for adding stock




def add_stock(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    p='y'
    while p=='y':
        pname=input("Enter the name of product : ")
        quantity=int(input("Enter the quantity of product : "))
        price=float(input("Enter the price of each product: "))
        amount=price*quantity
        query="insert into stock(pname,quantity,price,amount) values('{}',{},{},{})".format(pname,quantity,price,amount)
        cursor.execute(query)
        p=input("To add more products press .......y........ else press .........n........")
        mycon.commit()
        if p=='n':
            print("Records has been saved in stock table")
            customer.stock(user,passwd)
    mycon.close()
    cursor.close()
    print("Records has been saved in stock table")




# function for removing stock




def remove_stock(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    p='y'
    while p=='y':
        pname=input("Enter the name of product : ")
        query="delete from stock where pname='{}'".format(pname)
        cursor.execute(query)
        p=input("To remove more products press .......y........ else press .........n........")
        mycon.commit()
        if p=='n':
            customer.stock(user,passwd)        
    mycon.close()
    cursor.close()
    print("Records has been saved in stock table")




# function for viewing stock




def view_stock(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    query="select * from stock"
    try:
        cursor.execute(query)
        data=cursor.fetchall()
        for row in data:
            print("\n\n\t\t\t" ,row)
    except:
        print("Unexpected error occured")
        customer.stock(user,passwd)
    cursor.close()
    mycon.close()
    customer.stock(user,passwd)





# function for managing/editing ADMIN
    



def admin_login(user,passwd):
    print("\n\n\t\t\t")
    print("1: Add admin")
    print("2: Change admin username")
    print("3: Remove an admin")
    print("4: Change admin password")
    print("5: Back to Main Menu")
    print("6: Exit ")
    print("\n\n")
    choice=int(input("Enter your choice from the above options: \n\n"))
    while True:
        if choice==1:
            customer.add_admin(user,passwd)
        elif choice==2:
            customer.admin_username(user,passwd)
        elif choice==3:
            customer.admin_remove(user,passwd)
        elif choice==4:
            customer.admin_password(user,passwd)
        elif choice==5:
            customer.main_menu(user,passwd)
        elif choice==6:
            sys.exit(user,passwd)
        else:
            print("\n\n\t ERROR!  Enter a valid choice\n\n")
            break



# function for adin admin




def add_admin(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    id_=str(input("Enter your username: "))
    passwd=str(input("Enter your PIN: "))
    conf=str(input("Confirm your PIN: "))
    if passwd==conf:
        query="insert into admin values('{}','{}')".format(id_,passwd)
        try:
            cursor.execute(query)
            mycon.commit()
            print("\n\n\t\t\tUser succesfully added : ",id_,"\n\n")
            customer.admin_login(user,passwd)
        except():
            print("!!!!!........Failed to add user.......Please try again later...!!!!!")
            customer.admin_login(user,passwd)
        mycon.close()
        cursor.close()
    else:
        print("\n\n\t\t\t.....................PIN doesn't match ................... TRY AGAIN\n\n")
        customer.admin_login(user,passwd)
        



# function for changing admin username




def admin_username(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    id_=str(input("Enter your current username: "))
    new_id_=str(input("Enter your new username: "))
    query="update admin set id_='{}' where id_='{}'".format(new_id_,id_)
    try:
        cursor.execute(query)
        mycon.commit()
        print("\n\n\t\t\tUsername succesfully changed to: ",new_id_,"\n\n")
        customer.admin_login(user,passwd)
    except():
        print("!!!!!........Failed to update username.......Please try again later...!!!!!")
        customer.admin_login(user,passwd)
    mycon.close()
    cursor.close()




# function fo removing admin




def admin_remove(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    id_=str(input("Enter the admin username to be removed: "))
    query="delete from admin where id_='{}'".format(id_)
    try:
        cursor.execute(query)
        mycon.commit()
        print("\n\n\t\t\tUser succesfully removed\n\n")
        customer.admin_login(user,passwd)
    except():
        print("!!!!!........Failed to remove user.......Please try again later...!!!!!")
        customer.admin_login(user,passwd)
    mycon.close()
    cursor.close()




# Function for Changing admin password




def admin_password(user,passwd):
    mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
    cursor=mycon.cursor()
    id_=str(input("Enter your current username: "))
    passwd=str(input("Enter your current password: "))
    cursor.execute("select passwd from admin where id_='{}'".format(id_))
    display=cursor.fetchall()
    if(passwd==str(display[0][0])):    
        new_passwd=str(input("Enter your new password: "))
        conf=str(input("Confirm your new password: "))
        if new_passwd==conf:   
            query="update admin set passwd='{}' where id_='{}'".format(new_passwd,id_)
            try:
                cursor.execute(query)
                mycon.commit()
                print("\n\n\t\t\tPassword succesfully changed to: ",new_passwd,"\n\n")
                customer.admin_login(user,passwd)
            except():
                print("!!!!!........Failed to update username.......Please try again later...!!!!!")
                customer.admin_login(user,passwd)
        else:
            print("!!!!!........old password and new passsword doesn't match.......Please try again later...!!!!!")
            customer.admin_login(user,passwd)        
    mycon.close()
    cursor.close()






#   .........................................................................._main_  starts.........................................................................








print("\t\t\t............................................................................")
print("\t\t\t............................................................................")
print("\t\t\t............................................................................")
print("\t\t\t..........Welcome To Computer Shop Record Management System.................")
print("\t\t\t............................................................................")
print("\t\t\t............................................................................")
print("\t\t\t............................................................................")
print("\t\t\t....................You are going to enter ADMIN.............................")


print("\n\n\t\t\t-------------------------------------------------------------------------------\n\n")


user=input("Enter your SQL username: ")
passwd=input("Enter your password: ")
mycon=co.connect(host="localhost",user=user,passwd=passwd)
cursor=mycon.cursor()
query2="create database my_project"
try:
    cursor.execute(query2)
except:
    print("\n\n\t\t\t.........Database already exist , using database my_project..........\n\n")

# Creating the default table admin

mycon=co.connect(host="localhost",user=user,passwd=passwd,database="my_project")
cursor=mycon.cursor()
if mycon.is_connected()==True:
    query="""CREATE TABLE `admin` (
      `id_` varchar(10) DEFAULT NULL,
      `passwd` varchar(20) DEFAULT NULL
    )"""

    query1="insert into admin values('{}','{}')".format('0000','1234')

    try:
        cursor.execute(query)
    except:
        print("\n\n\t\t\t.............Table already exist............\n\n")
        print("\n\n\t\t\t Using the default table admin for further processes\n\n")
    i=1
    cursor.execute(query1)
    while i<5:
        try:
            id_=input("Enter you admin username: ")
            password =str(input("Enter your admin PIN: "))
            cursor.execute("select passwd from admin where id_='{}'".format(id_))
            display=cursor.fetchall()
            if(password==str(display[0][0])):
                print("\n\n\t\t\tYou have succesfully entered ADMIN\n\n")
                customer.main_menu(user,passwd)
            else:
                print("Incorrect password !!!")
        except IndexError:
            i+=1
            if i==5:
                print("\n\n\t\t\t................YOU HAVE NO ATTEMPTS LEFT FOR LOGIN.........................../n/n")
                sys.exit()
            print("\n\n\n\t\t\t............Please enter a valid username and password...............\n\n\n\t\t\t")
else:
    print("Error connecting to MySQL database")
    sys.exit()


                


