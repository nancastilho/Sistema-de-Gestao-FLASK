import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "administrativo", "pendente", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "suporte", "pendente", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "desenvolvimento", "pendente", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "suporte", "concluido", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "suporte", "desenvolvendo", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "administrativo", "concluido", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "desenvolvimento", "desenvolvendo", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "administrativo", "pendente", "teste.jpg")
            )

cur.execute("INSERT INTO posts (title, content, conclusao, departamentos, status, anexos) VALUES (?, ?, ?, ?, ?, ?)",
            ('teste', 'teste', "21/25/4241",
             "suporte", "concluido", "teste.jpg")
            )

cur.execute("INSERT INTO contas (nome, email, senha, departamento) VALUES (?, ?, ?, ?)",
            ('Renan', 'renan@renan.com', '1234', 'suporte')
            )

cur.execute("INSERT INTO contas (nome, email, senha, departamento) VALUES (?, ?, ?, ?)",
            ('Patrick', 'patrick@patrick.com', '4321', 'suporte')
            )

cur.execute("INSERT INTO contas (nome, email, senha, departamento) VALUES (?, ?, ?, ?)",
            ('Patrick', 'patrick@patrick.com.br', '4321', 'suporte')
            )

cur.execute("INSERT INTO setores (setor, vf) VALUES (?,?)",
            ('suporte', 'v')
            )


connection.commit()
connection.close()
