from xml.etree import ElementTree as ET
from os import listdir, path, makedirs, remove
import subprocess

import separe_id
import svg_page

ns_svg: dict[str, str] = {
    "dc": "http://purl.org/dc/elements/1.1/",
    "cc": "http://creativecommons.org/ns#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "svg": "http://www.w3.org/2000/svg",
    "": "http://www.w3.org/2000/svg",
    "xlink": "http://www.w3.org/1999/xlink",
    "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
    "inkscape": "http://www.inkscape.org/namespaces/inkscape",
}


def clean_xml_svg_g(line):
    for c in (
        '="http://www.w3.org/2000/svg"',
        ':inkscape="http://www.inkscape.org/namespaces/inkscape"',
        ':sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"',
        ':xlink="http://www.w3.org/1999/xlink"',
    ):
        line = line.replace(" xmlns" + c, "")
    return line


def prepare_svg_print(lang_to: str, label_size: str):
    ids = {}
    id_duplicate = []
    path_in: str = f"cards/{lang_to}/"
    path_to: str = f"print/{lang_to}/"
    path_print: str = f"{path_to}{label_size}/"
    if not path.exists(path_to):
        makedirs(path_to)
    if not path.exists(path_print):
        makedirs(path_print)

    files_svg = listdir(path_in)
    limit = len(files_svg)
    for ns_key, ns_value in ns_svg.items():
        ET.register_namespace(ns_key, ns_value)

    width: float = 223.23104
    height: float = 350.78546
    coordinates = [
        (
            str(svg_page.sizes[label_size][4] + x * width),
            str(svg_page.sizes[label_size][5] + y * height),
        )
        for y in range(2)
        for x in range(4)
    ]
    lines_full = "\n".join(svg_page.pre_full_page_svg(label_size=label_size))
    for num, i in enumerate(range(0, limit, 8), start=1):
        files_svg_list = files_svg[i : min(limit, i + 8)]
        lines = "\n".join(svg_page.pre_page_svg(num=num, label_size=label_size))
        pre_calque = "\n".join(svg_page.pre_calque_svg(num=num))
        pre_full_calque = "\n".join(svg_page.pre_calque_full_svg(num=num))
        calque = ""
        for nfile, file in enumerate(files_svg_list):
            svg = ""
            arbre_svg = ET.parse(path_in + file)
            racine_svg = arbre_svg.getroot()
            for g_element in racine_svg.findall("./g", ns_svg):
                svg += ET.tostring(
                    g_element,
                    encoding="utf8",
                    xml_declaration=False,
                ).decode("utf8")
                svg = clean_xml_svg_g(svg)
            id_duplicate = separe_id.find_duplicate(file, svg, ids, id_duplicate)

            calque += "\n".join(
                svg_page.page_svg(
                    num=num,
                    transform=coordinates[nfile],
                    label=file[:-4],
                    svg=svg,
                )
            )
        calque += "\n".join(svg_page.post_calque_svg())
        lines += pre_calque + calque
        lines_full += pre_full_calque + calque
        lines += "\n".join(svg_page.post_page_svg())
        with open(
            f"{path_print}print-{label_size.lower().replace(' ', '-')}-page{num}.svg",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(lines)

    lines_full += "\n".join(svg_page.post_page_svg())
    with open(
        f"{path_print}print-{label_size.lower().replace(' ', '-')}-full.svg",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(lines_full)


def to_pdf(lang_to, label_size):
    path_in: str = f"print/{lang_to}/{label_size}/"
    path_pdf: str = f"print/{lang_to}/"
    pdf_file = f"{path_pdf}print-{label_size.lower().replace(' ', '-')}.pdf"
    subprocess.run(
        [
            "c:/tools/Inkscape/bin/inkscape",
            f"{path_in}print-{label_size.lower().replace(' ', '-')}-full.svg",
            "--export-type=pdf",
            "--export-filename",
            pdf_file,
        ]
    )


if __name__ == "__main__":
    # Choose your language here en, fr, es, ... and size A4 or US Letter.
    prepare_svg_print("fr", "A4")
    to_pdf("fr", "A4")
