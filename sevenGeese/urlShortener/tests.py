from django.test import TestCase

from sevenGeese.schema import schema


class GraphQLTestCase(TestCase):

    def test_url(self):

        mutation = """
        query{
            url(url:"7geese.com"){
                url
            }
        }
        """
        result = schema.execute(mutation)
        assert not result.errors
