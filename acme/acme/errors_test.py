"""Tests for acme.errors."""
import datetime
import unittest

import mock


class BadNonceTest(unittest.TestCase):
    """Tests for acme.errors.BadNonce."""

    def setUp(self):
        from acme.errors import BadNonce
        self.error = BadNonce(nonce="xxx", error="error")

    def test_str(self):
        self.assertEqual("Invalid nonce ('xxx'): error", str(self.error))


class MissingNonceTest(unittest.TestCase):
    """Tests for acme.errors.MissingNonce."""

    def setUp(self):
        from acme.errors import MissingNonce
        self.response = mock.MagicMock(headers={})
        self.response.request.method = 'FOO'
        self.error = MissingNonce(self.response)

    def test_str(self):
        self.assertTrue("FOO" in str(self.error))
        self.assertTrue("{}" in str(self.error))


class PollErrorTest(unittest.TestCase):
    """Tests for acme.errors.PollError."""

    def setUp(self):
        from acme.errors import PollError
        self.timeout = PollError(
            waiting=[(datetime.datetime(2015, 11, 29), mock.sentinel.AR)],
            updated={})
        self.invalid = PollError(waiting=[], updated={
            mock.sentinel.AR: mock.sentinel.AR2})

    def test_timeout(self):
        self.assertTrue(self.timeout.timeout)
        self.assertFalse(self.invalid.timeout)

    def test_repr(self):
        self.assertEqual('PollError(waiting=[], updated={sentinel.AR: '
                         'sentinel.AR2})', repr(self.invalid))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
