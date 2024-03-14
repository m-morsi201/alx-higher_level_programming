-- Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT `name`, SUM(`rate`) AS `rating` FROM `tv_genres` AS m
	INNER JOIN `tv_show_genres` AS r ON r.`genre_id` = m.`id`
	INNER JOIN `tv_show_ratings` AS b ON b.`show_id` = r.`show_id`
 	GROUP BY `name` ORDER BY `rating` DESC;
