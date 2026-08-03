class UserEntity:
    def __init__(self, id=None, username=None, email=None, is_active=False):
        self.id = id
        self.username = username
        self.email = email
        self.is_active = is_active
