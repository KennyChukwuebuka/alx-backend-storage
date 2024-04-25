-- Create a trigger that decreases the quantity of an item after adding a new order
DELIMITER //

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_qty INT;
    
    -- Get the current quantity of the item
    SELECT quantity INTO item_qty
    FROM items
    WHERE name = NEW.item_name;
    
    -- Update the quantity of the item in the items table
    UPDATE items
    SET quantity = GREATEST(item_qty - NEW.number, 0)
    WHERE name = NEW.item_name;
END;
//

DELIMITER ;
