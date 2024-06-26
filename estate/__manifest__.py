{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Manage our real estate',
    'description': "estate",
    'depends': [
        'base_setup',
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/estate_propert_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
