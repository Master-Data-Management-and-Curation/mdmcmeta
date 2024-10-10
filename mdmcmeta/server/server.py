from fastapi import FastAPI
from .mockdb import MOCK_DB
from ..schema import MetadataGet, MetadataCreate

app = FastAPI()

@app.get("/")
def root():
    print("hello")
    return "hello"

@app.get("/api/metadata/")
def get_list_metadata(user: str | None = None):
    all_records = []
    for key in MOCK_DB.keys():
        md_create = MOCK_DB[key]
        this_record = MetadataGet(
            id=key,
            filename=md_create.filename,
            username=md_create.username,
            width=md_create.width,
            height=md_create.height,
            n_channels=md_create.n_channels,
            date=md_create.date,
            size=md_create.size,
        )
        all_records.append(this_record)

    if user is not None:
        filtered_by_user = []
        for record in all_records:
            if record.username == user:
                filtered_by_user.append(record)
    else:
        filtered_by_user = all_records

    out = filtered_by_user
    return out

@app.get("/api/metadata/{id}")
def get_single_metadata(id: int):
    record = MOCK_DB[id].model_dump()
    out = MetadataGet(
        id=id,
        **record,
    )
    return out

@app.post("/api/metadata/")
def post_metadata(record: MetadataCreate):
    new_idx = max(MOCK_DB.keys()) + 1
    MOCK_DB[new_idx] = record
    return get_single_metadata(new_idx)
