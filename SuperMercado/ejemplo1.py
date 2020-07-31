import sqlite
conn =  sqlite.connect("newDataBase.db")
c= conn.cursos()
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',88,35.14)")
conn.commit()
