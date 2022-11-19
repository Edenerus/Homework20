from dao.movie import MovieDao


class MovieService:
    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, director_id, genre_id, year):

        if director_id:
            all_movies = self.dao.get_all_movies_director(director_id)

            return all_movies

        if genre_id:
            all_movies = self.dao.get_all_movies_genre(genre_id)

            return all_movies

        if year:
            all_movies = self.dao.get_all_movies_year(year)

            return all_movies

        all_movies = self.dao.get_all()

        return all_movies

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        fields_to_update = ["title", "description", "trailer", "year", "rating", "genre_id", "director_id"]

        #for field in fields_to_update:
        setattr(movie, field, data.get(field))

        self.dao.update(movie)

    def patch(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        fields_to_update = ["title", "description", "trailer", "year", "rating", "genre_id", "director_id"]

        for field in fields_to_update:
            if data.get(field):
                setattr(movie, field, data.get(field))

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
