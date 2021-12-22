"""Test cases for action : start ariel search."""
import json
import logging
import os
import sys
import requests
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import (
    PluginException,
    ClientException,
)

from icon_ibm_qradar.actions.start_ariel_search import StartArielSearch
from icon_ibm_qradar.connection.connection import Connection

sys.path.append(os.path.abspath("../"))


class TestStartArielSearch(TestCase):
    """Test case class for action : Start ariel search."""

    def test_start_ariel_search(self):
        """To test the areial search.

        :return: None
        """
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = StartArielSearch()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("tests/start_ariel_search.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except FileNotFoundError:
            message = "Could not find or read sample tests file or dir "
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertTrue(isinstance(results.get("data"), dict))
        self.assertTrue(isinstance(results.get("data")["cursor_id"], str))

    def test_start_ariel_search_wrong_hostname(self):
        """To test the ariel search with wrong aql.

        :return: None
        """
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = StartArielSearch()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("tests/start_ariel_search_with_wrong_aql.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except FileNotFoundError:
            message = "Could not find or read sample tests file or dir "
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn

        with self.assertRaises(PluginException):
            test_action.run(action_params)

    def test_start_ariel_search_wrong_aql(self):
        """To test the ariel search with wrong host.

        :return: None
        """
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = StartArielSearch()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("tests/start_ariel_search_with_wrong_hostname.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except FileNotFoundError:
            message = "Could not find or read sample tests file or dir "
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn

        with self.assertRaises(requests.exceptions.ConnectionError):
            test_action.run(action_params)

    def test_start_ariel_search_empty_aql(self):
        """To test the ariel search with wrong host.

        :return: None
        """
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = StartArielSearch()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("tests/start_ariel_search_with_empty_aql.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except FileNotFoundError:
            message = "Could not find or read sample tests file or dir "
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn

        with self.assertRaises(ClientException):
            test_action.run(action_params)
