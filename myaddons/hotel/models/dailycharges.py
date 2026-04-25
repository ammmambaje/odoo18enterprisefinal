# -*- coding: utf-8 -*-

from odoo import models, fields


class dailycharges(models.Model):
    _name = 'hotel.dailycharges'
    _inherit = ['hotel.company.mixin']
    _description = 'hotel roomtype daily charges list'

    dailyrate = fields.Float('Daily Rate', digits=(10, 2))
    weekendrate = fields.Float('Weekend Rate', digits=(10, 2))
    amount = fields.Float('Daily Amount', digits=(10, 2))

    charge_id = fields.Many2one('hotel.charges', string='Charge Title')
    roomtype_id = fields.Many2one('hotel.roomtypes', string='Roomtype')