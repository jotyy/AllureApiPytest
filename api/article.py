from api.api_config import BASE_URL
from core.rest_client import RestClient


class Article(RestClient):

    def __init__(self, api_base_url, **kwargs):
        super(Article, self).__init__(api_base_url, **kwargs)

    def getAllArticles(self, **kwargs):
        return self.get("/api/v1/articles", **kwargs)


article = Article(BASE_URL)
