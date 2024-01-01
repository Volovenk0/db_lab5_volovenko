DO $$ 
DECLARE
    i INT := 1;
BEGIN
    LOOP
        EXIT WHEN i > 10;  
        INSERT INTO author (author_id, author_name) VALUES (i, 'Author ' || i);
        i := i + 1;
    END LOOP;
END $$;

