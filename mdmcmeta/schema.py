from pydantic import BaseModel  #this library do for us serialization and deserialization
from datetime import datetime

class MetadataCreate(BaseModel):
    filename: str
    username: str
    width: int
    height: int
    n_channels: int
    date: datetime
    size: int

class MetadataGet(MetadataCreate):
    id: int

    
