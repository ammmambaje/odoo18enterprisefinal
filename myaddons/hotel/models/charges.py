# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Charges(models.Model):
	_name = "hotel.charges"
	_description = "Hotel charges master list"

	name = fields.Char("Charge Name")
	description = fields.Char("Charge Description")