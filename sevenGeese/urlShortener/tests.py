from django.test import TestCase

from graphene.test import Client

from sevenGeese.schema import schema


class GraphQLTestCase(TestCase):

    def test_urls(self):

        query = """
        query{
            urls{
                shortUrl
            }
        }
        """
        expected = { "urls": {"shortUrl": None}}
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected


    def test_url(self):

        query = """
        query{
            urls(url:"7geese.com"){
                shortUrl
            }
        }
        """
        result = schema.execute(query)
        assert not result.errors
