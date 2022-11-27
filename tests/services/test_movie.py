import pytest

from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Movie1"

    def test_create(self):
        movie_data = {
            "name": "Movie4"
        }

        movie = self.movie_service.create(movie_data)
        movie_ = self.movie_service.get_one(movie.id)
        assert movie.id is not None
        assert movie_ is not None

    def test_update(self):
        movie_data = {
            "id": 3,
            "title": "Movie3_change",
            "description": "desc_change",
            "trailer": "link_change",
            "year": 2000,
            "rating": 10.0,
            "director_id": 1,
            "genre_id": 2
        }
        assert self.movie_service.update(movie_data)

    def test_delete(self):
        assert self.movie_service.delete(1) is None
