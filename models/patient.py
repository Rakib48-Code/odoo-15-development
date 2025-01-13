from odoo import api, fields, models
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    date_birth = fields.Date(string='Date Birth')
    age = fields.Integer(string='Age', compute='compute_age')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ], string='Gender', default='male')
    ref = fields.Char(string='Reference', tracking=True, default='New Patient')
    active = fields.Boolean(string='Active', default=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string="Status")

    @api.onchange('date_birth')
    def compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_birth:
                rec.age = today.year - rec.date_birth.year
            else:
                rec.age = 0

    def action_draft(self):
        self.state = 'draft'

    def action_in_consultation(self):
        self.state = 'in_consultation'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'
