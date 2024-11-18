from src.config.logging_config import setup_logging
from src.scheduler.task_scheduler import SyncScheduler

def main():
    # Configurar logging
    setup_logging()

    # Iniciar el scheduler
    SyncScheduler.start()

if __name__ == "__main__":
    main()
