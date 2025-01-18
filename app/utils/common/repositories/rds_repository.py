from .repository import Repository
from ..glue import Glue
from ..services import LogService


class RDSRepository(Repository):
    def __init__(
        self,
        glue: Glue,
        log: LogService
    ):
        super().__init__(glue, log)
