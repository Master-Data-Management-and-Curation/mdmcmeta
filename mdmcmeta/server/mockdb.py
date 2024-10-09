from ..schema import MetadataCreate
from datetime import datetime

# NOTE:
# The GET endpoints need a database and some data. For the time being, you may
# mock the data like so:
MOCK_DB = {
    1: MetadataCreate(
        filename = "/first/fname",
        username = "jacopo",
        width = 800,
        height = 600,
        n_channels = 3,
        date = datetime.fromisoformat("2024-10-09"),
        size = 1234,
    ),
    2: MetadataCreate(
        filename = "/second/fname",
        username = "jacopo",
        width = 800,
        height = 600,
        n_channels = 3,
        date = datetime.fromisoformat("2024-10-09"),
        size = 1234,
    ),
    3: MetadataCreate(
        filename = "/third/fname",
        username = "luigi",
        width = 800,
        height = 600,
        n_channels = 3,
        date = datetime.fromisoformat("2024-10-09"),
        size = 1234,
    )
}
