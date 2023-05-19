-- A script that uses the hbtn_0d_tvshows database to list all genres not linked
-- to the show Dexter
SELECT tv_genres.name
  FROM tv_genres
 WHERE name NOT IN
       (SELECT tv_genres.name
          FROM tv_genres, tv_show_genres, tv_shows
         WHERE title = 'Dexter'
       	   AND tv_shows.id = tv_show_genres.show_id
	   AND tv_genres.id = tv_show_genres.genre_id)
ORDER BY tv_genres.name ASC;
