from unittest import TestCase

import msgpack
from django.forms.utils import ErrorList


class MsgpackTestCase(TestCase):
    def test_errorlist(self):
        data = ErrorList("T")

        raw = msgpack.packb(data)

        msgpack.unpackb(raw)
