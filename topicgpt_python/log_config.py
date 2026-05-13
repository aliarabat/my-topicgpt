
import logging

logging.getLogger("httpx").setLevel(logging.CRITICAL)

def get_logger(name: str = "topic-gpt", cfg_filename: str = 'application'):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(message)s",
            # handlers=[RichHandler(markup=True)]
            filename=f"{cfg_filename}.log",
        )
        logger.info(f"{name} Logger has been initialized...")

    return logger