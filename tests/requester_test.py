from unittest import mock
from requests import Response

from util import requester
from util.requester import Requester

import datetime
import unittest


class RequesterTest(unittest.TestCase):
    @mock.patch('requests.get')
    def test_get_request_happy_200(self, mock_get):
        # setup mock response obj
        res = Response()
        res.status_code = 200
        res.elapsed = datetime.timedelta(microseconds=200)
        mock_get.return_value = res

        requesterObj = Requester("TEST_URL")

        my_response = requesterObj.get_request()
        self.assertIsNotNone(my_response, "Customer Response obj not null")
        self.assertEqual(my_response.url, "TEST_URL")
        self.assertEqual(my_response.response_ms, 0.2)
        self.assertEqual(my_response.up_or_down, 1, "")

    @mock.patch('requests.get')
    def test_get_request_happy_503(self, mock_get):
        # setup mock response obj
        res = Response()
        res.status_code = 503
        res.elapsed = datetime.timedelta(microseconds=650)
        mock_get.return_value = res

        requesterObj = Requester("TEST_URL")

        my_response = requesterObj.get_request()
        self.assertIsNotNone(my_response, "Customer Response obj not null")
        self.assertEqual(my_response.url, "TEST_URL")
        self.assertEqual(my_response.response_ms, 0.65)
        self.assertEqual(my_response.up_or_down, 0)

    @mock.patch('requests.get')
    def test_get_request_response_none(self, mock_get):
        # setup mock response obj
        res = None
        mock_get.return_value = res

        requesterObj = Requester("TEST_URL")

        my_response = requesterObj.get_request()
        self.assertIsNotNone(my_response, "Customer Response obj not null")
        self.assertEqual(my_response.url, "TEST_URL")
        self.assertEqual(my_response.response_ms, 0)
        self.assertEqual(my_response.up_or_down, 0)

    def test_converMicroToMilliSeconds(self):
        microseconds = 200
        milliseconds = requester.convertMicroToMilliSeconds(microseconds)

        self.assertEqual(milliseconds, 0.2)

    def test_converMicroToMilliSeconds_None(self):
        microseconds = None
        milliseconds = requester.convertMicroToMilliSeconds(microseconds)

        self.assertEqual(milliseconds, 0)

    def test_converMicroToMilliSeconds_Zero(self):
        microseconds = 0
        milliseconds = requester.convertMicroToMilliSeconds(microseconds)

        self.assertEqual(milliseconds, 0)
