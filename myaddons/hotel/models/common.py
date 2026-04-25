# -*- coding: utf-8 -*-

from odoo import fields, models


class HotelCompanyMixin(models.AbstractModel):
    _name = 'hotel.company.mixin'
    _description = 'Hotel company mixin'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        index=True,
        default=lambda self: self.env.company,
    )