import unittest
from unittest.mock import patch, MagicMock
from translate_svg import translate_text_svg


class TestTranslateTextSVG(unittest.TestCase):
    @patch("translate_svg.ET.parse")
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    @patch("translate_svg.json")
    @patch("translate_svg.os.walk")
    def test_translate_text_svg(self, mock_walk, mock_json, mock_open, mock_parse):
        # Mock the necessary functionalities to test translate_text_svg

        # Mock the file content that should be loaded for en_{lang_to}.json
        mock_json.load.return_value = {
            "Hello": "Bonjour",
            "Goodbye": "Au revoir"
            # Add other key-value pairs for testing scenarios
        }

        # Mock the behavior of os.walk to simulate files in the directory
        mock_walk.return_value = [("/path", [], ["example.svg"])]

        # Run the function with a mocked language parameter
        lang_to = "fr"
        translate_text_svg(lang_to)

        # Add assertions to verify the behavior of your function
        # For example, check if the write method is called with the expected arguments

        # Assert the open and write calls as per your function's behavior
        mock_open.assert_called_with(
            f"translate/en_{lang_to}.json", "w", encoding="utf-8"
        )
        mock_json.dump.assert_called_once()  # You might want to check the exact arguments passed

        # Assert the behavior based on the functionality of your function


if __name__ == "__main__":
    unittest.main()
