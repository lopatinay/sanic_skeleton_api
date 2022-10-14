from tests import BaseTestCase


def _inc(x):
    return x + 1


class BasicTest(BaseTestCase):
    async def test_answer(self):
        self.assertEqual(_inc(3), 4)
