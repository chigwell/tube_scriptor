import unittest
from unittest.mock import patch, Mock
from tube_scriptor.scriptor import fetch_transcript, extract_video_id


class TestTubeScriptor(unittest.TestCase):
    def test_extract_video_id_from_url(self):
        url = "https://www.youtube.com/watch?v=exampleVideoId"
        self.assertEqual(extract_video_id(url), "exampleVideoId")
        short_url = "https://youtu.be/exampleVideoId"
        self.assertEqual(extract_video_id(short_url), "exampleVideoId")
        self.assertEqual(extract_video_id("exampleVideoId"), "exampleVideoId")

    @patch('tube_scriptor.scriptor.requests.get')
    def test_fetch_transcript_list_format(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'''<?xml version="1.0" encoding="utf-8"?><transcript><text start="0.0" dur="3.24">Text 1</text><text start="3.24" dur="1.8">Text 2</text></transcript>'''
        mock_get.return_value = mock_response

        response = fetch_transcript("exampleVideoId", "list")
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]['text'], "Text 1")
        self.assertEqual(response[0]['start'], 0.0)
        self.assertEqual(response[0]['dur'], 3.24)

    def test_invalid_video_id(self):
        with self.assertRaises(ValueError):
            extract_video_id("https://not_a_valid_link")

    @patch('tube_scriptor.scriptor.requests.get')
    def test_non_200_response(self, mock_get):
        mock_get.return_value = Mock(status_code=404)

        with self.assertRaises(Exception):
            fetch_transcript("invalidVideoId", "string")
