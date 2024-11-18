TABLA_CONFIG = {
    'clientes_local': {
        'tabla_remota': 'Customers',
        'id_campo': 'id_cliente',
        'mapeo_campos': {
            'id_cliente': 'CustomerID',
            'nombre': 'CustomerName',
            'email': 'EmailAddress',
            'telefono': 'Phone'
        }
    },
    'productos_local': {
        'tabla_remota': 'Products',
        'id_campo': 'id_producto',
        'mapeo_campos': {
            'id_producto': 'ProductID',
            'nombre': 'ProductName',
            'precio': 'UnitPrice',
            'stock': 'UnitsInStock'
        }
    }
}
