-- A script that lists all shows without the genre Comedy in the database
-- hbtn_0d_tvshows
SELECT DISTINCT title
  FROM tv_shows
  LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
  LEFT JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
 WHERE title NOT IN
       (SELECT title
          FROM tv_shows
 	  LEFT JOIN tv_show_genres
	    ON tv_shows.id = tv_show_genres.show_id
	  LEFT JOIN tv_genres
	    ON tv_genres.id = tv_show_genres.genre_id
	 WHERE tv_genres.name = 'Comedy')
 ORDER BY title ASC;
