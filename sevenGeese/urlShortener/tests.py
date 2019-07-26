from django.test import TestCase

from graphene.test import Client

from sevenGeese.schema import schema

from .models import Urls


class GraphQLTestCase(TestCase):

    def test_urls(self):

        query = """
        query{
            urls{
                id, shortUrl, normalUrl
            }
        }
        """
        expected = { "urls": [] }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_create_url(self):
        mutation = """
        mutation{
            createUrl(url:"7geese.com"){
                url{id, shortUrl, normalUrl}
            }
        }
        """
        mutation = schema.execute(mutation)
        assert not mutation.errors

    def test_url(self):

        mutation = """
        mutation{
            createUrl(url:"7geese.com"){
                url{id, shortUrl, normalUrl}
            }
        }
        """
        mutation_result = schema.execute(mutation)
        assert not mutation_result.errors
        query = """
        query{url(url:"7geese.com"){
                id, shortUrl, normalUrl
             }
        }
        """
        query_result = schema.execute(query)
        assert not query_result.errors
        assert mutation_result.data.get('createUrl') == query_result.data
