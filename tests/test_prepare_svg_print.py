import unittest
from unittest.mock import patch, mock_open
from prepare_print import prepare_svg_print


class TestPrepareSVGPrint(unittest.TestCase):
    @patch("prepare_print.open", new_callable=mock_open)
    @patch("prepare_print.listdir")
    @patch("prepare_print.ET.parse")
    def test_prepare_svg_print(self, mock_listdir, mock_open, mock_parse):
        lang_to = "fr"
        label_size = "small"

        # Mocking files in the directory
        mock_listdir.return_value = ["file1.svg", "file2.svg"]

        # Mocking the open function
        mock_open.return_value = mock_open(
            f"print/{lang_to}/{label_size.lower()}/print-{label_size.lower()}-page1.svg"
        )

        # Assert that the open function was called with the correct arguments
        mock_open.assert_called_once_with(
            f"print/{lang_to}/{label_size.lower()}/print-{label_size.lower()}-page1.svg",
        )

        # Assert that the write function was called with the correct arguments
        # mock_open.return_value.write.assert_called_once_with("")

        # Run the function with mocked parameters
        prepare_svg_print(lang_to, label_size)


if __name__ == "__main__":
    unittest.main()
