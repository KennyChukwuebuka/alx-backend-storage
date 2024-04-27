DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_score FLOAT;

    -- Calculate total weighted score for the user
    SELECT SUM(corrections.score * projects.weight) INTO total_score
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate total weight for the user's projects
    SELECT SUM(weight) INTO total_weight
    FROM projects;

    -- Calculate average weighted score
    SET avg_score = total_score / total_weight;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;

END //

DELIMITER ;
