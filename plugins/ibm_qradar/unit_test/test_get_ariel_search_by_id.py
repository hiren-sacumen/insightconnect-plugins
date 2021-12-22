"""Test cases for get ariel search by id end point action."""
import json
import logging
import os
import sys
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException, ClientException

from icon_ibm_qradar.actions.get_ariel_search_by_id import GetArielSearchById
from icon_ibm_qradar.connection.connection import Connection

sys.path.append(os.path.abspath("../"))


class TestGetArielSearchById(TestCase):
    """Unit Test class for Test cases of action : get ariel search by id."""

    def test_get_ariel_search_by_id(self):
        """To Test the get serial search by id."""
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetArielSearchById()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("tests/get_ariel_search_by_id.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except FileNotFoundError:
            message = """Could not find or read sample tests from / dir"""
            self.fail(message)

        with self.assertRaises(PluginException):
            test_conn.connect(connection_params)
            test_action.connection = test_conn
            test_action.run(action_params)

    def test_get_ariel_search_by_id_with_empty_searchid(self):
        """To Test the get serial search by id."""
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetArielSearchById()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("tests/get_ariel_search_by_id_with_empty_search_id.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except FileNotFoundError:
            message = """Could not find or read sample tests from / dir"""
            self.fail(message)

        with self.assertRaises(ClientException):
            test_conn.connect(connection_params)
            test_action.connection = test_conn
            test_action.run(action_params)
