CREATE TABLE proyecto (
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> ''),
	fechaCreacion	date		NOT NULL,
	fechaUltimaMod	date		NOT NULL,
	categoria		char(100)	NOT NULL	CHECK (categoria <> ''),
	numVisitas		integer		NOT NULL,
	imagen			text 		NOT NULL,
	privacidad		boolean		NOT NULL,
	valoracion		integer		NOT NULL
);

CREATE TABLE usuario (
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> '')
);

CREATE TABLE amistad (
	usuario_1		char(40)	REFERENCES	usuario (nombre),
	usuario_2		char(40)	REFERENCES	usuario (nombre)	CHECK (usuario_1 <> usuario_2),
	PRIMARY KEY(usuario_1,usuario_2)
);

CREATE TABLE comentario (
	fecha 			date		NOT NULL,
	texto			char(300)	NOT NULL	CHECK (texto <> ''),
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	comentador		char(40)	REFERENCES	usuario (nombre),
	receptor		char(40)	REFERENCES	usuario (nombre),
	PRIMARY KEY(fecha,comentador)
);

CREATE TABLE lista (
	nombre			char(40)	PRIMARY KEY CHECK (nombre <> ''),
	fechaCreacion	date		NOT NULL
);

CREATE TABLE pertenece (
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	lista_nombre	char(40)	REFERENCES	lista (nombre),
	PRIMARY KEY(proyecto_nombre,lista_nombre)
);

CREATE TABLE pista (
	nombre			char(40)	CHECK (nombre <> ''),
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	audio			bytea		NOT NULL,
	PRIMARY KEY(nombre,proyecto_nombre)
);

CREATE TABLE valoracion (
	proyecto_nombre	char(40)	REFERENCES	proyecto (nombre),
	usuario_nombre	char(40)	REFERENCES	usuario (nombre),
	PRIMARY KEY(usuario_nombre,proyecto_nombre)
);	