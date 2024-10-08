# mdmcmeta


## Client

A command line client that can be called for posting metadata to the metadata
repo or to query the metadata repo.

### Post

```
client post <image_path> -u/--user <username>
# Extracts metadata from image_path and posts it
```

### Query

```
client query [-u/--user USER] [--max-width W]
# Without arguments, it returns all the records
# With -u, filters by users
# With --max-width, filters by max width

If multiple flags are provided, filter on each one.

Hints: 
* Use httpx to execute http calls
* Use pydantic models to format and validate the metadata
```

## Server

A server that acts as a simple metadata repository.

```
GET /api/metadata/
# return all records
GET /api/metadata/<id>
# Returns single record by id
GET /api/metadata/?user=USER&max-width=W
# return all records matching query

POST /api/metadata/
payload: MetadataCreate (already implemented, see repo)
response:
    status: 201 CREATED
    body: MetadataGet of the object stored in DB
```
