from data import movie_db

def recommend_movies(genre):
    genre = genre.capitalize()
    return movie_db.get(genre, [])
