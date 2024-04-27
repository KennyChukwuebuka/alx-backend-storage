-- Assuming the table 'names' already exists

-- Drop the index if it already exists
DROP INDEX IF EXISTS idx_name_first_score ON names;

-- Create the index on the first letter of the name column and the score column
CREATE INDEX idx_name_first_score ON names (name(1), score);
