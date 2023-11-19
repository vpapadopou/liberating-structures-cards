from xml.etree import ElementTree as ET
import json
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen import canvas


def translate_text_svg(lang_to: str):
    # Namespace orignal file
    ns: dict[str, str] = {
        "dc": "http://purl.org/dc/elements/1.1/",
        "cc": "http://creativecommons.org/ns#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "svg": "http://www.w3.org/2000/svg",
        "": "http://www.w3.org/2000/svg",
        "xlink": "http://www.w3.org/1999/xlink",
        "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
        "inkscape": "http://www.inkscape.org/namespaces/inkscape",
    }

    try:
        with open("translate//en_{lang_to}.json", "r", encoding="utf-8") as fp:
            it: dict[str, str] = json.load(fp)
    except FileNotFoundError:
        it = {}

    els: list[str] = ("tspan", "flowPara")
    path: str = "cards/en"
    for root, dirs, files in os.walk(path):
        for file in files:
            arbre_svg = ET.parse(path + file)
            racine_svg = arbre_svg.getroot()
            for el in els:
                for text_element in racine_svg.findall(".//" + el, ns):
                    if text_element.text:
                        from_text = text_element.text.strip()
                        if from_text not in it:
                            it[from_text] = ""
                        elif it[from_text] != "":
                            # Update text to SVG file
                            text_element.text = it[from_text]

            arbre_svg.write(f"{path}../{lang_to}/{file}")

    with open(f"translate/en_{lang_to}.json", "w", encoding="utf-8") as fp:
        json.dump(it, fp, indent=2)


def prepare_svg_print(lang_to: str, label_size):
    path: str = f"cards/{lang_to}/"
    path_print: str = f"print/{lang_to}/{label_size}/"

    width: int = 238
    height: int = 375
    coordinates = [(x * width, y * height) for y in range(2) for x in range(4)]

    width_mm = 74
    height_mm = 105

    files_svg = os.listdir(path)
    limit = len(files_svg)
    for n in range(int(limit / 8) + 1):
        svg_content = f"""<?xml version="1.0"?>
        <svg width="{width_mm*4}mm" height="{height_mm*2}mm" xmlns="http://www.w3.org/2000/svg">"""

        for i in range(8):
            if (8 * n) + i < limit:
                with open(path + files_svg[(8 * n) + i], "r") as f:
                    svg_initial = f.read()
                    x, y = coordinates[i]
                    svg_content += (
                        f'<g transform="translate({x}, {y})">{svg_initial}</g>'
                    )

        # svg_content += '<rect x="0mm" y="0mm" width="277mm" height="190mm" fill="none" stroke="black" />'
        svg_content += "</svg>"

        with open(
            f"{path_print}print-{label_size.lower()}-page{n+1}.svg", "w"
        ) as file_svg:
            file_svg.write(svg_content)


def scale(drawing, scaling_factor):
    # https://www.blog.pythonlibrary.org/2018/04/12/adding-svg-files-in-reportlab/
    """
    Scale a reportlab.graphics.shapes.Drawing()
    object while maintaining the aspect ratio
    """
    scaling_x = scaling_factor
    scaling_y = scaling_factor

    drawing.width = drawing.minWidth() * scaling_x
    drawing.height = drawing.height * scaling_y
    drawing.scale(scaling_x, scaling_y)
    return drawing


def to_pdf(lang_to: str, pagesize_label: str, pagesize: tuple[float, float]):
    path: str = "cards/" + lang_to
    file_pdf: str = f"print/{lang_to}/print-{pagesize_label}.pdf"

    canv: canvas.Canvas = canvas.Canvas(file_pdf, pagesize=landscape(pagesize))

    files_svg = os.listdir(path)
    for file in files_svg:
        if file.endswith(".svg"):
            drawing = svg2rlg(os.path.join(path, file))
            renderPDF.draw(drawing, canv, 0, 0)
            canv.setPageSize(landscape(pagesize))
            scaled_drawing = scale(drawing, scaling_factor=0.85)
            renderPDF.draw(scaled_drawing, canv, 0, 40)
            canv.showPage()
    canv.save()


if __name__ == "__main__":
    # Prepare translation
    # translate_text_svg("fr")
    # Prepare page
    prepare_svg_print("fr", "A4")
    # Transform to pf
    # FIXME ttf and apply svg in page
    to_pdf("fr", "a4", A4)
