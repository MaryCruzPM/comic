# -*- coding: utf-8 -*-
{
    'name': "comics_fields required productos",

    'summary': """add_fields
    """,

    'description': """
        Modulo para inventario campos requeridos en inventario 
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
        'contacts',
        ],

	'data': [
     'views/fields_required_invetario.xml',

    ],
	
    'installable':True,
}
