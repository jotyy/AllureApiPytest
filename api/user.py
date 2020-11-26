from core.rest_client import RestClient

BASE_URL = "https://jotyy.top/crud"

class User(RestClient):

    def __init__(self, api_base_url, **kwargs):
        super(User, self).__init__(api_base_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/login", **kwargs)

    def register(self, **kwargs):
        return self.post("/register", **kwargs)


user = User(BASE_URL)
