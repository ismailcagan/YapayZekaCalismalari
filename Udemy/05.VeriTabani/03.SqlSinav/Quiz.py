import sqlite3

class SqlQuiz:
    
    def OpenDatabase(self):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        return conn,cursor

    def answers(self,cursor):
    
        print("----------Sınav Cevapları----------")
        # Basit
        print("1. Bütün kursların bilgilerini getirin")
        cursor.execute("select * from Courses")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")
        
        print(60*"-")

        print("2. Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin")
        cursor.execute("select instructor,course_name from Courses")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")

        print(60*"-")
        
        print("3. Sadece 21 yaşındaki öğrencileri getirin")
        cursor.execute("select * from Students where age = 21")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")

        print(60*"-")
        
        print("4. Sadece Chicago'da yaşayan öğrencileri getirin")
        cursor.execute("select * from Students where city = 'Chicago'")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")

        print(60*"-")

        print("5. Sadece 'Dr. Anderson' tarafından verilen dersleri getirin")
        cursor.execute("select course_name from Courses where instructor='Dr Anderson'")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")
        
        print(60*"-")

        print("6. Sadece ismi 'A' ile başlayan öğrencileri getirin")
        cursor.execute("select * from Students where name like 'A%'")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")

        print(60*"-")

        print("7. Sadece 3 ve üzeri kredi olan dersleri getirin")
        cursor.execute("select * from Courses where credits >=3")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")

        print(60*"-")

        # Detaylı

        print("1. Öğrencileri alphabetic şekilde dizerek getirin")
        cursor.execute("select * from Students order by name")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")

        print(60*"-")

        print("2. 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin")
        cursor.execute("select * from Students where age >20 order by name")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")

        print(60*"-")

        print("3. Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin")
        cursor.execute("select * from Students where city = 'New York' or city ='Chicago'")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")

        print(60*"-")

        print("4. Sadece 'New York' ta yaşamayan öğrencileri getirin")
        cursor.execute("select * from Students where city != 'New York' ")
        records = cursor.fetchall()
        for item in records:
            print(f"{item}")
            
    def main(self):
        conn,cursor = self.OpenDatabase()
        try:
            self.answers(cursor)
        except sqlite3.Error as ex:
            print(f"{ex}")
        finally:
            conn.close()
            

if __name__ == "__main__":
    quiz = SqlQuiz()
    quiz.main()
