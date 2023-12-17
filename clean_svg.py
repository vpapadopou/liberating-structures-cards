import re
from os import listdir


def clean_files_with_regexp(directory, pattern):
    files = listdir(directory)
    for file in files:
        with open(directory + file, "r", encoding="utf-8") as fp:
            svg = fp.read()
        svg = re.sub(pattern, "", svg)
        with open(directory + file, "w", encoding="utf-8", newline="\n") as fpw:
            fpw.write(svg)


if __name__ == "__main__":
    # clean all files in cards/en/ with regexp to remove empty text.
    clean_files_with_regexp(
        "cards/en/", r"<text[^>]*>(?:\s*<tspan[^>]*>\s*</tspan>\s*)+</text>"
    )
