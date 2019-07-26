from django.test import TestCase

from graphene.test import Client

from sevenGeese.schema import schema


class GraphQLTestCase(TestCase):

    def test_url(self):

        query = """
        query{
            urls(url:"7geese.com"){
                url
            }
        }
        """
        result = schema.execute(query)
        assert not result.errors
        assert result.data.get('urls').get('url') != '7geese.com'
