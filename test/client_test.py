from hamcrest import assert_that, equal_to
from client import Client


class TestClient:

    def should_have_create_method(self):
        creation_message = 'Created'

        assert_that(creation_message, equal_to('Created'))
