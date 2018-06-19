#Ques1 Create a database. Create the following tables:
#1. Book 2. Titles 3. Publishers 4. Zipcodes 5. AuthorsTitles 6. Authors
import Mysqldb
db=MySQLdb.connect("localhost","testuser","test123","TESTDB")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
db.close()

db=MySQLdb.connect("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE BOOKS(book_id INT,Title_id INT primary key,location varchar(20),genre varchar(10)"""
sql="""CREATE TABLE Titles(select title id from Books as title_id,publisher_id INT primary key,publication year varchar(20),ISBN varchar(10)"""
sql="""CREATE TABLE Publishers(select * from Titles as publisher_id,Zipcode_id INT primary key,name varchar(20),address varchar(10)"""
sql="""CREATE TABLE Zip code(select * from zip code as zip_code,city varchar(20),state varchar(10)"""
sql="""CREATE TABLE Authors Titles(Author_id INT,Author_titleId INT primary key"""
sql="""CREATE TABLE Authors(Author_id INT,first_name varchar(20),middle_name varchar(20),last_name varchar(10)"""

cursor.execute(sql)
db.close()
#QUES@
db=MySQLdb=MySQLdb.connect("localhost","testuser","test123","TESTDB")
cursor=db.cursor()
sql="""INSERT INTO BOOKS(book_id,Title_id,location,genre)
     VALUES(1,3,'abcd','dff')"""
try:
    cursor.execute(sql)
    db.commit
except:
    db.rollback()
db.close()

#QUES3 Update any values in any of the tables. Print the original and updated values.
 import pymysql as pm

 try:
     con = pm.connect(host='localhost', database='yello', \
                     user='helpme')
    cursor = con.cursor()
    sql = "update BOOKS set location='ecbdnm' where bookid = 1"
    cursor.execute(sql)
    con.commit()
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')



