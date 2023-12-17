from os import listdir
import re


def replace_id(file: str, svg: str, id_duplicate: list[str]):
    # if find key on id_duplicate, replace with key suffix file name
    suffix = "".join([i[0] for i in file.split(".")[0].split("-")])
    for key in id_duplicate:
        val = '"' + key + '"'
        val_href = '"#' + key + '"'
        if val in svg:
            svg = svg.replace(val, f'"{key}_{suffix}"')
        if val_href in svg:
            svg = svg.replace(val_href, f'"#{key}_{suffix}"')
    return svg


def walk(lang: str):
    path = f"cards/{lang}/"
    ids = {}
    id_duplicate = []
    for file in listdir(path):
        with open(path + file, "r", encoding="utf-8") as fp:
            svg = fp.read()
            id_duplicate = find_duplicate(file, svg, ids, id_duplicate)

    for file in listdir(path):
        with open(path + file, "r", encoding="utf-8") as fp:
            svg = fp.read()
            svg = replace_id(file, svg, id_duplicate)

        with open(path + file, "w", encoding="utf-8", newline="\n") as fpw:
            fpw.write(svg)


def find_duplicate(file: str, svg: str, ids: dict[str, str], id_duplicate: list[str]):
    # write regexp xlink:href="#(.+?)" or n6:href="#(.+?)"
    for match in re.findall(r':href="#(.+?)"', svg):
        if match in ids:
            print("Duplicate", match, file, ids[match])
            id_duplicate.append(match)
        else:
            ids[match] = file
    return id_duplicate


if __name__ == "__main__":
    walk("en")
