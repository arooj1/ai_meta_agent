class MemoryStore:
    def __init__(self, user_profile):
        self.store = {}
        self.user = user_profile

    def update(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key)

    def dump(self):
        return {
            "user": self.user,
            "data": self.store
        }