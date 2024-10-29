-- list all shows without the genre Comedy
SELECT tv_shows.title
  FROM tv_shows 
    LEFT JOIN (SELECT tv_shows.id AS tv_shows_id
                 FROM tv_genres,
                      tv_show_genres,
                      tv_shows
                WHERE tv_genres.id = tv_show_genres.genre_id
                  AND tv_show_genres.show_id = tv_shows.id
                  AND tv_genres.name = "Comedy") AS tb_tv_shows_id
        ON tv_shows.id = tb_tv_shows_id.tv_shows_id
 WHERE tb_tv_shows_id.tv_shows_id IS NULL
ORDER BY tv_shows.title;


