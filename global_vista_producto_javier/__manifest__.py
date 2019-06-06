# -*- coding: utf-8 -*-
{
    'name': "Vista de productos",
    'description': """
        vista de productos con campos ninguno por default 
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': [
                'base',
                'stock',
                
                ],
    'data': [
        'views/global_view_producto.xml',
       
        ],
    'installable':True,
    'auto_install':False,
}
