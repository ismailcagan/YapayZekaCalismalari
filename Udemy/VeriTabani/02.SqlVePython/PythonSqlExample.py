import sqlite3
import os

# VERİ TABANI OLUŞTURULDU
def CreateDatabase():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db") # bağlantı açıyor
    cursor = conn.cursor() # databse içerisinde gezinip ekleme,silme,okuma vb.yapar
    return conn,cursor

# TABLO OLUŞTURMA
def CreateTables(cursor):
    cursor.execute('''
        create table Students(
            id integer primary key,
            name varchar not null,
            age int,
            email varchar unique,
            city varchar
        ) 
        ''')
    cursor.execute('''
            create table Courses(
                id integer primary key,
                course_name varchar not null,
                instructor text,
                credits integer
            ) 
            ''')

# TABLOLARA VERİ EKLEME
def InsertSampleData(cursor):
    students = [
        (1,"Alice Johnson",20,"alice@gmail.com","New York"),
        (2,"Bob Simith",19,"bob@gmail.com","Chicago"),
        (3,"Carol  White",21,"carol@gmail.com","Boston"),
        (4,"David Brown",20,"david@gmail.com","New York"),
        (5,"Emma Davis",22,"emma@gmail.com","Seattle")
    ]
    cursor.executemany("insert into Students values (?,?,?,?,?)",students)

    courses = [
        (1,"Pyhon Programing","Dr Anderson",3),
        (2,"Web Development","Prof Wilson",4),
        (3,"Data Science","Dr. Taylor",3),
        (4,"Mobile Apps","Prof. Garcia",2)
    ]
    cursor.executemany("insert into Courses values (?,?,?,?)",courses)

# TABLO SORGULARI
def BasicSqlOperatıons(cursor):
    #1)SelectALl
    print("--------------Select All-------------")
    cursor.execute("select * from Students")
    records = cursor.fetchall()
    for i in records:
        print(i)
        
    #2)SelectColumns
    print("-----------------Select Columns-----------")
    cursor.execute("select name,age from Students")
    records = cursor.fetchall()
    for i in records:
        print(i)
    
    #3) Where Clause
    print("-----------------Where age = 20 -----------")
    cursor.execute("select * from Students where age = 20")
    records = cursor.fetchall()
    for i in records:
        print(i)
    
    #4) Where Clause
    print("-----------------Where City = New York -----------")
    cursor.execute("select * from Students where city = 'New York'")
    records = cursor.fetchall()
    for i in records:
        print(i)
        
    #5) Order By
    print("-----------------Order By age -----------")
    cursor.execute("select * from Students order by age")
    records = cursor.fetchall()
    for i in records:
        print(i)

    #5) Limit
    print("-----------------Limit = 3 -----------")
    cursor.execute("select * from Students Limit 3")
    records = cursor.fetchall()
    for i in records:
        print(i)

# TABLO EKLEME-GÜNCELLEME-SİLME
def SqlUpdateDeleteInsertOperatıons(conn,cursor):
    #1) Insert
    cursor.execute("insert into Students values(6,'Frank Miller',23,'frank@gmail.com','Miami')")
    conn.commit()
    
    #2) Update
    cursor.execute("update Students set age = 24 where id = 6")

    #3) Delete
    cursor.execute("delete from Students where id = 6")

def AggregateFunctions(cursor):
    #1) Count
    print("--------------Aggregate Functions Counts--------------------")
    cursor.execute("select count(*) from Students ")
    result = cursor.fetchone()
    print(f"Kayit SAyisi :{result[0]}")
    
    #2) Average
    print("--------------Aggregate Functions Average--------------------")
    cursor.execute("select AVG(age) from Students ")
    result = cursor.fetchone()
    print(f"Yaş Ortalaması :{result[0]}")

    #2) Max-Min
    print("--------------Aggregate Functions Max-Min--------------------")
    cursor.execute("select Max(age),Min(age) from Students ")
    result = cursor.fetchall()
    print(f"Max Yaş :{result[0][0]} - Min Yaş :{result[0][1]}")

    #2) Group By
    print("--------------Aggregate Functions Group By--------------------")
    cursor.execute("select city, Count(*) from Students Group By city ")
    result = cursor.fetchall()
    print(f"{result}")


def main():
    conn,cursor = CreateDatabase()
    try:
        CreateTables(cursor)
        InsertSampleData(cursor)
        BasicSqlOperatıons(cursor)
        SqlUpdateDeleteInsertOperatıons(conn,cursor)
        AggregateFunctions(cursor)
        conn.commit() # cursor'un yaptığı işleri uygula
    
    except sqlite3.Error as ex:
        print(ex)
    
    finally:
        conn.close()


if __name__ == "__main__":
    main()
    