from xml.etree import ElementTree as ET
import json
import os

# Namespace orignal file
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


def translate_text_svg(lang_to: str):
    try:
        with open(f"translate/en_{lang_to}.json", "r", encoding="utf-8") as fp:
            it: dict[str, str] = json.load(fp)
    except FileNotFoundError:
        it = {}

    els: tuple[str, ...] = ("tspan", "flowPara")
    path: str = "cards/en/"
    path_to: str = f"cards/{lang_to}/"
    if not os.path.exists(path_to):
        os.makedirs(path_to)

    for root, dirs, files in os.walk(path):
        for file in files:
            arbre_svg = ET.parse(path + file)
            racine_svg = arbre_svg.getroot()
            for el in els:
                for text_element in racine_svg.findall(".//" + el, ns_svg):
                    if text_element.text:
                        from_text = text_element.text.strip()
                        if from_text not in it:
                            it[from_text] = ""
                        elif it[from_text] != "":
                            # Update text to SVG file
                            text_element.text = it[from_text]
            arbre_svg.write(f"{path_to}/{file}")

    with open(f"translate/en_{lang_to}.json", "w", encoding="utf-8") as fp:
        json.dump(it, fp, indent=2)


if __name__ == "__main__":
    translate_text_svg("es")
