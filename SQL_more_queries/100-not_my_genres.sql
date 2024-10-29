--  list all genres not linked to the show Dexter
SELECT tv_genres.name
  FROM tv_genres
      LEFT JOIN 
      (SELECT tv_genres.id AS genres_id
  FROM tv_genres,
       tv_show_genres,
       tv_shows
 WHERE tv_genres.id = tv_show_genres.genre_id
   AND tv_show_genres.show_id = tv_shows.id
   AND tv_shows.title = "Dexter") AS tb_genres_id ON tv_genres.id = tb_genres_id.genres_id
 WHERE tb_genres_id.genres_id IS NULL
ORDER BY tv_genres.name;