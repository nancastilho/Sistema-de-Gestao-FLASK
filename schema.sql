DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS contas;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    conclusao TEXT NOT NULL,
    departamentos TEXT NOT NULL,
    status TEXT NOT NULL,
    anexos TEXT NOT NULL
);

CREATE TABLE user (
	id INTEGER NOT NULL, 
	nome VARCHAR(20) NOT NULL, 
	username VARCHAR(20) NOT NULL, 
    departamento VARCHAR(80) NOT NULL, 
	password VARCHAR(80) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);

CREATE TABLE setores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    setor TEXT NOT NULL,
    vf TEXT NOT NULL
);

