CREATE OR REPLACE FUNCTION V() RETURNS TRIGGER AS $V$
    BEGIN
    IF (NEW.valor = TRUE) THEN
        UPDATE proyecto  SET valoracion = valoracion + 1 WHERE nombre = NEW.proyecto_nombre;
    ELSE
    	UPDATE proyecto  SET valoracion = valoracion - 1 WHERE nombre = NEW.proyecto_nombre;
    END IF;
       RETURN NULL;
    END;
$V$ LANGUAGE plpgsql;

CREATE TRIGGER valoracion
AFTER INSERT ON valoracion
    FOR EACH ROW 
    EXECUTE PROCEDURE V();