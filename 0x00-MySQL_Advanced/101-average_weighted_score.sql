-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    SELECT user_id, SUM(score * projects.weight) / SUM(projects.weight) AS average
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    GROUP BY user_id;
END$$
DELIMITER $$