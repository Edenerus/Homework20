from flask import request
from flask_restx import Resource, Namespace

from container import genre_service
from dao.model.genre import GenreSchema


genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        try:
            all_genres = genre_service.get_all()

            return genres_schema.dump(all_genres), 200

        except Exception as e:
            return str(e), 404

    def post(self):
        try:
            req_json = request.json
            genre_service.create(req_json)

        except Exception as e:
            return str(e), 404

        return "", 201


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = genre_service.get_one(gid)

            if not genre:
                return "Такого фильма нет в базе данных", 404

            return genre_schema.dump(genre), 200

        except Exception as e:
            return str(e), 404

    def put(self, gid):
        try:
            genre = genre_service.get_one(gid)

            if not genre:
                return "Такого фильма нет в базе данных", 404

            req_json = request.json
            req_json["id"] = gid

            genre_service.update(req_json)

            return "", 204

        except Exception as e:
            return str(e), 404

    def patch(self, gid):
        try:
            genre = genre_service.get_one(gid)

            if not genre:
                return "Такого фильма нет в базе данных", 404

            req_json = request.json
            req_json["id"] = gid

            genre_service.patch(req_json)

            return "", 204

        except Exception as e:
            return str(e), 404

    def delete(self, gid):
        try:
            genre = genre_service.get_one(gid)

            if not genre:
                return "Такого фильма нет в базе данных", 404

            genre_service.delete(gid)

            return "", 204

        except Exception as e:
            return str(e), 404
