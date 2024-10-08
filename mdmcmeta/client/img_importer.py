from pathlib import Path
from sys import argv
from sys import stderr
from PIL import Image
from PIL import UnidentifiedImageError
import os

def read_image(input_file):
    ext=input_file.suffix
    if ext != '.png' :
            raise Exception('Il file non è di tipo png')
            #print ('Il file non è di tipo png')
            #return
    else:
        try:
            image=Image.open(input_file)
        except UnidentifiedImageError as e:
            raise e
            #print(f'Errore: {e}',file=sys.stderr)
            #return
        except OSError as e:
            raise e
            #print('Errore di apertura file: {e}', file=sys.stderr)
            #return
        return image

if __name__ == "__main__":
    # 1. The program accepts as input a folder or a single file containing PNG image
    try:
        input = Path(argv[1])
    except IndexError:
        print("Usage: <input>", file=stderr)
        exit(1)

    image = read_image(input)
    #image.save('output.png')
    #print(image)
