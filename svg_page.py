def pre_full_page_svg():
    name_page = "print-a4-full.svg"
    yield '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
    yield "<!-- Created with Inkscape (http://www.inkscape.org/) -->"
    yield '<svg width="297mm" height="210mm" viewBox="0 0 1122.5197 793.70081" version="1.1" id="svg1"'
    yield 'xml:space="preserve" inkscape:version="1.3 (0e150ed6c4, 2023-07-21)" sodipodi:docname="' + name_page + '"'
    yield 'inkscape:export-filename="print-a4-full.pdf" inkscape:export-xdpi="96" inkscape:export-ydpi="96"'
    yield 'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"'
    yield 'xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"'
    yield 'xmlns:xlink="http://www.w3.org/1999/xlink"'
    yield 'xmlns="http://www.w3.org/2000/svg"'
    yield 'xmlns:svg="http://www.w3.org/2000/svg">'
    yield '<sodipodi:namedview id="namedview1" pagecolor="#ffffff" bordercolor="#000000" borderopacity="0.25"'
    yield ' inkscape:showpageshadow="2"  inkscape:pageopacity="0.0" inkscape:pagecheckerboard="0"'
    yield 'inkscape:deskcolor="#d1d1d1" inkscape:document-units="mm" inkscape:zoom="0.73142761" inkscape:cx="678.12589"'
    yield 'inkscape:cy="461.42639" inkscape:window-width="1920" inkscape:window-height="1017" inkscape:window-x="-8"'
    yield 'inkscape:window-y="-8" inkscape:window-maximized="1" inkscape:current-layer="layer1">'
    for i in range(1, 10):
        yield f'<inkscape:page x="{1132.5197 * (i - 1)}" y="0" width="1122.5198" height="793.70081" id="page{i}" '
        yield 'margin="0" bleed="0" inkscape:export-filename="../print-a4.pdf" inkscape:export-xdpi="96"'
        yield 'inkscape:export-ydpi="96"/>'
    yield "</sodipodi:namedview>"
    yield '<defs id="defs1" />'


def pre_page_svg(num: int):
    name_page = f"print-a4-page{num}.svg"
    yield '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
    yield "<!-- Created with Inkscape (http://www.inkscape.org/) -->"
    yield '<svg width="297mm" height="210mm" viewBox="0 0 1122.5197 793.70081" version="1.1" id="svg1"'
    yield 'xml:space="preserve" inkscape:version="1.3 (0e150ed6c4, 2023-07-21)" sodipodi:docname="' + name_page + '"'
    yield 'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"'
    yield 'xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"'
    yield 'xmlns:xlink="http://www.w3.org/1999/xlink"'
    yield 'xmlns="http://www.w3.org/2000/svg"'
    yield 'xmlns:svg="http://www.w3.org/2000/svg">'
    yield '<sodipodi:namedview id="namedview1" pagecolor="#ffffff" bordercolor="#000000" borderopacity="0.25"'
    yield ' inkscape:showpageshadow="2"  inkscape:pageopacity="0.0" inkscape:pagecheckerboard="0"'
    yield 'inkscape:deskcolor="#d1d1d1" inkscape:document-units="mm" inkscape:zoom="0.73142761" inkscape:cx="678.12589"'
    yield 'inkscape:cy="461.42639" inkscape:window-width="1920" inkscape:window-height="1017" inkscape:window-x="-8"'
    yield 'inkscape:window-y="-8" inkscape:window-maximized="1" inkscape:current-layer="layer1" />'
    yield '<defs id="defs1" />'


def pre_calque_full_svg(num: int):
    yield f'<g inkscape:label="Calque {num}" inkscape:groupmode="layer" id="layer{num}" '
    yield f'transform="translate({1132.52 * (num - 1)}, 0)">'


def pre_calque_svg(num: int):
    yield f'<g inkscape:label="Calque {num}" inkscape:groupmode="layer" id="layer{num}">'


def page_svg(
    label: str,
    svg: str,
    num: int,
    transform: tuple[str, str],
):
    yield f'<g style="enable-background:new" id="g{num -1}" transform="'
    yield f"matrix(1,0,0,1,{','.join(transform)})"
    yield f'" inkscape:label="{label}">'
    yield svg
    yield "</g>"


def post_calque_svg():
    yield "</g>"


def post_page_svg():
    yield "</svg>"
