-- A script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title
  FROM tv_shows AS ts,
       tv_show_genres AS tsg,
       tv_genres AS tg
 WHERE tg.name = 'Comedy'
   AND tsg.genre_id = tg.id
   AND ts.id = tsg.show_id
 ORDER BY title ASC;
