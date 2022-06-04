#table creation

import sqlite3 as sql

conn=sql.connect('test.db') 
cur = conn.cursor()

#cur.execute('create table user_table(username varchar(25), passwd varchar(25)  )')

print('=========WELCOME TO START    EMPLOYEE MANAGEMENT SYSTEM=========')

import datetime as dt 
print (dt.datetime.now())

print('1. REGISTER')

print()

print('2. LOGIN')

print()

n=int(input('enter your choice='))

print()

if n== 1:
    name=input('Enter a Username= ')
    print()
    passwd=int(input('Enter a 4 DIGIT Password='))
    print()
    V_SQLInsert="INSERT   INTO user_table(passwrd,username) values (' str (passwd)' ,'name') " 
    cur.execute(V_SQLInsert) 
    conn.commit() 
    print() 
    print('USER created succesfully') 
    import mainp

if n==2:
    name=input('Enter your Username=') 
    print() 
    passwd=int(input('Enter your 4 DIGITPassword='))
    V_Sql_Sel="select * from user_table where  passwrd='"+str (passwd)+" and username= "+name+"'"
    cur.execute(V_Sql_Sel)
    conn.commit()
    if cur.fetchall() is None: 
        print('Invalid username or password')
    else:
     print() 
     import mainp

conn.close()
