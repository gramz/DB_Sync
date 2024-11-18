from typing import List, Dict, Any
import logging
from .query_builder import QueryBuilder
from ..utils.data_utils import obtener_datos_como_dict

class TableSynchronizer:
    def __init__(self, sql_conn, mysql_conn):
        self.sql_conn = sql_conn
        self.mysql_conn = mysql_conn
        self.query_builder = QueryBuilder()

    def sync_table(self, tabla_local: str, config: Dict[str, Any]):
        try:
            logging.info(f"Iniciando sincronización de tabla {tabla_local}")

            cursor_sql = self.sql_conn.cursor()
            cursor_mysql = self.mysql_conn.cursor()

            # Obtener datos
            query_sql = self.query_builder.generate_select_query(config, es_remoto=True)
            datos_sql = obtener_datos_como_dict(cursor_sql, query_sql)
            datos_mysql = obtener_datos_como_dict(
                cursor_mysql, 
                f"SELECT * FROM {tabla_local}"
            )

            # Procesar cambios
            self._process_changes(
                tabla_local,
                config,
                datos_sql,
                datos_mysql,
                cursor_mysql
            )

            self.mysql_conn.commit()

        except Exception as e:
            logging.error(f"Error sincronizando tabla {tabla_local}: {str(e)}")
            self.mysql_conn.rollback()
            raise
        finally:
            cursor_sql.close()
            cursor_mysql.close()

    def _process_changes(self, tabla_local, config, datos_sql, datos_mysql, cursor):
        id_campo = config['id_campo']

        # Crear índices
        registros_sql = {str(reg[id_campo]): reg for reg in datos_sql}
        registros_mysql = {str(reg[id_campo]): reg for reg in datos_mysql}

        # Identificar cambios
        ids_sql = set(registros_sql.keys())
        ids_mysql = set(registros_mysql.keys())

        self._handle_inserts(tabla_local, config, registros_sql, ids_sql - ids_mysql, cursor)
        self._handle_updates(tabla_local, config, registros_sql, registros_mysql, ids_sql & ids_mysql, cursor)
        self._handle_deletes(tabla_local, config, ids_mysql - ids_sql, cursor)
