import schedule
import time
import logging
from ..core.connectors import SQLServerConnector, MySQLConnector
from ..core.synchronizer import TableSynchronizer
from ..config.table_mappings import TABLA_CONFIG

class SyncScheduler:
    @staticmethod
    def sincronizar_todas_las_tablas():
        try:
            logging.info("Iniciando proceso de sincronización")

            # Establecer conexiones
            sql_conn = SQLServerConnector.connect()
            mysql_conn = MySQLConnector.connect()

            # Crear sincronizador
            synchronizer = TableSynchronizer(sql_conn, mysql_conn)

            # Sincronizar cada tabla
            for tabla_local, config in TABLA_CONFIG.items():
                synchronizer.sync_table(tabla_local, config)

            logging.info("Sincronización completada exitosamente")

        except Exception as e:
            logging.error(f"Error en el proceso de sincronización: {str(e)}")
        finally:
            sql_conn.close()
            mysql_conn.close()

    @staticmethod
    def start():
        logging.info("Iniciando programador de tareas")

        # Programar la tarea cada 4 horas
        schedule.every(4).hours.do(SyncScheduler.sincronizar_todas_las_tablas)

        # Primera ejecución inmediata
        SyncScheduler.sincronizar_todas_las_tablas()

        # Mantener el programa en ejecución
        while True:
            schedule.run_pending()
            time.sleep(60)
