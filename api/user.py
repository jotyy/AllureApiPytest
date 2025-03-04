from api.api_config import BASE_URL
from core.rest_client import RestClient


class User(RestClient):

    def __init__(self, api_base_url, **kwargs):
        super(User, self).__init__(api_base_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/login", **kwargs)

    def register(self, **kwargs):
        return self.post("/register", **kwargs)

    def unregister(self, **kwargs):
        return self.delete("/unregister", **kwargs)


user = User(BASE_URL)
