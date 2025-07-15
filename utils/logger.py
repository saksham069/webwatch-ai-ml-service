import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.StreamHandler(),  # logs to console
        logging.FileHandler("ml_service.log")  # logs to file
    ]
)

logger = logging.getLogger("ml-service")
