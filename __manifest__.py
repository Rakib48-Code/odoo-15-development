{
    'name' : 'Odoo 15 Develpoment',
    'version' : '15.0.0.1.1',
    'category' : 'Odoo 15 Tutorial',
    'summary':'Development Tutorial',
    'description': 'Odoo 15 full development tutorials.',
    'depends' : [],
    'data': [

        # security file
        'security/ir.model.access.csv',


        # view file
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'installable': True,
    'application': True,
}