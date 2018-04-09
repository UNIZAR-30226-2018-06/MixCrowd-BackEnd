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
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> ''),
	fechaRegistro	date 		DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE proyecto (
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> ''),
	fechaCreacion	date		DEFAULT CURRENT_TIMESTAMP,
	fechaUltimaMod	date		DEFAULT CURRENT_TIMESTAMP,
	numVisitas		integer		DEFAULT 0,
	imagen			text,
	privacidad		boolean		NOT NULL,
	valoracion		integer		DEFAULT 0,
	administrador	char(40)	REFERENCES	usuario(nombre)
);

CREATE TABLE etiqueta (
	categoria		char(100)	NOT NULL	CHECK (categoria <> ''),
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	PRIMARY KEY(categoria,proyecto_nombre)
);

CREATE TABLE colabora (
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	usuario 		char(40)	REFERENCES	usuario (nombre),
	PRIMARY KEY(proyecto_nombre,usuario)
);

CREATE TABLE amistad (
	usuario_1		char(40)	REFERENCES	usuario (nombre),
	usuario_2		char(40)	REFERENCES	usuario (nombre)	CHECK (usuario_1 <> usuario_2),
	PRIMARY KEY(usuario_1,usuario_2)
);

CREATE TABLE comentario (
	fecha 			date		DEFAULT CURRENT_TIMESTAMP,
	texto			char(300)	NOT NULL	CHECK (texto <> ''),
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	comentador		char(40)	REFERENCES	usuario (nombre),
	receptor		char(40)	REFERENCES	usuario (nombre),
	PRIMARY KEY(fecha,comentador)
);

CREATE TABLE lista (
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> ''),
	fechaCreacion	date		DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pertenece (
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	lista_nombre	char(40)	REFERENCES	lista (nombre),
	PRIMARY KEY(proyecto_nombre,lista_nombre)
);

CREATE TABLE pista (
	nombre			char(40)	CHECK (nombre <> ''),
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	audio			bytea,
	fecha 			date		DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(nombre,proyecto_nombre)
);

CREATE TABLE valoracion (
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	usuario_nombre	char(40)	REFERENCES	usuario (nombre),
	valor 			integer 	NOT NULL,
	PRIMARY KEY(usuario_nombre,proyecto_nombre)
);	

CREATE TABLE visita (
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	usuario_nombre	char(40)	REFERENCES	usuario (nombre),
	fecha 			date		DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(usuario_nombre,proyecto_nombre,fecha)
);
