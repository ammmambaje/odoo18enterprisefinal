# -*- coding: utf-8 -*-

from odoo import models, fields


class charges(models.Model):
    _name = 'hotel.charges'
    _inherit = ['hotel.company.mixin']
    _description = 'hotel charges/accounts master list'
    _order = 'name'

    dailyrate = fields.Float("Daily Rate", digits=(10,2))
    weekendrate = fields.Float("Weekend Rate", digits=(10,2))

    name = fields.Char("Account Name")
    description = fields.Char("Account Description")
    paymentaccount = fields.Boolean("Payment Account", default=False)