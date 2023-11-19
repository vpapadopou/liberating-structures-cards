import unittest
from unittest.mock import patch, mock_open
from translate_svg import prepare_svg_print


class TestPrepareSVGPrint(unittest.TestCase):
    @patch("translate_svg.open", new_callable=mock_open)
    @patch("translate_svg.os.listdir")
    def test_prepare_svg_print(self, mock_listdir, mock_open):
        lang_to = "fr"
        label_size = "A4"

        # Mocking files in the directory
        mock_listdir.return_value = ["file1.svg", "file2.svg"]

        prepare_svg_print(lang_to, label_size)

        # Assertions based on the behavior of your function
        # For example, check if the files are opened and written correctly with the expected content

        # Check if the files are opened and written with the correct content and filenames based on your function's behavior
        # mock_open.assert_any_call(
        #     f"print/{lang_to}/{label_size.lower()}/print-{label_size.lower()}-page1.svg",
        #     "w",
        # ).write.assert_called_once()

        # Assert other aspects of the function's behavior based on your implementation


if __name__ == "__main__":
    unittest.main()
