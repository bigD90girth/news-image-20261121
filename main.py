"""Copy the entry image to the output directory.

The image is the entry: a newspaper front page summing up Saturday
21 November 2026 — Iran saying it struck two U.S. bases in Bahrain,
the Russian missile on Kryvyi Rih, the capture of cartel boss
"El Chapo Isidro" in Sinaloa, COP31 running past its deadline with
no deal, the market slide as AI shares fell, and 39 more stories
from seven regions, with a markets strip. The program only moves
its bytes, so both runs write the same file. No network, no
rendering at run time: the page is fixed in the repository.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
