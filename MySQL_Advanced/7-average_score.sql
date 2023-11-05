-- 7-average_score.sql
-- average_score

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    
    -- Calculate the average score for the given user
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
    
    -- Update the average score for the user in the users table
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END;

//

DELIMITER ;
