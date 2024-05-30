def directors(movies):
    return {movie.director for movie in movies}


def common_elements(xs, ys):
    return {i for i in xs if i in ys}
