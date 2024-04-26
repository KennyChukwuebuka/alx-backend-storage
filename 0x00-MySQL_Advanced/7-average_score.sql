-- Drops the stored procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Changes the delimiter from the default ';' to '$$' to allow for the stored procedure definition
DELIMITER $$

-- Creates a stored procedure named ComputeAverageScoreForUser that takes one parameter: user_id
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    -- Declares a variable to store the total score, initialized to 0
    DECLARE total_score INT DEFAULT 0;
    
    -- Declares a variable to store the count of projects, initialized to 0
    DECLARE projects_count INT DEFAULT 0;

    -- Selects the sum of scores for the given user_id and stores it in the total_score variable
    SELECT SUM(score)
        INTO total_score
        FROM corrections
        WHERE corrections.user_id = user_id;
    
    -- Selects the count of projects for the given user_id and stores it in the projects_count variable
    SELECT COUNT(*)
        INTO projects_count
        FROM corrections
        WHERE corrections.user_id = user_id;

    -- Updates the average_score field in the users table for the given user_id
    -- If the projects_count is 0, sets average_score to 0, otherwise sets it to the total_score divided by projects_count
    UPDATE users
        SET users.average_score = IF(projects_count = 0, 0, total_score / projects_count)
        WHERE users.id = user_id;
END $$

-- Changes the delimiter back to the default ';'
DELIMITER ;