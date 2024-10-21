import mysql.connector
from mysql.connector import Error

def get_records(batch_size=5):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='employee',
        )

        if connection.is_connected():
            print('Connected successfully')
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM dept_emp")

            while True:
                records = cursor.fetchmany(batch_size)  
                if not records:
                    break
                yield records  
            
        else:
            print('Not connected, sorry.')  
                     
    except Error as e:
        print(f'Error is: {e}')
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    print('----BATCH OF RECORDS-----')
    batch_number = 1  
    for batch in get_records(batch_size=5):  
        print(f"Batch number {batch_number}:") 
        for record in batch:  
            print(record)  
        batch_number += 1 
        input("Press Enter to continue...")  
        print()  
