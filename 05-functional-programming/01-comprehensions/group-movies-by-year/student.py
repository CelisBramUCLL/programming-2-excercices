def group_movies_by_year(movies):
    return {
        movie.year: [movie2.title for movie2 in movies if movie.year == movie2.year]
        for movie in movies
    }
