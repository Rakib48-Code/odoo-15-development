from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ], string='Gender')
    ref = fields.Char(string='Reference', tracking=True)
    active = fields.Boolean(string='Active', default=True)