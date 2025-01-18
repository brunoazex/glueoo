import logging


class LogService:
    def __init__(
        self,
        name: str,
        level=logging.INFO
    ):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

    def __getattr__(self, attr):
        return getattr(self._logger, attr)
