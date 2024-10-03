from pydantic import BaseModel
from datetime import datetime

class MetadataCreat(BaseModel):

	filename: str
	username: str
	width: int
	height: int
	n_channel: int
	date: datetime
	size: int


class MetadataGet(MetadataCreat):

	id: int
