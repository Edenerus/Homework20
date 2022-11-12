from dao.model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        entity = self.session.query(Director).get(mid)

        return entity

    def get_all(self):
        entity_list = self.session.query(Director).all()

        return entity_list

    def create(self, data):
        director = Director(**data)

        self.session.add(director)
        self.session.commit()

        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()

        return director

    def delete(self, mid):
        director = self.get_one(mid)

        self.session.delete(director)
        self.session.commit()
