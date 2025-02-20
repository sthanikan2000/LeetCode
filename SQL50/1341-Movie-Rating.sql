(
    select name results
    from MovieRating
    inner join Users using(user_id)
    group by user_id
    order by count(user_id) desc, name asc
    limit 1
)
UNION ALL ## Keep duplicates
(
    select title results
    from MovieRating
    inner join Movies using(movie_id)
    where created_at between "2020-02-01" and "2020-02-29"
    group by movie_id
    order by AVG(rating) desc, title asc
    limit 1
);

# Failing test case where movie title result and user name are same
-- (
--     select name results
--     from MovieRating
--     inner join Users using(user_id)
--     group by user_id
--     order by count(user_id) desc, name asc
--     limit 1
-- )
-- UNION
-- (
--     select title results
--     from MovieRating
--     inner join Movies using(movie_id)
--     where created_at between "2020-02-01" and "2020-02-29"
--     group by movie_id
--     order by AVG(rating) desc, title asc
--     limit 1
-- );