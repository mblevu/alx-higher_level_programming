-- Lists all shows contained in the database hbtn_od_tvshows
-- Lists all rows of tables in adatabase
SELECT tvshows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
