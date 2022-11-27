import pytest

from service.genre import GenreService


class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None
        assert len(genres) > 0

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None
        assert genre.name == "Genre1"

    def test_create(self):
        genre_data = {
            "name": "Genre4"
        }

        genre = self.genre_service.create(genre_data)
        genre_ = self.genre_service.get_one(genre.id)
        assert genre.id is not None
        assert genre_ is not None

    def test_update(self):
        genre_data = {
            "id": 3,
            "name": "Genre1_change"
        }
        assert self.genre_service.update(genre_data)

    def test_delete(self):
        assert self.genre_service.delete(1) is None
