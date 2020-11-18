import sqlite3

def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

try:
    #existing DB
    sqliteCon = sqlite3.connect('C:\sqlite\database\Egor_test.db')
    #copy into this DB
    backupCon = sqlite3.connect('C:\sqlite\database\Egor_test(b).db')
    with backupCon:
        sqliteCon.backup(backupCon, pages=2, progress=progress)
    print("backup successful")
except sqlite3.Error as error:
    print("Error while taking backup: ", error)
finally:
    if(backupCon):
        backupCon.close()
        sqliteCon.close()
