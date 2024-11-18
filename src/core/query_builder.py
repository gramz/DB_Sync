from typing import Dict, Any

class QueryBuilder:
    @staticmethod
    def generate_select_query(config: Dict[str, Any], es_remoto: bool = False) -> str:
        campos = config['mapeo_campos']
        if es_remoto:
            campos_select = [f"{campo_remoto} as {campo_local}" 
                           for campo_local, campo_remoto in campos.items()]
            nombre_tabla = config['tabla_remota']
        else:
            campos_select = list(campos.keys())
            nombre_tabla = config['tabla_local']

        return f"SELECT {', '.join(campos_select)} FROM {nombre_tabla}"

    @staticmethod
    def generate_insert_query(tabla: str, campos: list) -> str:
        campos_str = ', '.join(campos)
        placeholders = ', '.join(['%s'] * len(campos))
        return f"INSERT INTO {tabla} ({campos_str}) VALUES ({placeholders})"

    @staticmethod
    def generate_update_query(tabla: str, campos: list, id_campo: str) -> str:
        campos_update = [campo for campo in campos if campo != id_campo]
        return f"UPDATE {tabla} SET " + \
               ', '.join([f"{col} = %s" for col in campos_update]) + \
               f" WHERE {id_campo} = %s"

    @staticmethod
    def generate_delete_query(tabla: str, id_campo: str) -> str:
        return f"DELETE FROM {tabla} WHERE {id_campo} = %s"
