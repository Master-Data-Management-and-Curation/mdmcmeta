from mdmcmeta.schema  import MetadataCreate
from httpx import post
from pydantic import json

def handle_meta(meta)
    payload=model.model_dump_json(meta)  # model.model_dump_json transforms to a serializable object
    ##dict_meta = {"filename":meta.filename,"username":meta.username,"width":meta.width,"height":meta.height,"n_channel":meta.n_channel,"date":meta.date,"size":meta.size} 


    do_post = httpx.request(POST,f"{HOST}:{PORT}/api/metadata", json=payload) # json è un serializable oject



