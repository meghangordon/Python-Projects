
import sqlite3

dbsub = sqlite3.connect('dbsub.db')

with dbsub:
    cur = dbsub.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_submission( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList TEXT \
        )")
    dbsub.commit()


dbsub = sqlite3.connect('dbsub.db')
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                   'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for x in fileList:
    if x.endswith('.txt'):
        with dbsub:
            cur = dbsub.cursor()
            cur.execute("INSERT INTO tbl_submission (col_fileList) VALUES (?)", (x,))
            print(x)
            
dbsub.close()

