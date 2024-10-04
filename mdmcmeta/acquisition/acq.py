import numpy as np
from PIL import Image
from pathlib import Path


def generate_grayscale(w: int, h: int, path: Path):
    array = np.random.randint(0, 256, size=(w, h), dtype=np.uint8)
    image = Image.fromarray(array, mode="L")
    image.save(path)
