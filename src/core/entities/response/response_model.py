class UserResponseObject:
    def __init__(self, email=None, username=None, id=None):
        self.email = email
        self.username = username
        self.id = id


class TokensResponseObject:
    def __init__(self, access=None, refresh=None):
        self.access = access
        self.refresh = refresh


class DataResponseObject:
    def __init__(self, user=None, tokens=None):
        self.user = user
        self.tokens = tokens


class ResponseObject:
    def __init__(self, status=None, data=None, message=None):
        self.status = status
        self.message = message
        self.data = data
