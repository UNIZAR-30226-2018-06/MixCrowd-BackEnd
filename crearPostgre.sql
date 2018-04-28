DROP TABLE usuario CASCADE;
DROP TABLE proyecto CASCADE;
DROP TABLE etiqueta CASCADE;
DROP TABLE colabora CASCADE;
DROP TABLE amistad CASCADE;
DROP TABLE comentario CASCADE;
DROP TABLE lista CASCADE;
DROP TABLE pertenece CASCADE;
DROP TABLE pista CASCADE;
DROP TABLE valoracion CASCADE;
DROP TABLE visita CASCADE;


CREATE TABLE usuario (
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> '')
);

CREATE TABLE proyecto (
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> ''),
	fechaCreacion	date		DEFAULT CURRENT_TIMESTAMP,
	fechaUltimaMod	date		DEFAULT CURRENT_TIMESTAMP,
	numVisitas		integer		NOT NULL DEFAULT 0,
	imagen			text,
	privacidad		boolean		NOT NULL,
	valoracion		integer		DEFAULT 0,
	administrador	char(40),
	FOREIGN KEY (administrador) REFERENCES usuario(nombre)
);

CREATE TABLE etiqueta (
	categoria		char(100)	NOT NULL	CHECK (categoria <> ''),
	proyecto_nombre	char(40),
	PRIMARY KEY(categoria,proyecto_nombre),
	FOREIGN KEY (proyecto_nombre) REFERENCES proyecto (nombre)
);

CREATE TABLE colabora (
	proyecto_nombre	char(40),
	usuario 		char(40),
	PRIMARY KEY(proyecto_nombre,usuario),
	FOREIGN KEY (proyecto_nombre) REFERENCES proyecto (nombre),
	FOREIGN KEY (usuario) REFERENCES usuario(nombre)
);

CREATE TABLE amistad (
	usuario_1		char(40),
	usuario_2		char(40)	CHECK (usuario_1 <> usuario_2),
	PRIMARY KEY(usuario_1,usuario_2),
	FOREIGN KEY (usuario_1) REFERENCES usuario(nombre),
	FOREIGN KEY (usuario_2) REFERENCES usuario(nombre)
);

CREATE TABLE comentario (
	fecha 			date		DEFAULT CURRENT_TIMESTAMP,
	texto			char(300)	NOT NULL	CHECK (texto <> ''),
	proyecto_nombre	char(40),
	comentador		char(40),
	receptor		char(40),
	PRIMARY KEY(fecha,comentador),
	FOREIGN KEY (proyecto_nombre) REFERENCES proyecto (nombre),
	FOREIGN KEY (comentador) REFERENCES usuario(nombre),
	FOREIGN KEY (receptor) REFERENCES usuario(nombre)
);

CREATE TABLE lista (
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> ''),
	fechaCreacion	date		DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pertenece (
	proyecto_nombre	char(40),
	lista_nombre	char(40),
	PRIMARY KEY(proyecto_nombre,lista_nombre),
	FOREIGN KEY (proyecto_nombre) REFERENCES proyecto (nombre),
	FOREIGN KEY (lista_nombre) REFERENCES lista (nombre)
);

CREATE TABLE pista (
	nombre			char(40)	CHECK (nombre <> ''),
	proyecto_nombre	char(40),
	audio			bytea,
	fecha 			date		DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(nombre,proyecto_nombre),
	FOREIGN KEY (proyecto_nombre) REFERENCES proyecto (nombre)
);

CREATE TABLE valoracion (
	proyecto_nombre	char(40),
	usuario_nombre	char(40),
	valor 			integer 	NOT NULL,
	PRIMARY KEY(usuario_nombre,proyecto_nombre),
	FOREIGN KEY (proyecto_nombre) REFERENCES proyecto (nombre),
	FOREIGN KEY (usuario_nombre) REFERENCES usuario(nombre)
);	

CREATE TABLE visita (
	proyecto_nombre	char(40),
	usuario_nombre	char(40),
	fecha 			date		DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(usuario_nombre,proyecto_nombre,fecha),
	FOREIGN KEY (proyecto_nombre) REFERENCES proyecto (nombre),
	FOREIGN KEY (usuario_nombre) REFERENCES usuario(nombre)
);
