CREATE OR REPLACE FUNCTION nV() RETURNS TRIGGER AS $nV$
    BEGIN
        UPDATE proyecto  SET numVisitas = numVisitas + 1 WHERE nombre = NEW.proyecto_nombre;
       RETURN NULL;
    END;
$nV$ LANGUAGE plpgsql;

CREATE TRIGGER numVisitas
AFTER INSERT ON visita
    FOR EACH ROW EXECUTE PROCEDURE nV();