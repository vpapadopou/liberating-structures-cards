import subprocess
from os import listdir


def to_png(lang_to):
    path_in: str = f"cards/{lang_to}/"
    path_png: str = f"png/{lang_to}/"
    for svg in listdir(path_in):
        # print(
        subprocess.run(
            [
                "c:/tools/Inkscape/bin/inkscape",
                f"{path_in}{svg}",
                "--export-type=png",
                "--export-area=30:20:250:377",
                # "--export-overwrite",
                "--export-filename",
                f"{path_png}{svg[:-4]}.png",
            ]
        )


if __name__ == "__main__":
    to_png("en")
    to_png("fr")
