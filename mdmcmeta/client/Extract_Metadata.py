import os 
import time
from mdmcmeta.schema import MetadataCreate
from PIL import Image
from pathlib import Path
from datetime import datetime
import img_importer



def extract_metadata(path,user):
    #Take pillow obj from img_importer and path
    image=read_image(path)
    #Fill the obj from schema with our metadata
    out=MetadataCreate(  
        username=user,
        filename=Path(path).name,
        width=image.width,
        height=image.height,
        size=os.path.getsize(path),
        date=datetime.fromtimestamp(os.path.getctime(path)),
        n_channels=len(image.getbands()),
    )
    #return the obj
    return out
#JUST FOR TEST
if __name__ == "__main__":
    out=extract_metadata("/home/user00/mdmcmeta/esempio","ggg")
    print(out)
    

    