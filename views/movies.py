from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema


movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        try:

            director_id = request.args.get('director_id')
            genre_id = request.args.get('genre_id')
            year = request.args.get('year')

            movies = movie_service.get_all(director_id, genre_id, year)

            return movies_schema.dump(movies), 200

        except Exception as e:
            return str(e), 404

    def post(self):
        try:
            req_json = request.json
            movie_service.create(req_json)

        except Exception as e:
            return str(e), 404

        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)

            if not movie:
                return "Такого фильма нет в базе данных", 404

            return movie_schema.dump(movie), 200

        except Exception as e:
            return str(e), 404

    def put(self, mid):
        try:
            movie = movie_service.get_one(mid)

            if not movie:
                return "Такого фильма нет в базе данных", 404

            req_json = request.json
            req_json["id"] = mid

            movie_service.update(req_json)

            return "", 204

        except Exception as e:
            return str(e), 404

    def patch(self, mid):
        try:
            movie = movie_service.get_one(mid)

            if not movie:
                return "Такого фильма нет в базе данных", 404

            req_json = request.json
            req_json["id"] = mid

            movie_service.patch(req_json)

            return "", 204

        except Exception as e:
            return str(e), 404

    def delete(self, mid):
        try:
            movie = movie_service.get_one(mid)

            if not movie:
                return "Такого фильма нет в базе данных", 404

            movie_service.delete(mid)

            return "", 204

        except Exception as e:
            return str(e), 404
