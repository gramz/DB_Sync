from typing import List, Dict, Any

def obtener_datos_como_dict(cursor, query: str) -> List[Dict[str, Any]]:
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]
