import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from utils.common.glue import Glue
from utils.common.services import LogService, CacheService
from domain.repositories.customer_repository import (
    CustomerSourceRepository,
    CustomerTargetRepository
)
from domain.services.customer_service import CustomerService
from utils.common.repositories import S3Repository
from tasks.customer_task import CustomerTask
from tasks.task import Task
from typing import List


class Entrypoint:
    def __init__(
        self,
        glue_context: GlueContext
    ):
        self.glue = Glue(
            glue_context.spark_session,
            glue_context
        )

        self.log = LogService("TASK")
        self.cache = CacheService(S3Repository("cache", self.glue, self.log))

        self.customers_src = CustomerSourceRepository(self.glue, self.log)
        self.customers_target = CustomerTargetRepository(self.glue, self.log)
        self.customers_svc = CustomerService(
            self.customers_src, self.customers_target
        )
        self.customers = CustomerTask(self.customers_svc, self.log)
        self.task_handlers = {
            CustomerTask: self.customers
        }

    def run(self, tasks: List[Task]):
        for task in tasks:
            handler = self.task_handlers[task]
            try:
                handler.execute()
            except Exception as exc:
                self.log.error(exc)


if __name__ == '__main__':
    args = getResolvedOptions(
        sys.argv,
        ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH']
    )
    sc = SparkContext()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session
    job = Job(glueContext)
    job.init(args['JOB_NAME'], args)

    entry = Entrypoint(glueContext)
    entry.run(
        [
            CustomerTask
        ]
    )
