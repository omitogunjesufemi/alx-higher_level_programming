-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their
-- rating.
SELECT name, SUM(rate) AS 'rating'
  FROM tv_shows, tv_show_ratings, tv_show_genres, tv_genres
 WHERE tv_shows.id = tv_show_ratings.show_id
   AND tv_shows.id = tv_show_genres.show_id
   AND tv_genres.id = tv_show_genres.genre_id
 GROUP BY name
 ORDER BY rating DESC;
