"""
you must create table as this to save BLOB data in
CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);

What is BLOB
A BLOB (large binary object) is an SQLite data type that can be used to store large
objects typically large files such as images, music, videos, documents, pdf, etc. We need to convert
our files and images into binary data i.e., byte array in Python to store and retrieve from SQLite database
The SQLite table is empty as of now let’s insert a few employee’s photo and resume file in it.
"""

import sqlite3


def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(empId, name, photo, resumeFile):
    try:
        db_connect = sqlite3.connect('PATH TO BASE')
        cursor = db_connect.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO SOME_TABLE_IN_BASE
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        db_connect.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("the sqlite connection is closed")

# examples start 
insertBLOB(1, "Smith", "E:\pynative\Python\photos\smith.jpg", "E:\pynative\Python\photos\smith_resume.txt")
insertBLOB(2, "David", "E:\pynative\Python\photos\david.jpg", "E:\pynative\Python\photos\david_resume.txt")