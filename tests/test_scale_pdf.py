import unittest
from unittest.mock import patch, MagicMock
from typing import Tuple
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter, landscape
from translate_svg import scale, to_pdf


class TestScaleAndPDF(unittest.TestCase):
    def test_scale(self):
        drawing = MagicMock()
        drawing.minWidth.return_value = 100
        drawing.height = 200

        scaled_drawing = scale(drawing, scaling_factor=0.85)

        self.assertEqual(scaled_drawing.width, 85)  # Check if width is correctly scaled
        self.assertEqual(
            scaled_drawing.height, 170
        )  # Check if height is correctly scaled

    @patch("translate_svg.canvas.Canvas")
    @patch("translate_svg.svg2rlg")
    @patch("translate_svg.renderPDF")
    @patch("translate_svg.os.listdir")
    @patch("translate_svg.scale")
    def test_to_pdf(
        self, mock_scale, mock_listdir, mock_renderPDF, mock_svg2rlg, mock_canvas
    ):
        lang_to = "fr"
        pagesize_label = "A4"
        pagesize = (595.2755905511812, 841.8897637795277)  # Taille A4 par exemple

        # Mocking files in the directory
        mock_listdir.return_value = ["file1.svg", "file2.svg"]

        # Run the function with mocked parameters
        to_pdf(lang_to, pagesize_label, pagesize)

        # Assertions based on the behavior of your function
        # For example, check if Canvas is created with the expected arguments
        mock_canvas.assert_called_with(
            f"print/{lang_to}/print-{pagesize_label}.pdf", pagesize=landscape(pagesize)
        )

        # Assert other method calls and behavior within your function based on your specific implementation

        # Check if showPage is called the right number of times, depending on the number of SVG files
        self.assertEqual(
            mock_canvas().showPage.call_count, 2
        )  # Modify as needed based on your scenario

        # Assert other aspects of the function's behavior based on your implementation


if __name__ == "__main__":
    unittest.main()
