import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241", "administrativo", "pendente", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241", "administrativo", "pendente", "teste.jpg")
            )

cur.execute("INSERT INTO contas (email, senha) VALUES (?, ?)",
            ('renan@renan.com', '1234')
            )

connection.commit()
connection.close()