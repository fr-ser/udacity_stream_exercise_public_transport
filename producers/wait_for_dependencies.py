"""Used in local development (and docker) to wait until all services started"""

from shared_helpers.logging import logger
from shared_helpers.wait_until import (
    check_kafka,
    check_schema_registry,
    check_rest_proxy,
    check_kafka_connect,
)


if __name__ == "__main__":
    check_kafka()
    check_schema_registry()
    check_rest_proxy()
    check_kafka_connect()

    logger.info(f"All dependencies are there!")
