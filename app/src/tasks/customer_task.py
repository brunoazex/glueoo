from domain.services.customer_service import CustomerService
from utils.common.services import LogService
from .task import Task


class CustomerTask(Task):
    def __init__(
        self,
        customers: CustomerService,
        log: LogService
    ):
        super().__init__(log)
        self._customers = customers

    def process(self):
        raw_data = self._customers.load()
        transformed_data = self._customers.transform(raw_data)
        self._customers.persist(transformed_data)
