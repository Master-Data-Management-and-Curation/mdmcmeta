import numpy as np
from PIL import Image
from pathlib import Path
import sys


def generate_image(w: int, h: int, mode: str, path: Path):
    if mode == "L":
        size = (w, h)
    elif mode == "RGB":
        size = (w, h, 3)
    elif mode == "RGBA":
        size = (w, h, 4)
    else:
        print("Wrong mode!")
        return

    array = np.random.randint(0, 256, size=size, dtype=np.uint8)
    image = Image.fromarray(array, mode=mode)
    image.save(path)


if __name__ == "__main__":
    w = int(sys.argv[1])
    h = int(sys.argv[2])
    mode = sys.argv[3]
    path = Path(sys.argv[4])

    generate_image(w, h, mode, path)
