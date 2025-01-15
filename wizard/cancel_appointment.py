from odoo import api, fields, models

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wiz'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')