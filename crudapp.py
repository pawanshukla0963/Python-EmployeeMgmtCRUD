
import pymysql as p

'''importing pymysql to establish a connection between our SQL database and this python programme.
 Whatever changes we perform from queries in this file those are reflected in our sql database "Office".'''

def getconnect():
    return p.connect (host="localhost", user="root", password = "", database="Office") # making connection to SQL database

    
def insertrec(data): # to insert a record in table employee in columns id, firstname, lastname, email and address
    db = getconnect() # get connection of database and save it in variable db
    cr = db.cursor() 
    '''call cursor function to perform sql queries on table and gt result back. A cursor in SQL Server is a database object that reads one row at a time '''
    sql = "insert into employee values (%s, %s, %s, %s, %s)" # chronologically inserts elements from data list in place of %s 

    cr.execute(sql,data) # executes sql query with data parameter
    db.commit() #commits the inserted data in SQL database , confirms the action
    db.close()
    print("Data Inserted Successsfully...!")

def updaterec(data): # to update any record 
    db = getconnect()
    cr = db.cursor()
    sql = "update employee set FirstName=%s, LastName=%s, Email=%s, Address=%s where id=%s"
    cr.execute(sql,data)
    db.commit()
    db.close()
    print("Data updated successfully...!")

def deleterec(ids): #to delete a record
    db = getconnect()
    cr = db.cursor()
    sql = "delete from employee where id=%s" # id in parameter is inserted in %s and record of that id is deleted
    cr.execute(sql,ids)
    db.commit()
    db.close()
    print("Data deleted successfully..!")

def readdata(): # to display all records present in table
    db = getconnect()
    cr = db.cursor()
    sql = "select * from employee"
    cr.execute(sql)
    data = cr.fetchall()
    a,b,c,d,e = "id","FirstName","LastName","Email","Address"  # Here we can observe Python's multiple variable assignment feature
    print(f"\n\n{a:^5} {b:^15} {c:^15} {d:^20} {e:^30} ") 
    '''prints Column names for the data in table. provides designated space for each column and thus makes printed data look organised.'''
    for i,fn,ln,e,a in data:
        print(f"{i:^5} {fn:^15} {ln:^15} {e:^20} {a:^30}\n")
    db.commit()
    db.close()


while True: # Creating Menu for this app
    print("\n"," CRUD Database App ".center(40,"-"))
    print("\nUser Wants to - \n 1. Insert Records in Table \n 2. Update a record \n 3. Delete a record  \n 4. Display all records from table")
    n = input("Enter Your Selection: ")

    if(n=="1"):
        ids = int(input("\nEnter the ID: "))
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        if fname.isalpha()==True and lname.isalpha()==True: # to make sure user puts only alphabets in name
            pass
        else:
            print("Names only contain alphabets")
            continue
        email = input("Enter Email: ")
        add = input("Enter address: ")

        data = [ids,fname,lname,email,add]
        insertrec(data)
        continue

    if(n=="2"):
        ids = int(input("\nEnter ID of the record to be edited: "))
        fname = input("Enter updated First Name: ")
        lname = input("Enter updated Last Name: ")
        if fname.isalpha()==True and lname.isalpha()==True:
            pass
        else:
            print("Names only contain alphabets")
            continue
        email = input("Enter updated Email: ")
        add = input("Enter updated address: ")

        data = [fname,lname,email,add,ids]
        updaterec(data)
        continue

    if(n=="3"):
        ids = int(input("\nEnter ID of the record you want to Delete: "))
        deleterec(ids)
        continue

    if(n=="4"):
        readdata()
        continue

    else: # Any input other than 1,2,3,4 exits the app
        break
