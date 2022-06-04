import time
print ("\t\t\t", time.ctime ())
import sqlite3 as sql 
conn = sql.connect ('test.db')
cur=conn.cursor()
mycursor = conn.cursor()
def menu ():
        print ("      EMPLOYEES MANAGEMENT SYSTEM      ")
        c = 'yes'
        c = input ("do you want to continue or not (yes or No):") 
        while (c == 'yes'):
        
            print("1. login") 
            print("2. employee registeration") 
            print("3. employee details") 
            print("4. update salary")
            print("5. employees list ") 
            print("6. know the number of employees ") 
            print("7. work experience ")
            print("8. know your salary ")
            print("9. exiting ") 
            choice=int(input("    Enter the choice:    "))
            if choice==1:
              login()
            
            elif choice==2: 
                register()
            
            elif choice==3:
             details()
            
            elif choice ==4:
             em_salary()
    
            elif choice==5: 
             em_list()
            
            elif choice==6:
             em_count()
            
            elif choice==7:
             em_perform()
            
            elif choice==8:
                salary()
            
            else:       
             print (" exit ")
             break
             print(" Thank You ")

def login():

        import sys
        user_id=input(" enter USER ID: ")
        pwd=int(input(" enter the password: "))
        
        if user_id == 'Admin' and pwd==1234: 
            print(" welcome to EMPLOYEE MANAGEMENT SYSTEM ") 
        else:
         print(" invalid user id and password ")
         sys.exit()

        
def register():
        
    import sqlite3 as sql
    
            
    conn=sql.connect ('test.db')
            
    mycursor=conn.cursor()
            
    eno=int(input(" enter your employee ID: ")) 
    ename=input (" enter your name: ")
    edept=input( " enter department you want to join: ") 
    esal=int(input (" enter your salary: "))
    eage=int(input(" enter your age: "))
    insert="INSERT into OFFICE ('id','name','dep','sal','age') VALUES (?,?,?,?,?)"
    tup=(eno,ename,edept,esal,eage)
    mycursor.execute(insert,tup) 
    conn.commit ()
    conn.close()
    print ("congrats you have joined suuceessfully") 
    print ("registerd suyccessfully")
            
def details():

        import sqlite3 as sql
        
        conn=sql.connect('test.db') 
        mycursor=conn.cursor ()
        mycursor.execute ("select* from OFFICE")
        
        results=mycursor.fetchall()
        
        conn.commit()
        print("Employee id \tName \tDepartment \tSalary \tAge" )
        print("----------- \t---- \t---------- \t------ \t---")
        for row in results:
         print(str(row[0])+"\t\t"+row[1]+"\t"+row[2]+"\t\t"+str(row[3])+"\t"+str(row[4])+"\t")

        conn.close() 

def em_salary():

        import sqlite3 as sql 

        conn=sql.connect('test.db') 
        mycursor=conn.cursor()
            
        nam=input(" enter your name ")
        mycursor.execute(" UPDATE office set sal=sal+(sal/10) where name = '{}'".format(nam))
        conn.commit()
        conn.close()
def em_list ():
            
        import sqlite3 as sql
        c=0
        conn=sql.connect ('test.db') 
        mycursor=conn.cursor()

        mycursor.execute("select name from office order by name asc")

        list_=mycursor.fetchall() 
        for row in list_ :
         print(row[0]+"\t%s"+row[1]+"\t%s"+row[2]+"\t%s"+row[3]+"\t%s"+row[4]+"\t%s"+row[5]+"\t%s"+row[6])
         c=c+1
        print("Total number of employees are :",c)
        conn.close()

def em_count():

        import sqlite3 as sql
        
        conn=sql.connect ('test.db')
        
        mycursor=conn.cursor() 
        mycursor.execute("select count(distinct name) from office")
        count=mycursor.fetchall()
        
        for x in count:
         print(" number of employees: ",x) 
        
        conn.commit()
        conn.close()

def salary():

        nam=input("enter your name :")
        a=mycursor.execute("select sal from office where name='{}'".format(nam))
        
        mycursor.execute(a)
        
        salary=mycursor.fetchall() 
        for x in salary:
         print(x, "is your current salary", nam)
        
        conn.commit()
        conn.close()
def em_perform():
        
        v_em_no=int(input("enter your employee ID")) 
        v_em_name=input ("enter your name:")
        v_em_dept=input( "enter department you want to join: ")
        esal=int(input (" enter your salary: "))
        v_em_performance=input("enter your performance:")
        v_em_work=input("enter your experience (YEARS):")
        eage=int(input("emter your age"))
        insert="INSERT into OFFICE ('id','name','sal','dep','per','exp','age') VALUES (?,?,?,?,?,?,?)"
        tup=(v_em_no,v_em_name,esal,v_em_dept,v_em_performance,v_em_work,eage)
        mycursor.execute(insert,tup) 
        conn.commit()
        conn.close()
        print("performance added")
conn.close()        
menu()
