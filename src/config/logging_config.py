import logging
import os
from datetime import datetime

def setup_logging():
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_filename = os.path.join(
        log_directory, 
        f"sync_{datetime.now().strftime('%Y%m%d')}.log"
    )

    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
