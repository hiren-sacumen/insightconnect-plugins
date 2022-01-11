import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import ClientException, PluginException

from icon_ibm_qradar.actions.get_offense_note import GetOffenseNote
from unit_test.helpers.offense_note import OffenseNotesHelper

sys.path.append(os.path.abspath("../"))


class TestGetOffenseNote(TestCase):
    """Test case class for action : Get offense notes."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = OffenseNotesHelper.default_connector(GetOffenseNote())

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes(self, make_request):
        """To get the offense notes.

        :return: None
        """
        action_params = {"offense_id": "33"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_without_offense_id(self, make_request):
        """To get offense notes without offense id provided.

        :return: None
        """
        action_params = {}
        with self.assertRaises(ClientException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_with_fields(self, make_request):
        """To get offense notes with field list given.

        :return: None
        """
        action_params = {"offense_id": "33", "fields": "id"}
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_with_filter(self, make_request):
        """To get offense notes with given filter.

        :return: None
        """
        action_params = {"offense_id": "33", "filter": "id=10001"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To Test the get offense notes by id with internalServerError."""
        action_params = {"offense_id": "33", "filter": "internalServerError"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)
