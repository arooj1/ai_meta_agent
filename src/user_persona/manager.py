class UserPersonaManager:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id):
        return self.db.get(user_id)