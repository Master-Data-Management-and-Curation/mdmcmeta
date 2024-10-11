from sys import argv, stderr
from pathlib import Path
import os
from datetime import datetime
from PIL import Image
import httpx
from mdmcmeta.schema import MetadataCreate


def extract_metadata(filename, user):
    #Take pillow obj from img_importer and path
    image = Image.open(filename)
    #Fill the obj from schema with our metadata
    out = MetadataCreate(  
        username=user,
        filename=Path(filename).name,
        width=image.width,
        height=image.height,
        size=os.path.getsize(filename),
        date=datetime.fromtimestamp(os.path.getctime(filename)),
        n_channels=len(image.getbands()),
    )
    return out


SERVER_URL = "http://127.0.0.1"
SERVER_PORT = 8000


if __name__ == "__main__":
    if argv[1] == "post":
        # capture from command line the filename
        image_path = argv[2]
        if argv[3] in ("-u", "--user"):
            username = argv[4]
        else:
            print("please provide user. terminating", file=stderr)
            exit(1)


        # extract the metadata from the file with PIL
        # get inspiration from mdmcmeta/client/Extract_Metadata.py
        # using PIL.Image.open() to open the filename as an 
        # image object

        # encapsulate the metadata in the MetadataCreate schema
        md = extract_metadata(filename=image_path, user=username)

        # execute a post request with httpx
        payload = md.model_dump()
        payload["date"] = md.date.isoformat()
        res = httpx.post(
            f"{SERVER_URL}:{SERVER_PORT}/api/metadata/", json=payload
        )
        print(res.json())

    elif argv[1] == "query":
        # parse the remaining arguments and check if we 
        # need to query by user
        username = None
        try:
            if argv[2] in ("-u", "--user"):
                username = argv[3]
        except IndexError:
            pass

        # execute a get request with httpx
        query_string = ""
        if username is not None:
            query_string = f"?user={username}"
        res = httpx.get(
            f"{SERVER_URL}:{SERVER_PORT}/api/metadata/{query_string}"
        )
        print(res.json()) 

    else:
        raise ValueError

    exit(0)
