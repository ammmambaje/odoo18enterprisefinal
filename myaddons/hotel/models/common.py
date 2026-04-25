# -*- coding: utf-8 -*-

from odoo import fields


def company_id_field():
    return fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        index=True,
        default=lambda self: self.env.company,
    )