# -*- coding: utf-8 -*-

from odoo import fields, models, api


class RoomTypes(models.Model):
	_name = "hotel.roomtypes"
	_description = "Hotel Room Types Master List"

	name = fields.Char("Room Type")
	description = fields.Char("Room Type Description")