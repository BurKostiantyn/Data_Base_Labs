CREATE OR REPLACE FUNCTION check_doc_rules() RETURNS TRIGGER AS $$
DECLARE
    cat_rec RECORD;
    cur_category CURSOR FOR 
        SELECT * FROM categories WHERE category_id = NEW.category_id;
BEGIN
    -- === ЛОГІКА ДЛЯ INSERT ===
    IF (TG_OP = 'INSERT') THEN
        NEW.title := TRIM(NEW.title);

        IF length(NEW.title) < 3 THEN
            RAISE EXCEPTION 'Помилка: Назва документа занадто коротка (мінімум 3 символи)!';
        END IF;

        OPEN cur_category;
        LOOP
            FETCH cur_category INTO cat_rec;
            EXIT WHEN NOT FOUND;

            IF cat_rec.description LIKE '%Locked%' THEN
                RAISE EXCEPTION 'Помилка: Ця категорія заблокована для нових документів!';
            END IF;
        END LOOP;
        CLOSE cur_category;

        RETURN NEW;

    -- === ЛОГІКА ДЛЯ DELETE ===
    ELSIF (TG_OP = 'DELETE') THEN
        IF OLD.created_at >= CURRENT_DATE THEN
            RAISE EXCEPTION 'Помилка: Заборонено видаляти документи, створені сьогодні!';
        END IF;
        
        RETURN OLD;
    END IF;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;