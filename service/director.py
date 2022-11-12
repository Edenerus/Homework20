from dao.director import DirectorDao


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        did = data.get("id")
        director = self.get_one(did)

        fields_to_update = ["title", "description", "trailer", "year", "rating", "genre_id", "director_id"]

        for field in fields_to_update:
            setattr(director, field, data.get(field))

        self.dao.update(data)

    def patch(self, data):
        did = data.get("id")
        director = self.get_one(did)

        fields_to_update = ["title", "description", "trailer", "year", "rating", "genre_id", "director_id"]

        for field in fields_to_update:
            if data.get(field):
                setattr(director, field, data.get(field))

        self.dao.update(data)

    def delete(self, did):
        self.dao.delete(did)
