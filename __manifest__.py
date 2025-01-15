{
    'name' : 'Odoo 15 Develpoment',
    'version' : '15.0.0.1.1',
    'category' : 'Odoo 15 Tutorial',
    'summary':'Development Tutorial',
    'description': 'Odoo 15 full development tutorials.',
    'depends' : ['mail','product'],
    'data': [

        # security file
        'security/ir.model.access.csv',

        # wizard file
        'wizard/cancel_appointment_wizard.xml',


        # view file
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/male_patient.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
    ],
    'installable': True,
    'application': True,
}