from .repository import Repository
from ..services import LogService
from ..glue import Glue


class S3Repository(Repository):
    def __init__(self, path: str, glue: Glue, log: LogService):
        super().__init__(glue, log)
        self._path = path
